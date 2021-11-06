import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

const Index = () => import('views/Index')
const Management = () => import('views/management/Management')
const House = () => import('views/house/House')
const Apartment = () => import('views/apartment/Apartment')
const Store = () => import('views/store/Store')
const Others = () => import('views/other/Other')
const Login = () => import('components/common/login/Login')

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    component: Login
  },
  {
    path: '/rent',
    component: Index,
    children: [
      {
        path: '',
        redirect: 'management'
      },
      {
        path: 'management',
        component: Management
      },
      {
        path: 'house',
        component: House
      },
      {
        path: 'apartment',
        component: Apartment
      },
      {
        path: 'store',
        component: Store
      },
      {
        path: 'other',
        component: Others
      }
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
