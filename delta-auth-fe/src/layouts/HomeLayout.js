import { Navigate, Outlet } from "react-router-dom";
import { useAuth } from "../hooks/useAuth";
import { Link } from "react-router-dom";
import { useSelector } from "react-redux";

export const HomeLayout = () => {
  const { user } = useAuth();
  const { authenticated } = useSelector((s) => s.user);

  if (user) {
    return <Navigate to="/dashboard/profile" />;
  }

  return (
    <div>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/login">Login</Link>
      </nav>
      <Outlet />
    </div>
  );
};
