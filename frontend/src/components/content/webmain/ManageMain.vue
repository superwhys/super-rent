<template>
  <div class="manage">
    <base-manage-main>
    </base-manage-main>
  </div>

</template>

<script>
import BaseManageMain from "components/content/basemain/BaseManageMain";

export default {
  name: "ManageMain",
  components: {
    BaseManageMain
  }
}
</script>

<style scoped>
  .manage {
    width: 100%;
    height: 100%;
  }
</style>