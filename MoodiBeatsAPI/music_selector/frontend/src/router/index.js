import Vue from 'vue'
import Router from 'vue-router'
import listVideo from '@/components/video/listVideo'
import SearchVideo from '@/components/video/SearchVideo'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Inicio',
      component: SearchVideo
    },
    {
      path: '/video',
      name: 'listVideo',
      component: listVideo
    },
    {
      path: '/search',
      name: 'SearchVideo',
      component: SearchVideo
    }
  ],
  mode: 'history'
})