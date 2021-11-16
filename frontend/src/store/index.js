import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: "",
    token: ""
  },
  mutations: {
    addToken(state, data) {
      state.token = data.token
      state.user = data.username
    }
  },
  actions: {
  },
  modules: {
  }
})
