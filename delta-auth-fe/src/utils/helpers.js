export const priceInDollars = (priceInCents / 100).toLocaleString("en-US", {
  style: "currency",
  currency: "USD",
});
