import React, { useEffect } from "react";
import { shallowEqual, useDispatch, useSelector } from "react-redux";
import { loginUser } from "../@redux/userSlice";
import { Loading } from "../components/loading";
import { useLocalStorage } from "./useLocalStorage";
// import AuthErrorMessage from 'components/lib/AuthErrorMessage';

const withAuth = (WrappedComponent) => (props) => {
  const dispatch = useDispatch();
  const { data, error, loading, redirecting, authenticated } = useSelector(
    (s) => s.user,
    shallowEqual
  );
  const [user, setUser] = useLocalStorage("user", null);

  useEffect(() => {
    if (user && !authenticated) {
      dispatch(
        loginUser({
          email: null,
          password: null,
          access_token: user["accessToken"],
        })
      );
    }
  }, []);

  //   if (error) {
  //     return <AuthErrorMessage />;
  //   }

  if (loading) {
    return <Loading message="Getting account details..." />;
  }

  //   if (redirecting) {
  //     return <Loading message="Redirecting you to log in..." />;
  //   }

  return <WrappedComponent {...props} />;
  return null;
};

export default withAuth;
