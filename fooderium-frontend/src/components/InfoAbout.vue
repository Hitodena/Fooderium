<script setup>
import { defineProps } from 'vue'

const props = defineProps({
  recipe: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <div class="mb-4">
    <h1 class="text-2xl font-bold">{{ recipe.title }}</h1>
    <img
      :src="recipe.image_url"
      alt="Recipe Image"
      class="w-full h-64 object-cover mb-2"
    />
    <p class="text-gray-700">{{ recipe.description }}</p>
    <ul class="list-disc pl-5">
      <li>Калории: {{ recipe.calories }}</li>
      <li>Белки: {{ recipe.proteins }}</li>
      <li>Жиры: {{ recipe.fats }}</li>
      <li>Углеводы: {{ recipe.carbs }}</li>
      <li>Время: {{ recipe.hours }} ч {{ recipe.minutes }} мин</li>
      <li>Острота: {{ recipe.spiciness }}</li>
      <li>Сложность: {{ recipe.difficulty }}</li>
    </ul>
  </div>
</template>
