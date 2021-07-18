<template>
  <div class="build-man">
    <main-head class="head"></main-head>
  </div>
</template>

<script>
import MainHead from "components/common/mainhead/MainHead";

export default {
  name: "BuildingMan",
  components: {
    MainHead
  }
}
</script>

<style scoped>
  .build-man {
    width: 790px;
    height: 693px;
    overflow: hidden;
    background-color: #fff;
  }

  .head {
    margin: 15px 10px 0 10px;
  }
</style>