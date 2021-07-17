<template>
  <div id="app" class="App">
<!--    <login></login>-->
    <frame></frame>
  </div>
</template>

<script>
  // import Login from "components/common/login/Login";
  import Frame from "components/content/frame/Frame";

  export default {
    name:'App',
    components: {
      // Login
      Frame
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
