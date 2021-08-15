<template>
  <div class="build-main">
    <building-man></building-man>
  </div>
</template>

<script>
import BuildingMan from "components/content/webmain/BuildingMan";

export default {
  name: "House",
  components: {
    BuildingMan
  }
}
</script>

<style scoped>
  .build-main {
    height: 100%;
  }
</style>