<script setup>
import TheCard from '@/components/TheCard.vue'
import axios from 'axios'
import { onMounted, ref } from 'vue'

const recipes = ref([])

onMounted(async () => {
  try {
    const response = await axios.get('http://localhost:8000/api/recipes/')
    recipes.value = response.data.results
  } catch (error) {
    console.error('Ошибка при получении данных:', error)
  }
})
</script>

<template>
  <div class="flex flex-wrap gap-4">
    <TheCard v-for="recipe in recipes" :key="recipe.id" :recipe="recipe" />
  </div>
</template>
