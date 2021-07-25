<template>
  <div class="apart-main">
    <base-main>
      <div slot="table">
        <main-head class="head"></main-head>
        <apartment-table></apartment-table>
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
import ApartmentTable from "components/common/mainTable/ApartmentTable";

export default {
  name: "ApartmentMain",
  components: {
    BaseMain,
    MainHead,
    ApartmentTable
  }
}
</script>

<style scoped>
  .apart-main {
    /*width: 790px;*/
    height: 693px;
    overflow: hidden;
  }

  .head {
    margin: 10px 10px 0 20px;
  }

</style>