import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import {Container, Header, Aside, Main, Footer,
        Button, Input, Checkbox, Menu,
        MenuItemGroup, MenuItem, Row, Col,
        Submenu, Select, Option, Dropdown,
        DropdownMenu, DropdownItem, Table, TableColumn,
        Pagination} from "element-ui";

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
Vue.use(Select)
Vue.use(Option)
Vue.use(Dropdown)
Vue.use(DropdownItem)
Vue.use(DropdownMenu)
Vue.use(Table)
Vue.use(TableColumn)
Vue.use(Pagination)

Vue.prototype.$bus = new Vue()

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
