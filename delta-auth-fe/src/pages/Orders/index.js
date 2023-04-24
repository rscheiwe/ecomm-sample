import React from "react";
import Table from "../../components/table";

export const OrdersPage = () => {
  const userProducts = [];
  const columns = React.useMemo(
    () => [
      {
        Header: "Product ID",
        accessor: "id",
      },
      {
        Header: "Brand",
        accessor: "brand",
      },
      {
        Header: "Product Name",
        accessor: "product_name",
      },
      {
        Header: "Style",
        accessor: "style",
      },
    ],
    []
  );

  if (userProducts && userProducts.length > 0) {
    return (
      <div className="min-h-screen bg-gray-100 text-gray-900">
        <main className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 pt-4">
          <div className="">
            <h1 className="text-xl font-semibold">Orders</h1>
          </div>
          <div className="">
            <h3 className="text-l font-semibold">
              {userProducts.length}{" "}
              <span className="font-light">Orders Available</span>
            </h3>
          </div>
          <div className="mt-6">
            <Table columns={columns} data={userProducts} />
          </div>
        </main>
      </div>
    );
  }
  return <div className="m-10 font-bold">Under Construction!</div>;
};
