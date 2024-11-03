<script setup>
import { defineProps } from 'vue'

const props = defineProps({
  comment: Object,
})
</script>

<template>
  <div class="border p-4 mb-2 rounded">
    <p class="text-sm text-gray-600">
      {{ new Date(comment.created_at).toLocaleString() }}
    </p>
    <p class="font-semibold">{{ comment.content }}</p>
  </div>
</template>
