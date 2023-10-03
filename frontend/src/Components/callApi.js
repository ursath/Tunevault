import axios from 'axios'
import { errorAlert } from './errorAlert';
import { Exception } from 'sass';
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

    axiosBack.get( path)
  .then(function (response) {
    console.log(response.data);
    return response.data;
  })
  .catch(function (error) {
    console.log(error);
  })

}  
/*
{
      email: "androminguez@gmail.com",
      username: "sawaasm",
      password: "fuaaaPibexlmi",
      re_password: "fuaaaPibexlmi"
  }
*/

// data:  is the data to be sent as the request body
// con return 0,1 veo si fue exitoso
export async function postApiDisplayError( path, dataToPost ) {
  
  const ret = axiosBack.post( path,dataToPost)
  .then(function (response) {
    console.log(response.data);
    return 0;
  })
  .catch(function (error) {
    // ya imprime errores
    let ans =  Object.values(error.response.data).flat();
    //console.log(ans);
    errorAlert(ans);
    return -1;
  });
  
  return ret;
}

export async function postApi( path, dataToPost ) {
   
  const ret = axiosBack.post( path,dataToPost)
  .then(function (response) {
    console.log(response.data);
    return 0;
  })
  .catch(function (error) {
    console.log(error.response.data);
    return -1;
  });
   
  //return getApi('api/comments/',{});
  return ret;
}
