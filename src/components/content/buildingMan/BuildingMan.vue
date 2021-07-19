<template>
  <div class="build-man">
    <main-head class="head"></main-head>
    <main-table></main-table>
  </div>
</template>

<script>
import MainHead from "components/common/mainhead/MainHead";
import MainTable from "components/common/mainTable/MainTable";

export default {
  name: "BuildingMan",
  components: {
    MainHead,
    MainTable
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
    margin: 10px 10px 0 20px;
  }
</style>