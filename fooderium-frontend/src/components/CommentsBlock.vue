<template>
  <div class="mt-4">
    <h2 class="text-xl font-bold mb-2">Комментарии ({{ comments.length }})</h2>
    <div v-for="comment in comments" :key="comment.id">
      <TheComment :comment="comment" />
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'
import TheComment from './TheComment.vue';

const props = defineProps({
  comments: Array,
})
</script>
