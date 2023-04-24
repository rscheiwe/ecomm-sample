import { combineReducers } from "redux";
import userSlice from "./userSlice";
import inventorySlice from "./inventorySlice";

export default combineReducers({
  user: userSlice,
  inventory: inventorySlice,
});
