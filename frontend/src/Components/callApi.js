import axios from 'axios'
const urlBack = "http://127.0.0.1:8000/";

const axiosBack = axios.create({
  baseURL: urlBack,  

});


/* ej de `param`:
{
    firstName: 'Fred',
    lastName: 'Flintstone'
}

headers: {
    'Content-Type': 'application/json',}
*/
//`params` are the URL parameters to be sent with the request
export function getApi(path) {
  // useEffect( () => { } )
    axiosBack.get( path)
  .then(function (response) {
    console.log(response.data);
    return response.data;
  })
  .catch(function (error) {
    console.log(error);
  })

}  

// data:  is the data to be sent as the request body
export function postApi( {path, param, dataToPost} ) {
  
  axiosBack.post( 'api/users/',{
      email: "androminguez@gmail.com",
      username: "swaasm",
      password: "fuaaaPibexlmi",
      re_password: "fuaaaPibexlmi"
  })
  .then(function (response) {
    console.log(response.data);
  })
  .catch(function (error) {
    console.log('hola');
    console.log(error.data);
  });
  return getApi('api/',{});
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