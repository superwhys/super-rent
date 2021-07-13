<template>
  <div id="app" class="App">
    <login></login>
  </div>
</template>

<script>
  import Login from "components/common/login/Login";
  export default {
    name:'App',
    components: {
      Login
    }
  }


</script>

<style>
  @import 'assets/css/base.css';
  .App{
    width: 100%;
    height: 100%;
  }
</style>
