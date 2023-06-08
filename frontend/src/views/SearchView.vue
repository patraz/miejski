<template>
    <section class="bg-gradient-to-b from-neutral-900 to-neutral-800 text-white body-font">
        <div class="container px-5 py-24 mx-auto flex flex-col">
            <div class="lg:w-4/6 mx-auto">

                <div class="flex flex-col sm:flex-row mt-10">
                    <WordList />
                    <div
                        class="sm:w-2/3 sm:pl-8 sm:py-8 sm:border-l border-gray-200 sm:border-t-0 border-t mt-4 pt-4 sm:mt-0 text-center sm:text-left">
                        <p class="leading-relaxed text-xl mb-4">
                            <span class="font-bold text-3xl pr-2">Ściek -</span>zbiór wyrazów, wyrażeń i skrótów używanych
                            głównie w młodzieżowym i miejskim środowisku. Ten kolorowy język jest często używany w rapie,
                            hip-hopie i kulturze ulicznej. Słownik slangu ulicznego pomaga zrozumieć i porozumieć się z
                            ludźmi, którzy posługują się tym nieformalnym stylem komunikacji. Od skrótów typu "YOLO" (You
                            Only Live Once) po unikalne wyrazy jak "chillować" (odpoczywać), ten słownik odzwierciedla
                            dynamiczną i nieustannie ewoluującą naturę języka ulicy.
                        </p>
                        <a class="text-emerald-500 inline-flex items-center">Losuj słowo
                            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
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
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
    name: 'HomeView',
    components: {
        HelloWorld,

    }
}
</script>