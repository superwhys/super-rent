<template>
  <div class="build-man">
    <base-main>
      <div slot="table">
        <main-head class="head"></main-head>
        <main-table></main-table>
      </div>
      <div slot="plot">
        <span>plot</span>
      </div>
    </base-main>
  </div>
</template>

<script>
import BaseMain from "components/content/basemain/BaseMain";
import MainHead from "components/common/mainhead/MainHead";
import MainTable from "components/common/mainTable/MainTable";

export default {
  name: "BuildingMan",
  components: {
    BaseMain,
    MainHead,
    MainTable
  }
}
</script>

<style scoped>
  .build-man {
    /*width: 790px;*/
    height: 693px;
    overflow: hidden;
  }

  .head {
    margin: 10px 10px 0 20px;
  }
</style>