from django.test import TestCase

from api.models import Peeps, PeepsMetric
from mypeeps.settings import ACTIONS
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