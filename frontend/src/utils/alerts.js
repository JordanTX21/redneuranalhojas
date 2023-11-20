import Swal from 'sweetalert2'


export const error = async (msg) => {
    return await Swal.fire({
        text: msg,
        icon: 'error',
        toast: true,
        timer: 2000,
        showConfirmButton: false,
      })
}

export const success = async (msg) => {
    return await Swal.fire({
        text: msg,
        icon: 'success',
        toast: true,
        timer: 2000,
        showConfirmButton: false,
      })
}