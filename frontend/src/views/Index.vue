<template>
  <frame-web>
    <router-view></router-view>
  </frame-web>
</template>

<script>
import FrameWeb from "components/content/frameweb/FrameWeb";

export default {
  name: "Index",
  components: {
    FrameWeb
  }
}
</script>

<style scoped>

</style>