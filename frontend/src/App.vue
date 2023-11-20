<template>
  <RouterView />
</template>
<script>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
export default {
  components: {
    RouterLink, RouterView, HelloWorld
  },
  data() {
    return {}
  }
}
</script>
<style scoped></style>
