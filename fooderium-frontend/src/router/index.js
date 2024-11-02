import Vue from 'vue';
import Router from 'vue-router';
import Recipes from '../views/TheRecipes.vue';
import RecipeDetail from '../views/RecipeDetail.vue';

Vue.use(Router);

const routes = [
  { path: '/recipes', component: Recipes },
  { path: '/recipe/:id', component: RecipeDetail, props: true },
];

export default new Router({
  mode: 'history',
  routes,
});
