import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import {Container, Header, Aside, Main, Footer,
        Button, Input, Checkbox, Menu,
        MenuItemGroup, MenuItem, Row, Col,
        Submenu} from "element-ui";

Vue.config.productionTip = false

Vue.use(Container)
Vue.use(Header)
Vue.use(Aside)
Vue.use(Main)
Vue.use(Footer)
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
