<script setup>

defineProps({
  bookData: {
    type: Object,
    required: true,
  }
})

</script>

<template>
  <div class="">
    <div
      class="flex flex-col items-center justify-center bg-dark-bg/20 m-4 rounded-4xl p-8 gap-4 w-[300px] h-[400px] shadow-lg hover:shadow-2xl transition-shadow duration-300 ease-in-out"
    >
    <img
      v-if="bookData[0].image"
      :src="bookData[0].image"
      alt=""
      srcset=""
      class="w-[150px] h-[200px] object-cover mt-2"
    />
      <h2 class="text-white text-center font-knewave text-2xl">{{ bookData[0].title }}</h2>
      <h2 class="text-white font-[Popins] text-md font-normal">{{ bookData[0].author }}</h2>
      <h2 class="text-white font-[Popins] text-md font-normal">Score: {{ bookData[0].score }}</h2>
    </div>
  </div>
</template>
