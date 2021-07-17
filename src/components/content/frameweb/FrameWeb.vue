<template>

  <el-container>
    <el-aside width="213px">
      <side-bar></side-bar>
    </el-aside>
    <el-container>
      <el-header class="header">
        <page-head></page-head>
      </el-header>
      <el-main class="main">Main</el-main>
      <el-footer class="footer">Footer</el-footer>
    </el-container>
  </el-container>
</template>

<script>
import SideBar from "components/common/sidebar/SideBar";
import PageHead from "components/common/pageheader/PageHead";

export default {
  name: "FrameWeb",
  components: {
    SideBar,
    PageHead
  }
}
</script>

<style scoped>
  .header {
    background-color: black;
  }
  .main {
    background-color: gold;
  }

  .footer {
    background-color: green;
  }
</style>