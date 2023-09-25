function callApi(path, method, body, sucess, fail) {
    fetch("https://localhost:8000" + path, {    // <--- changed from "" to "https://localhost:8000"
      headers: {
      //   Authorization: 'Basic SGVsbG8gdGhlcmUgOikgSGF2ZSBhIGdvb2QgZGF5IQ==',
      //   'Content-Type': 'application/json',
      // },
      body: JSON.stringify(body),
    });
  }
  export default callApi;