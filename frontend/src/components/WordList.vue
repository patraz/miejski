<template>
    <div class="sm:w-1/3 text-center sm:pr-8 sm:py-8">
        <h1 class="tracking-widest text-white text-2xl mb-3 font-bold title-font">OSTATNIE 10 SŁÓW</h1>
        <ul class="max-w-full space-y-1 text-white font-bold list-inside"  
                                >
            <li class="flex items-center"
                                v-for="word in words"
                                v-bind:key="word.id">
                <svg fill="currentColor" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" 
                    class="w-4 h-4 mr-1.5 text-emerald-400 dark:text-emerald-400 flex-shrink-0" aria-hidden="true">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09zM18.259 8.715L18 9.75l-.259-1.035a3.375 3.375 0 00-2.455-2.456L14.25 6l1.036-.259a3.375 3.375 0 002.455-2.456L18 2.25l.259 1.035a3.375 3.375 0 002.456 2.456L21.75 6l-1.035.259a3.375 3.375 0 00-2.456 2.456zM16.894 20.567L16.5 21.75l-.394-1.183a2.25 2.25 0 00-1.423-1.423L13.5 18.75l1.183-.394a2.25 2.25 0 001.423-1.423l.394-1.183.394 1.183a2.25 2.25 0 001.423 1.423l1.183.394-1.183.394a2.25 2.25 0 00-1.423 1.423z"></path>
                </svg> 
                
                <RouterLink :to="word.word" class="hover:text-emerald-400" ></RouterLink>
                <router-link :to="{ name: 'Definition', params: { slug: word.slug } }">{{word.word}}</router-link>
            </li>
                    
        </ul>
    </div>
</template>
  
  
  
  <script>
  import axios from 'axios'
  
  export default {
    data() {
          return {
              words: []
          }
    },
    name: 'WordList',
    async mounted() {
          await axios
              .get('/api/v1/definitions/last-definitions/')
              .then(response => {
                  console.log(response.data)
                  this.words = response.data
              })
      }
    
  }
  </script>