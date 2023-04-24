import React, { useEffect } from "react";
import { shallowEqual, useDispatch, useSelector } from "react-redux";
import { Loading } from "../../components/loading";
import { useLocalStorage } from "../../hooks/useLocalStorage";
import { getUserInventory } from "../../@redux/inventorySlice";
import {
  DefaultFilterForColumn,
  DefaultThreshholdForColumn,
} from "../../components/table";
// import AuthErrorMessage from 'components/lib/AuthErrorMessage';
import Table from "../../components/table";

export const InventoryPage = () => {
  const dispatch = useDispatch();
  const { data, error, loading, redirecting, authenticated } = useSelector(
    (s) => s.inventory,
    shallowEqual
  );

  const inventory = useSelector((s) => s.inventory.data, shallowEqual);
  const [user, setUser] = useLocalStorage("user", null);
  useEffect(() => {
    dispatch(
      getUserInventory({
        email: null,
        password: null,
        access_token: user["accessToken"],
      })
    );
  }, []);

  //   if (error) {
  //     return <AuthErrorMessage />;
  //   }

  // if (loading) {
  //   return <Loading message="Getting account details..." />;
  // }

  const columns = [
    {
      Header: "Inventory ID",
      accessor: "inventory_id",
      disableFilters: true,
      Filter: false,
    },
    {
      Header: "Product ID",
      accessor: "product_id",
      disableFilters: true,
      Filter: false,
    },
    {
      Header: "Product Name",
      accessor: "product_name",
      Filter: DefaultFilterForColumn,
    },
    {
      Header: "SKU",
      accessor: "sku",
    },
    {
      Header: "Quantity",
      accessor: "quantity",
      // disableFilters: true,
      // Filter: DefaultThreshholdForColumn,
      filter: (rows, id, filterValue) =>
        rows.filter(
          (row) => filterValue === "" || row.values[id] <= Number(filterValue)
        ),
    },
    {
      Header: "Color",
      accessor: "color",
      disableFilters: true,
      Filter: false,
    },
    {
      Header: "Size",
      accessor: "size",
      disableFilters: true,
      Filter: false,
    },
    {
      Header: "Price",
      accessor: "price_cents",
      disableFilters: true,
      Filter: false,
    },
    {
      Header: "Cost",
      accessor: "cost_cents",
      disableFilters: true,
      Filter: false,
    },
  ];

  if (inventory && inventory.length > 0) {
    return (
      <div className="min-h-screen bg-gray-100 text-gray-900">
        <main className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 pt-4">
          <div className="">
            <h1 className="text-xl font-semibold">Inventory</h1>
          </div>
          <div className="">
            <h3 className="text-l font-semibold">
              {inventory?.length}{" "}
              <span className="font-light">Inventory Available</span>
            </h3>
          </div>
          <div className="mt-6">
            <Table columns={columns} data={inventory} />
          </div>
        </main>
      </div>
    );
  }
  return <div>HI</div>;

  //   if (authenticated && user) return <WrappedComponent {...props} />;
};
