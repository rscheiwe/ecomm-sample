import { sanitizeError } from "../../utils/errors";

const ErrorAction =
  (type) =>
  ([error, payload]) => ({
    type,
    payload,
    error,
  });

const handleErrors =
  ({ dispatch, getState }) =>
  (next) =>
  (action) => {
    if (action.type === "ASYNC") {
      const errorAction = ErrorAction(action.errorType);
      return action.handler(dispatch, getState).catch((e) => {
        if (process.env.NODE_ENV !== "test") {
          console.error(e);
        }
        const error = sanitizeError(e);
        const payload = action.getErrorPayload(error);
        dispatch(errorAction(payload));
      });
    }
    return next(action);
  };

export default handleErrors;
