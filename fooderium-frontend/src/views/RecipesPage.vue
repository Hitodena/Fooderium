<template>
  <div class="p-4">
    <InfoAbout :recipe="recipe" />
    <IngredientsList :products="recipe.recipe_products" />
    <RecipeSteps :steps="recipe.steps" />
    <CommentsBlock :comments="comments" />
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import CommentsBlock from '@/components/CommentsBlock.vue'
import InfoAbout from '@/components/InfoAbout.vue'
import IngredientsList from '@/components/IngredientsList.vue'
import RecipeSteps from '@/components/RecipeSteps.vue'

const route = useRoute()
const recipe = ref({})
const comments = ref([])

onMounted(async () => {
  await fetchRecipe()
  await fetchComments()
})

async function fetchRecipe() {
  const response = await fetch(
    `http://localhost:8000/api/recipes/${route.params.id}`,
  )
  recipe.value = await response.json()
}

async function fetchComments() {
  const response = await fetch(`http://localhost:8000/api/comments/`)
  const data = await response.json()
  comments.value = data.results.filter(
    comment => comment.recipe === recipe.value.id,
  )
}
</script>
