import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import Adapter from "../services/Adapter";
import _initialState from "./_initialState";

const loginUser = createAsyncThunk(
  "user/loginUser",
  async (input, { dispatch, getState, rejectWithValue }) => {
    const { email, password, access_token } = input;
    try {
      let response;
      //   previously logged in but state dropped
      if (access_token) {
        response = await Adapter.getCurrentUser({
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

const userSlice = createSlice({
  name: "user",
  initialState: _initialState.user,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(loginUser.pending, (state) => {
        if (!state.loading) {
          state.error = null;
          state.loading = true;
        }
      })
      .addCase(loginUser.fulfilled, (state, action) => {
        if (state.loading) {
          state.loading = false;
          if (action.payload["access_token"]) {
            state.data = action.payload;
          } else {
            state.data.data.user = action.payload;
            state.authenticated = true;
          }
        }
      })
      .addCase(loginUser.rejected, (state, action) => {
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

export { loginUser };

export default userSlice.reducer;
