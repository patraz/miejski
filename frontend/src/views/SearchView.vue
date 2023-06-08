<template>
    <section class="bg-gradient-to-b from-neutral-900 to-neutral-800 text-white body-font">
        <div class="container px-5 py-24 mx-auto flex flex-col">
            <div class="lg:w-4/6 mx-auto">
                <div class="flex flex-col sm:flex-row mt-10">
                    <WordList />
                    <SearchList :q="q"/>
                </div>
            </div>
        </div>
    </section>
</template>
  
<script>
// @ is an alias to /src
import WordList from '@/components/WordList.vue'
import SearchList from '@/components/SearchList.vue'

export default {
    name: 'SearchView',
    components: {
        WordList,
        SearchList,
    },
    
    props: {
        q: {
        type: String,
        default: ''
        }
    },
}
</script>