<template>
  <el-row>
    <el-col :span="4">
      <side-bar></side-bar>
    </el-col>
  </el-row>
</template>

<script>
import SideBar from "components/common/sidebar/SideBar";

export default {
  name: "Frame",
  components: {
    SideBar
  }
}
</script>

<style scoped>

</style>