<script setup>
import { defineProps } from 'vue'

const props = defineProps({
  product: {
    type: Object,
    required: true,
  },
  quantity: {
    type: Number,
    required: true,
  },
})
</script>

<template>
  <div class="flex items-center gap-2">
    <img
      :src="product.image"
      alt="Product Image"
      class="w-10 h-10 object-cover"
    />
    <span class="font-medium">{{ product.name }} {{ quantity }}г.</span>
  </div>
</template>
