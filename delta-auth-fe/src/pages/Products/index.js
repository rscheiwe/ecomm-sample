import React, { useState } from "react";
import Table from "../../components/table";
import { useSelector } from "react-redux";

export const ProductsPage = () => {
  const userProducts = useSelector((s) => s.user.data.data.user?.products);
  const columns = React.useMemo(
    () => [
      {
        Header: "Product ID",
        accessor: "id",
        disableFilters: true,
        Filter: false,
      },
      {
        Header: "Brand",
        accessor: "brand",
        disableFilters: true,
        Filter: false,
      },
      {
        Header: "Product Name",
        accessor: "product_name",
        disableFilters: true,
        Filter: false,
      },
      {
        Header: "Style",
        accessor: "style",
        disableFilters: true,
        Filter: false,
      },
    ],
    []
  );

  if (userProducts && userProducts.length > 0) {
    return (
      <div className="min-h-screen bg-gray-100 text-gray-900">
        <main className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 pt-4">
          <div className="">
            <h1 className="text-xl font-semibold">Products</h1>
          </div>
          <div className="">
            <h3 className="text-l font-semibold">
              {userProducts?.length}{" "}
              <span className="font-light">Products Available</span>
            </h3>
          </div>
          <div className="mt-6">
            <Table columns={columns} data={userProducts} />
          </div>
        </main>
      </div>
    );
  }
  return <div>Please Refresh</div>;
};
