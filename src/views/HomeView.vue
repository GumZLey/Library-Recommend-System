<script setup>
import { ref } from 'vue'
import BookComponent from '../components/BookComponent.vue'

const bookData = ref([
])

const searchQuery = ref('')

window.addEventListener('search-query', (event) => {
  searchQuery.value = event.detail
  bookData.value = []
  fetchBooks(searchQuery.value)
})

const fetchBooks = async (query = '') => {
  try {
    query.forEach(async (element) => {
      const response = await fetch(
        `https://openlibrary.org/search.json?q=${encodeURIComponent(element[0])}&limit=1`,
      )
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()
      bookData.value.push(
        data.docs.map((book) => ({
          id: book.cover_i,
          title: book.title,
          author: book.author_name ? book.author_name.join(', ') : 'Unknown',
          image: book.cover_i ? `https://covers.openlibrary.org/b/id/${book.cover_i}-L.jpg` : null,
          score: element[1],
        })),
      )
      bookData.value.sort((a, b) => b[0].score - a[0].score)
    })

  } catch (error) {
    console.error('Error fetching books:', error)
  }
}


</script>

<template>
  <main
    class="flex flex-row justify-center flex-wrap min-h-screen bg-dark-bg/20 mx-4 md:mx-20 my-10 rounded-4xl"
  >
    <div v-for="book in bookData" :key="book.id">
      <BookComponent :bookData="book" />
    </div>
  </main>
</template>
