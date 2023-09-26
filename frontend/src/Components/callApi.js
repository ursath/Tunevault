import axios from 'axios'
const urlBack = "http://localhost:8000/jwt/";

const axiosBack = axios.create({
  baseURL: urlBack
});


/* ej de `param`:
{
    firstName: 'Fred',
    lastName: 'Flintstone'
}
*/
//`params` are the URL parameters to be sent with the request
export function getApi({path, param }) {
  // useEffect( () => { } )
    axiosBack.get( path, {
      params: param
    })
  .then(function (response) {
    console.log(response);
    return response;
  })
  .catch(function (error) {
    console.log(error);
  })

}  

// data:  is the data to be sent as the request body
export function postApi( {path, param, dataToPost} ) {
  
  axiosBack.post( path,{
    params: param
  }, {
    data: dataToPost 
  })
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  });
}

/*
const submit = async (e) => {
        e.preventDefault();
        await fetch('http://127.0.0.1:8000/api/profiles/', {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
            username,
            password
            })
        });
        window.location.href = '/';
    }
    */