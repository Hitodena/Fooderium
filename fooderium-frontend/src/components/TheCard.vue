<script setup>
import { defineProps } from 'vue'

const BASE_URL = 'http://localhost:8000'

const props = defineProps({
  recipe: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <router-link
    :to="`/recipes/${recipe.id}`"
    class="border rounded-lg overflow-hidden w-48 shadow-md cursor-pointer hover:bg-gray-200 transition-colors duration-200"
  >
    <img
      :src="`${BASE_URL}${recipe.image}`"
      :alt="recipe.title"
      class="w-full h-32 object-cover"
    />
    <h3 class="text-lg font-semibold p-2">{{ recipe.title }}</h3>
  </router-link>
</template>
