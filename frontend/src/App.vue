<template>
  <div id="app" class="App">
    <frame-web>
        <router-view></router-view>
    </frame-web>
  </div>
</template>

<script>
  // import Login from "components/common/login/Login";
  import FrameWeb from "components/content/frameweb/FrameWeb";

  export default {
    name:'App',
    components: {
      FrameWeb
    }
  }


</script>

<style>
  @import 'assets/css/base.css';
  .App{
    width: 100%;
    height: 100%
  }
</style>
