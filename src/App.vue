<script setup>
import { RouterView } from 'vue-router'
import { ref } from 'vue'
import debounce from 'lodash.debounce'
import axios from 'axios'

const searchQuery = ref('')
const handleSearch = debounce(async (query) => {
  try {
    const response = await axios.get('http://127.0.0.1:5001/recommend', {
      params: { title: query },
    });
    const recommendations = response.data;
    const event = new CustomEvent('search-query', { detail: recommendations });
    // console.log('Recommendations:', recommendations);
    window.dispatchEvent(event);
  } catch (error) {
    console.error('Error fetching recommendations:', error);
  }
}, 700)
</script>

<template>
  <header class="flex items-center justify-center sm:justify-around h-16 text-primary font-knewave sm:flex-nowrap flex-wrap gap-2">
    <h1 class="lg:text-4xl text-2xl">Book Recommendation</h1>
    <div class="ml-4">
      <input
        type="text"
        placeholder="Get Recommend Books..."
        class="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary w-[250px] md:w-[400px]"
        v-model="searchQuery"
        @input="handleSearch(searchQuery)"
      />
    </div>
  </header>

  <RouterView />
</template>
