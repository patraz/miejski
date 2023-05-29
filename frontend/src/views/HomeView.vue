<template>
  <div class="home">
    <Nav/>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import Nav from '@/components/Nav.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld,
    Nav
  }
}
</script>
