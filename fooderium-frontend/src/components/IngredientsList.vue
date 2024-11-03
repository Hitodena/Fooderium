<script setup>
import { defineProps } from 'vue'
import RecipeProduct from './RecipeProduct.vue'

const props = defineProps({
  products: {
    type: Array,
    required: true,
  },
})
</script>

<template>
  <div class="mb-4">
    <h2 class="text-xl font-semibold">Ингредиенты</h2>
    <div
      v-for="product in products"
      :key="product.product.id"
      class="flex items-center mb-2"
    >
      <RecipeProduct :product="product.product" :quantity="product.quantity" />
    </div>
  </div>
</template>
