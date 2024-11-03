<template>
  <div class="flex flex-wrap gap-4">
    <TheCard v-for="recipe in recipes" :key="recipe.id" :recipe="recipe" />
  </div>
</template>

<script setup>
import { defineProps } from 'vue'
import TheCard from './TheCard.vue'

const props = defineProps({
  recipes: {
    type: Array,
    required: true,
  },
})
</script>
