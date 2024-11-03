import RecipesList from '@/views/RecipesList.vue'
import RecipesPage from '@/views/RecipesPage.vue'
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'RecipesList',
    component: RecipesList,
  },
  {
    path: '/recipes/:id',
    name: 'RecipesPage',
    component: RecipesPage,
    props: true,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
