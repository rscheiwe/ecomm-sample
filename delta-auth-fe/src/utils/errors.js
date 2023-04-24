class ConnectionError extends Error {
  static message = `Could not connect to the client-properties api.`;

  constructor() {
    super(ConnectionError.message);
  }
}

class GenericError extends Error {
  static message = `There was an unknown problem with your request.`;

  constructor() {
    super(GenericError.message);
  }
}

const Errors = {
  ConnectionError,

  GenericError,
};

const checkNetworkError = (e) => {
  if (
    e.message.toLowerCase().includes("network") || // for firefox
    e.message.toLowerCase().includes("fetch") // for chrome
  )
    return new Errors.ConnectionError();
  return e;
};

const checkGenericError = (e) => {
  if (!Object.values(Errors).some((type) => e instanceof type)) {
    return new Errors.GenericError();
  }
  return e;
};

export const sanitizeError = (e) => checkGenericError(checkNetworkError(e));
