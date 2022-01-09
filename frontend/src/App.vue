<template>
  <div id="app" class="App">
    <router-view></router-view>
  </div>
</template>

<script>

  export default {
    name:'App',
    mounted() {
      const h = document.documentElement.clientHeight;
      console.log(h)
      const ss = document.getElementById('app');
      console.log(ss)
      ss.style.height = h + "px";
    },
    created() {
      if (sessionStorage.getItem('userInfo') !== null) {
        this.$store.commit('EventListener')
      }
    }
  }

</script>

<style>
  @import 'assets/css/base.css';
  .App{
    width: 100%;
  }
</style>
