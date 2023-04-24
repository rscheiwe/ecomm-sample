import React from "react";
import { useSelector } from "react-redux";
import { useLocalStorage } from "../hooks/useLocalStorage";
import { Link, Navigate, useLocation, useOutlet } from "react-router-dom";
import { useAuth } from "../hooks/useAuth";

import { dashboardLinks } from "../utils/dashboardLinks";
import withAuth from "../hooks/withAuth";

const ProtectedLayout = () => {
  const { user, logout } = useAuth();
  const { data } = useSelector((s) => s.user);
  const currentUser = data?.data?.user;
  const location = useLocation();

  const outlet = useOutlet();

  if (!user) {
    return <Navigate to="/" />;
  }

  return (
    <div className="grid grid-cols-[300px_1fr] h-screen max-h-screen">
      <div className="flex flex-col text-white overflow-hidden">
        <div className="bg-slate-800 px-2">
          <Link href="/token-topup" className="block mt-2 text-center">
            <span className="pl-1">{currentUser?.shop_name}</span>
          </Link>
        </div>
        <div className="px-4 flex-1 overflow-auto bg-gradient-to-b from-slate-800 to-cyan-800">
          {dashboardLinks.map((dashboardLink) => (
            <Link
              key={dashboardLink.id}
              to={`/dashboard/${dashboardLink.href}`}
              className={`py-1 hover:bg-white/20 border border-white/0 block text-ellipsis overflow-hidden whitespace-nowrap my-1 px-2 bg-white/10 cursor-pointer rounded-sm ${
                location.pathname === `/dashboard/${dashboardLink.href}`
                  ? "bg-white/20 border-white"
                  : ""
              }`}
            >
              {dashboardLink.linkName}
            </Link>
          ))}
        </div>
        <div className="bg-cyan-800 flex items-center gap-2 border-t border-t-black/50 h-20 px-2">
          {!!currentUser ? (
            <>
              <div className="min-w-[50px]">
                <img
                  src={
                    "https://cdn4.iconfinder.com/data/icons/basics-set-2/100/User_Profile-512.png"
                  }
                  alt={currentUser.username}
                  height={50}
                  width={50}
                  className="rounded-full bg-white"
                />
              </div>
              <div className="flex-1">
                <div className="font-bold">{currentUser.email}</div>
                <div className="text-sm">
                  <button
                    key={"logout"}
                    onClick={logout}
                    className="mt-2 border border-solid border-black py-2 px-4 rounded cursor-pointer"
                  >
                    Logout
                  </button>
                </div>
              </div>
            </>
          ) : (
            <Link href="/api/auth/login">Login</Link>
          )}
        </div>
      </div>
      {outlet}
    </div>
  );
};

export default withAuth(ProtectedLayout);
