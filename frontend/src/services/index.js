import axios from "axios";
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

const domain = location.origin

const postFile = async (url, data) => {
    console.log(data)
    try{
        const response = await axios.post(`${domain}/${url}`, data)
        console.log(response.data)
        return response.data
    }catch(e){
        if(e.response){
            console.log(e.response.data)
            return e.response.data
        }
        return {"success":false,"message":"Ocurrió un error Interno","data":e}
    }
}

export {
    postFile,
}