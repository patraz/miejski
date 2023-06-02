<template>
  <section class="bg-gradient-to-b from-neutral-900 to-neutral-800 text-white body-font">
    <div class="container px-5 py-24 mx-auto flex flex-col">
      <div class="lg:w-4/6 mx-auto">

        <div class="flex flex-col sm:flex-row mt-10">
          <div class="sm:w-1/3 text-center sm:pr-8 sm:py-8">
            <h1 class="tracking-widest text-white text-3xl mb-3 font-bold title-font">NOWE SŁOWA</h1>
            <ul class="max-w-full space-y-1 text-white font-bold list-inside"  
                            >
              <li class="flex items-center"
                            v-for="word in words"
                            v-bind:key="word.id">
                <svg fill="currentColor" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" 
                class="w-4 h-4 mr-1.5 text-emerald-400 dark:text-emerald-400 flex-shrink-0" aria-hidden="true">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09zM18.259 8.715L18 9.75l-.259-1.035a3.375 3.375 0 00-2.455-2.456L14.25 6l1.036-.259a3.375 3.375 0 002.455-2.456L18 2.25l.259 1.035a3.375 3.375 0 002.456 2.456L21.75 6l-1.035.259a3.375 3.375 0 00-2.456 2.456zM16.894 20.567L16.5 21.75l-.394-1.183a2.25 2.25 0 00-1.423-1.423L13.5 18.75l1.183-.394a2.25 2.25 0 001.423-1.423l.394-1.183.394 1.183a2.25 2.25 0 001.423 1.423l1.183.394-1.183.394a2.25 2.25 0 00-1.423 1.423z"></path>
              </svg> 
            
                <RouterLink :to="word.slug" class="hover:text-emerald-400" >{{word.word}}</RouterLink>
              </li>
              
            </ul>

          </div>
          <div class="sm:w-2/3 sm:pl-8 sm:py-8 sm:border-l border-gray-200 sm:border-t-0 border-t mt-4 pt-4 sm:mt-0 text-center sm:text-left">
            <p class="leading-relaxed text-xl mb-4">
<span class="font-bold text-3xl pr-2">Ściek -</span>zbiór wyrazów, wyrażeń i skrótów używanych głównie w młodzieżowym i miejskim środowisku. Ten kolorowy język jest często używany w rapie, hip-hopie i kulturze ulicznej. Słownik slangu ulicznego pomaga zrozumieć i porozumieć się z ludźmi, którzy posługują się tym nieformalnym stylem komunikacji. Od skrótów typu "YOLO" (You Only Live Once) po unikalne wyrazy jak "chillować" (odpoczywać), ten słownik odzwierciedla dynamiczną i nieustannie ewoluującą naturę języka ulicy.</p>
            <a class="text-emerald-500 inline-flex items-center">Losuj słowo
              <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
                <path d="M5 12h14M12 5l7 7-7 7"></path>
              </svg>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>



<script>
import axios from 'axios'

export default {
  data() {
        return {
            words: []
        }
  },
  name: 'HelloWorld',
  props: {
    msg: String
  },
  async mounted() {
        console.log('mounted')

        await axios
            .get('/api/v1/definitions/')
            .then(response => {
                console.log(response.data)
                this.words = response.data
            })

        document.title = 'Slang | Ściek'
    }
  
}
</script>

