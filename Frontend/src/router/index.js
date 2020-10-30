import Vue from 'vue'
import VueRouter from 'vue-router'
import DashBoard from '../views/DashBoard.vue'
import Home from '../views/Home.vue'
// user
import SignupForm from '../views/user/SignupForm.vue'
import ChatRoom from '@/views/ChatRoom.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/dashboard',
    name: 'DashBoard',
    component: DashBoard
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/board/:code',
    name: 'board',
    component: () => import(/* webpackChunkName: "about" */ '../views/Space.vue')
  },
  {
    path: '/boardlist',
    name: 'BoardList',
    component: () => import('../components/RoomList.vue')
  },
  {
    path: '/login',
    name: 'SignupForm',
    component: SignupForm
  },
  {
    path: '/chat-room/:username',
    name : 'ChatRoom',
    component: ChatRoom,
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
