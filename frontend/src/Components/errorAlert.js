import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

//! Hay q incluir <ToastContainer /> en la pag donde vaya a aparecer

const notify = (msg) => toast.error(msg);

export  function errorAlert(ans) {
    for (const msg in ans ){
        console.log(ans[msg]);
        notify(ans[msg]);
    }  
    return -1;
}
