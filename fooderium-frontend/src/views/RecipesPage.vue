<script setup>
import CommentsBlock from '@/components/CommentsBlock.vue'
import IngredientsList from '@/components/IngredientsList.vue'
import RecipeSteps from '@/components/RecipeSteps.vue'
import axios from 'axios'
import { onMounted, ref } from 'vue'

const props = defineProps(['id'])

const recipe = ref({})
const comments = ref([])

onMounted(async () => {
  try {
    console.log('Загрузка данных о рецепте с id:', props.id)
    const recipeResponse = await axios.get(
      `http://localhost:8000/api/recipes/${props.id}/`,
    )
    recipe.value = recipeResponse.data
    console.log('Данные о рецепте:', recipe.value)

    const commentsResponse = await axios.get(
      `http://localhost:8000/api/comments/?recipe=${props.id}`,
    )
    comments.value = commentsResponse.data.results || []
    console.log('Комментарии:', comments.value)
  } catch (error) {
    console.error('Ошибка при загрузке данных:', error)
  }
})
</script>

<template>
  <div
    v-if="recipe.title"
    class="max-w-3xl mx-auto p-6 bg-white rounded-lg shadow-md"
  >
    <h1 class="text-3xl font-bold mb-4">{{ recipe.title }}</h1>
    <img
      :src="recipe.image_url"
      alt="Рецепт"
      class="w-full h-auto max-w-xs mx-auto"
    />
    <p class="text-gray-700 mb-4">{{ recipe.description }}</p>

    <div class="bg-gray-100 p-4 rounded-lg mb-4">
      <h2 class="text-xl font-semibold mb-2">Пищевая ценность</h2>
      <p>
        Калории: <span class="font-medium">{{ recipe.calories }}</span>
      </p>
      <p>
        Белки: <span class="font-medium">{{ recipe.proteins }}</span>
      </p>
      <p>
        Жиры: <span class="font-medium">{{ recipe.fats }}</span>
      </p>
      <p>
        Углеводы: <span class="font-medium">{{ recipe.carbs }}</span>
      </p>
    </div>

    <IngredientsList
      v-if="recipe.recipe_products.length"
      :products="recipe.recipe_products"
    />
    <RecipeSteps v-if="recipe.steps.length" :steps="recipe.steps" />

    <div class="mt-4">
      <h2 class="text-xl font-semibold mb-2">Комментарии</h2>
      <CommentsBlock v-if="comments.length" :comments="comments" />
      <p v-else class="text-gray-500">Пока нет комментариев.</p>
    </div>
  </div>
  <div v-else class="text-center">Загрузка...</div>
</template>
