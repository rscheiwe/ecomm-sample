import FormData from "form-data";

const BASE_URL = "http://localhost:8000";

const baseHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Content-Type": "application/json",
  Accept: "application/json",
};

const authHeaders = (token) => ({ Authorization: `Bearer ${token}` });

const Adapter = {
  async loginUser({ email, password }) {
    const url = `${BASE_URL}/token`;
    const bodyFormData = new FormData();

    bodyFormData.append("username", email);
    bodyFormData.append("password", password);
    const res = await fetch(url, {
      method: "POST",
      body: bodyFormData,
    });
    const parsed = await res.json();

    if (parsed.error) {
      // throw new Errors.PortalError(parsed.message);
    }

    return parsed;
  },

  async getCurrentUser({ token }) {
    const url = `${BASE_URL}/delta-users/current-user`;
    const currentUserAuthHeaders = authHeaders(token);
    const headers = { ...baseHeaders, ...currentUserAuthHeaders };
    const res = await fetch(url, {
      method: "GET",
      headers: { ...baseHeaders, ...currentUserAuthHeaders },
    });

    const parsed = await res.json();
    if (parsed.error) {
      // throw new Errors.PortalError(parsed.message);
    }

    return parsed;
  },
  async getCurrentUserInventory({ token }) {
    const url = `${BASE_URL}/delta-inventory/current-user-inventory`;
    const currentUserAuthHeaders = authHeaders(token);
    const headers = { ...baseHeaders, ...currentUserAuthHeaders };
    const res = await fetch(url, {
      method: "GET",
      headers: { ...baseHeaders, ...currentUserAuthHeaders },
    });

    const parsed = await res.json();
    if (parsed.error) {
      // throw new Errors.PortalError(parsed.message);
    }

    return parsed;
  },
};
export default Adapter;
