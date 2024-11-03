<template>
  <div class="p-4">
    <h1 class="text-2xl font-bold mb-4">Список Рецептов</h1>
    <input
      type="text"
      v-model="search"
      placeholder="Поиск рецептов..."
      class="border p-2 mb-4 w-full"
    />
    <CardList :recipes="filteredRecipes" />
  </div>
</template>

<script setup>
import CardList from '@/components/CardList.vue'
import { computed, onMounted, ref } from 'vue'

const recipes = ref([])
const search = ref('')

onMounted(async () => {
  await fetchRecipes()
})

async function fetchRecipes() {
  const response = await fetch('http://localhost:8000/api/recipes/')
  const data = await response.json()
  console.log(response)
  recipes.value = data.results
}

const filteredRecipes = computed(() => {
  return recipes.value.filter(recipe => {
    return recipe.title.toLowerCase().includes(search.value.toLowerCase())
  })
})
</script>
