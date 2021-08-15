<template>
  <el-container>
    <el-aside width="213px" class="aside">
      <side-bar></side-bar>
    </el-aside>
    <el-container>
      <el-header height="160px" class="header">
        <page-head></page-head>
      </el-header>
      <el-main class="main">
        <!-- router -->
        <slot></slot>
      </el-main>
      <el-footer height="60px" class="footer">Footer</el-footer>
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
  .aside {
    background-color: #002140;
  }

  .header {
    background-color: black;
  }

  .main {
    padding: 10px;
    height: calc(100% - 320px);
  }

  .footer {
    background-color: green;
  }
</style>