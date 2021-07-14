import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import {Button, Input, Checkbox} from "element-ui";

Vue.config.productionTip = false

Vue.use(Button)
Vue.use(Input)
Vue.use(Checkbox)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
