import axios from 'axios';
import urljoin from 'url-join';
const urlBack = "127.0.0.1:8000/";

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
export function postApi( {path, dataToPost} ) {

  const fullUrl = urljoin(urlBack, path); // Concatenate the base URL and path using urljoin
  const url = "127.0.0.1:8000/register/";
  axios.post(url, 
    dataToPost 
  );
  axiosBack.post(url, 
    dataToPost 
  )
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  }); 
}
