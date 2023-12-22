<template>
  <main>
    <div class="container mx-auto px-6">
      <div class="pt-10">
        <div class="font-bold text-3xl text-center text-gray-500 dark:text-white mb-3">RED NEURONAL PARA LA CLASIFICACION DE HOJAS DE LUCUMA</div>
        <div class="text-sm text-gray-500 dark:text-gray-400 mb-3">Plataforma especializada que utiliza redes neuronales para clasificar hojas de lucuma en las categorias de "sana", "seca" y "dañada". Este proyecto hace uso de la red som con aprendizaje aplicado, para clasificar imagenes que se suban en un tipo de hoja especifico.</div>
        <div><span class="font-bold text-sm text-white">Precisión: </span><span class="text-sm text-gray-500 dark:text-gray-400">89.67%</span></div>
      </div>
      <div class="my-10 lg:grid lg:grid-cols-2 lg:gap-8">
        <div
          class="block p-6 mb-6 bg-white border border-gray-200 rounded-lg shadow-md dark:bg-gray-800 dark:border-gray-700 lg:mb-0 flex justify-center">
          <div>
            <div class="relative">
              <button type="button" v-if="selectedFile" @click="clearFile"
                class="absolute right-2 top-2 bg-gray-900 rounded-md p-2 inline-flex items-center justify-center text-gray-300 hover:text-gray-400 hover:bg-gray-500 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500">
                <span class="sr-only">Close menu</span>
                <!-- Heroicon name: outline/x -->
                <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                  stroke="currentColor" aria-hidden="true">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
              <figure class="max-w-lg">
                <img class="h-auto w-full rounded-lg" :src="imgagen" alt="image description">
                <figcaption class="mt-2 text-sm text-center text-gray-500 dark:text-gray-400">Imagen Entrada</figcaption>
              </figure>
            </div>
            <div>
              <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white" for="default_img">Subir
                imagen</label>
              <input
                class="block w-full mb-5 text-sm border rounded-lg cursor-pointer text-gray-400 focus:outline-none bg-gray-700 border-gray-600 placeholder-gray-400"
                id="default_img" type="file" @input="inputFile">
            </div>
          </div>
        </div>
        <div
          class="block p-6 mb-6 bg-white border border-gray-200 rounded-lg shadow-md dark:bg-gray-800 dark:border-gray-700 lg:mb-0 flex justify-center">
          <div>
            <figure class="max-w-lg">
              <Slider :images="images"/>
              <!-- <img class="h-auto w-full rounded-lg" :src="response" alt="image description"> -->
              <figcaption class="mt-2 text-sm text-center text-gray-500 dark:text-gray-400">Imagen Salida</figcaption>
              <figcaption class="mt-2 font-bold text-center text-gray-500 dark:text-white" v-if="categoria && bmu">Categoria: {{ categoria }} | BMU: {{ bmu }}</figcaption>
            </figure>
            <div class="flex justify-center">
              <div>
                <label class="block mb-2 text-sm font-medium text-transparent" for="btn-view">Button</label>
                <button type="button" id="btn-view" @click="sendFile" :disabled="isSend"
                  class="block text-white bg-blue-700 disabled:bg-blue-500 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">
                  <span v-if="!isSend">Procesar Imagen</span>
                  <span v-else>
                    <svg aria-hidden="true" role="status" class="inline w-4 h-4 me-3 text-white animate-spin"
                      viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path
                        d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                        fill="#E5E7EB" />
                      <path
                        d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                        fill="currentColor" />
                    </svg>
                    Procesando...
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
<script>
import Slider from '../components/Slider.vue'
export default {
  components:{
    Slider
  },
  data() {
    return {
      imgagen: "https://flowbite.com/docs/images/examples/image-3@2x.jpg",
      response: "https://flowbite.com/docs/images/examples/image-3@2x.jpg",
      images: {
        "default":"https://flowbite.com/docs/images/examples/image-3@2x.jpg"
      },
      categoria: "",
      bmu: "",
      selectedFile: undefined,
      isSend: false,
    }
  },
  methods: {
    inputFile(evt) {
      this.selectedFile = evt.target.files[0]
      this.imgagen = URL.createObjectURL(this.selectedFile)
    },
    clearFile() {
      document.getElementById("default_img").value = ""
      this.imgagen = "https://flowbite.com/docs/images/examples/image-3@2x.jpg"
      this.selectedFile = undefined
    },
    async sendFile() {
      this.isSend = true
      const data = new FormData()
      data.append("file", this.selectedFile)
      const response = await Services.postFile("api/v1/hojas/upload/", data)
      this.isSend = false
      if(!response.success){
        if(response.data && response.data.file && response.data.file.length > 0){
          return Alerts.error(response.data.file[0]);
        }
        if(!response.message){
          return Alerts.error("Ocurrió un error interno");
        }
        return Alerts.error(response.message);
      }
      // this.response = 'data:image/png;base64,' + response.data.image
      this.images = response.data.images
      this.categoria = response.data.categoria
      this.bmu = response.data.bmu.toString()
    }
  }
}
</script>
