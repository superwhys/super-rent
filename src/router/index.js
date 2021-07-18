import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

const Management = () => import('views/management/Management')
const House = () => import('views/house/House')
const Apartment = () => import('views/apartment/Apartment')
const Store = () => import('views/store/Store')
const Others = () => import('views/other/Other')

const routes = [
  {
    path: '',
    redirect: '/Management'
  },
  {
    path: '/Management',
    component: Management
  },
  {
    path: '/house',
    component: House
  },
  {
    path: '/apartment',
    component: Apartment
  },
  {
    path: '/store',
    component: Store
  },
  {
    path: '/other',
    component: Others
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
