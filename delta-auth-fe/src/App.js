import { Route, Routes, useLocation } from "react-router-dom";
import { LoginPage } from "./pages/Login";
import { HomePage } from "./pages/Home";
import { ProfilePage } from "./pages/Profile";
import { ProductsPage } from "./pages/Products";
import { InventoryPage } from "./pages/Inventory";
import ProtectedLayout from "./layouts/ProtectedLayout";
import { OrdersPage } from "./pages/Orders";
import { HomeLayout } from "./layouts/HomeLayout";
import withAuth from "./hooks/withAuth";

function App() {
  return (
    <Routes>
      <Route element={<HomeLayout />}>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<LoginPage />} />
      </Route>
      <Route path="/dashboard" element={<ProtectedLayout />}>
        <Route path="profile" element={<ProfilePage />} />
        <Route path="products" element={<ProductsPage />} />
        <Route path="inventory" element={<InventoryPage />} />
        <Route path="orders" element={<OrdersPage />} />
      </Route>
    </Routes>
  );
}
export default App;
// export default withAuth(App);
