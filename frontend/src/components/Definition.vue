<template>
    <div class="sm:w-2/3 sm:pl-8 sm:py-8 sm:border-l border-gray-200 sm:border-t-0 border-t mt-4 pt-4 sm:mt-0 text-center sm:text-left">
        <div class="p-6 rounded-lg"><h3 class="tracking-widest text-emerald-400 mb-3 text-xs font-medium title-font">SŁOWO</h3><h2 class="text-lg text-white font-medium title-font mb-4">{{word.word}}</h2>
        <h3 class="tracking-widest text-emerald-400 text-xs font-medium title-font mt-3 mb-3">ZNACZENIE</h3>
        <p>{{ slug }}</p>
        <div class="bg-neutral-700 p-6 rounded-lg"><p class="leading-relaxed text-base">{{word.meaning}}</p></div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'

export default {
    name: 'Definition',
    data() {
          return {
              word: {}
          }
    },
    watch: {
        $route(to, from) {
        // Wykonaj działania w przypadku zmiany adresu URL
        this.getWord();
        },
    },
    async mounted() {
        console.log('mounted')

        let slug = this.$route.params.slug

        this.getWord()

        document.title = this.word.word + ' | Ściek'
    },
    methods: {
        async getWord(){
            let slug = this.$route.params.slug

            await axios
                .get(`/api/v1/definitions/${slug}/`)
                .then(response => {
                    console.log(response.data)
                    this.word = response.data
                })
        }
    }
  }
</script>