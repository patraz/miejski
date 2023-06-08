<template>
    <div
        class="sm:w-2/3 sm:pl-8 sm:py-8 sm:border-l border-gray-200 sm:border-t-0 border-t mt-4 pt-4 sm:mt-0 text-center sm:text-left">
        <h1 class="text-2xl text-white font-bold title-font">Wyniki wyszukiwania "{{ this.q }}"</h1>
        <ul>
            <li class="w-full p-2" v-for="word in searchResults" v-bind:key="word.slug">
                <div class="bg-neutral-700 p-5 rounded-lg">
                    <p class=" text-emerald-400 text-xl mb-3 title-font uppercase">{{ word.word }}</p>
                    <p class=" text-white-400 text-l mb-3 title-font">"{{ word.meaning.slice(0, 30) }}..."" <RouterLink
                            :to="'/' + word.slug" class="text-bold text-emerald-300 hover:text-emerald-500">kliknij po
                            więcej</RouterLink>
                    </p>
                </div>
            </li>

        </ul>
    </div>
</template>

<script>

import axios from 'axios'
export default {
    name: 'SearchList',
    data() {
        return {
            searchResults: [],
        }
    },
    props: {
        q: {
        type: String,
        required: true
        }
    },
    watch: {
        q(to, from) {
        // Wykonaj działania w przypadku zmiany adresu URL
        this.getSearch();
        },
    },
    async mounted() {
        this.getSearch()
    },
    methods: {
        async getSearch(){
            await axios
            .get(`/api/v1/definitions/search/`, {
                params: {
                    q: this.q
                }
            })
            .then(response => {
                // Handle the response data
                console.log(response)
                console.log(response.data);
                this.searchResults = response.data

            })
            .catch(error => {
                // Handle any errors
                console.error(error);
            });
            document.title ='Szukaj | Ściek'
        }
    }
}
</script>