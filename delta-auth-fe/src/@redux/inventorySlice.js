import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import Adapter from "../services/Adapter";
import _initialState from "./_initialState";

const getUserInventory = createAsyncThunk(
  "inventory/getUserInventory",
  async (input, { dispatch, getState, rejectWithValue }) => {
    const { email, password, access_token } = input;
    try {
      let response;
      //   previously logged in but state dropped
      if (access_token) {
        response = await Adapter.getCurrentUserInventory({
          token: access_token,
        });

        return response;
      } else {
        // fresh login for token
        response = await Adapter.loginUser({
          email,
          password,
        });
        return response;
      }
    } catch (err) {
      if (!err.response) {
        throw err;
      }
      return rejectWithValue(err.response.data);
    }
  },
  {
    dispatchConditionRejection: true,
  }
);

const inventorySlice = createSlice({
  name: "inventory",
  initialState: _initialState.inventory,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(getUserInventory.pending, (state) => {
        if (!state.loading) {
          state.error = null;
          state.loading = true;
        }
      })
      .addCase(getUserInventory.fulfilled, (state, action) => {
        if (state.loading) {
          state.loading = false;
          state.data = action.payload;
        }
      })
      .addCase(getUserInventory.rejected, (state, action) => {
        if (state.loading) {
          state.loading = false;
          state.error =
            action.error.message ||
            action.payload?.errorMessage ||
            "status 404";
        }
      });
  },
});

export { getUserInventory };

export default inventorySlice.reducer;
