import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import {Button, Input, Checkbox, Menu,
        MenuItemGroup, MenuItem, Row, Col,
        Submenu} from "element-ui";

Vue.config.productionTip = false

Vue.use(Button)
Vue.use(Input)
Vue.use(Checkbox)
Vue.use(Menu)
Vue.use(MenuItemGroup)
Vue.use(MenuItem)
Vue.use(Row)
Vue.use(Col)
Vue.use(Submenu)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
