<script setup>
import { defineProps } from 'vue'

const props = defineProps({
  steps: {
    type: Array,
    required: true,
  },
})
</script>

<template>
  <div class="mb-4">
    <h2 class="text-xl font-semibold">Шаги</h2>
    <div v-for="step in steps" :key="step.step_number" class="mb-4">
      <h3 class="text-lg">Шаг {{ step.step_number }}</h3>
      <img
        :src="step.image"
        alt="Step Image"
        class="w-full h-32 object-cover mb-2"
      />
      <p>{{ step.instruction }}</p>
    </div>
  </div>
</template>
