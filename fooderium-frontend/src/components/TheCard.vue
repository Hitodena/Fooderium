<template>
  <div class="border rounded-lg overflow-hidden w-48 shadow-md">
    <img
      :src="recipe.image"
      :alt="recipe.title"
      class="w-full h-32 object-cover"
    />
    <h3 class="text-lg font-semibold p-2">{{ recipe.title }}</h3>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'

const props = defineProps({
  recipe: {
    type: Object,
    required: true,
  },
})
</script>
