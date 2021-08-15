<template>
  <base-main class="base-main">
    <div slot="table">
      <main-head class="head"></main-head>
      <house-table class="house-table"></house-table>
    </div>
    <div slot="plot">
      <span>plot</span>
    </div>
  </base-main>
</template>

<script>
import BaseMain from "components/content/basemain/BaseMain";
import MainHead from "components/common/mainhead/MainHead";
import HouseTable from "components/common/mainTable/HouseTable";

export default {
  name: "BuildingMan",
  components: {
    BaseMain,
    MainHead,
    HouseTable
  }
}
</script>

<style scoped>
  .base-main {
    height: 100%;
    overflow: hidden;
  }

  .head {
    margin: 0px 10px 0 20px;
    width: 770px;
    height: 110px;
    line-height: 55px;
  }

  .house-table {
    height: calc(100% - 110px);
  }
</style>