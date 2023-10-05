import { IoRocketSharp } from "react-icons/io5"
import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="hero min-h-screen bg-base-200">
      <div className="hero-content text-center">
        <div className="max-w-md">
          <h1 className="text-5xl font-bold font-chalkboard animate-text bg-gradient-to-r from-accent via-accent-focus to-primary-focus bg-clip-text text-transparent">Hello there</h1>
          <p className="py-6">
            Welcome to <b>MyPeeps</b>
          </p>
          <Link to="/login" className="btn btn-primary">
            GET STARTED <IoRocketSharp/>
          </Link>
        </div>
      </div>
    </div>
  );
}
export default Home;
