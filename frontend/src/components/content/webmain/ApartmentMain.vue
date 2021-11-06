<template>
  <base-main class="base-main">
    <div slot="table">
      <main-head class="head"></main-head>
      <apartment-table class="apartment-table"></apartment-table>
    </div>
    <div slot="plot">
      <span>plot</span>
    </div>
  </base-main>
</template>

<script>
import BaseMain from "components/content/basemain/BaseUnitRentMain";
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
.base-main {
  height: 100%;
  overflow: hidden;
}

.head {
  margin: 0 10px 0 20px;
  width: 770px;
  height: 110px;
  line-height: 55px;
}

.apartment-table {
  height: calc(100% - 110px);
}
</style>