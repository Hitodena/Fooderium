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

<template>
  <div class="flex flex-wrap gap-4 justify-center">
    <TheCard
      v-for="(recipe, index) in recipes"
      :key="recipe.id"
      :recipe="recipe"
      :style="{ animation: `fadeIn 0.5s ease forwards ${index * 0.1}s` }"
      class="opacity-0"
    />
  </div>
</template>

<style scoped>
@keyframes fadeIn {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.opacity-0 {
  opacity: 0;
  transform: translateY(20px);
}
</style>
