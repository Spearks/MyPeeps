from django.test import TestCase
from django.utils import timezone

from api.models import Peeps, PeepsMetric
from accounts.models import User

from mypeeps.settings import ACTIONS
from rest_framework_simplejwt.tokens import RefreshToken

actions = ACTIONS

# Create your tests here.

class PeepsTest(TestCase):

    def test_peeps_name_is_lowercased_and_spaces_replaced(self):
        peeps = Peeps(name="Test Peeps")
        peeps.save()
        self.assertEqual(peeps.name, "test_peeps")

    def test_random_seed_generated_if_not_provided(self):
        peeps = Peeps(name="New peeps")
        peeps.save()
        self.assertTrue(peeps.seed is not None)

    def test_attributes_default_to_random_values(self):
        peeps = Peeps(name="New peeps")
        peeps.save()
        self.assertGreaterEqual(peeps.attribute_creativity, 0)
        self.assertLessEqual(peeps.attribute_creativity, 0.5)

    def test_peeps_metric_created_on_peeps_save(self):
        peep = Peeps.objects.create(name="Test")
        action = list(actions.keys())

        PeepsMetric(action=action[0], peep=peep, attribute_hp=100, attribute_creativity=0, attribute_romance=0).save()
        self.assertEqual(PeepsMetric.objects.count(), 1)

from rest_framework.test import APIClient

class PeepsActionsViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a Peeps object 
        self.peep = Peeps.objects.create(
        name="Test Peep"
        )

        # Create a sample user
        self.user = User.objects.create_user(
        username='test', 
        email='test@example.com',
        password='password'
        )

        # Create sample JWT
        refresh = RefreshToken.for_user(self.user)
        jwt = str(refresh.access_token)

        # Authenticate client
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {jwt}')
    
    def test_post_action(self):
        # Create POST data
        data = {
            "name": "Read",
            "options": {"name": "Read Pablo Neruda"}, 
            "peep": self.peep.id
        }

        # Make POST request
        response = self.client.post('/api/v1/peeps/actions', data, format='json')

        # Assert status code
        self.assertEqual(response.status_code, 200)

        # Assert response data
        self.assertEqual(response.data['message'], "Successful action")

        # Assert Peeps data was updated
        updated_peep = Peeps.objects.get(id=self.peep.id)  
        self.assertEqual(updated_peep.attribute_romance, self.peep.attribute_romance + 2.2)

        # Assert PeepsMetric object was created
        self.assertEqual(PeepsMetric.objects.count(), 1)

        metric = PeepsMetric.objects.first()
        self.assertEqual(metric.peep, self.peep)
        
    def test_rate_limit(self):
        # Create metric in past
        PeepsMetric.objects.create(
            peep=self.peep,
            action="Read Pablo Neruda",
            time=timezone.now()-timezone.timedelta(minutes=1),
            attribute_hp=100, attribute_creativity=0, attribute_romance=0
        )

        data = {
            "name": "Read",
            "options": {"name": "Read Pablo Neruda"}, 
            "peep": self.peep.id
        }

        # Make POST request 
        response = self.client.post('/api/v1/peeps/actions', data, format='json')

        # Assert rate limit response
        self.assertEqual(response.data['message'], "Action are in throttle-limited")