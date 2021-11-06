<template>
  <el-container>
    <!--  侧边导航栏  -->
    <el-aside width="213px" class="aside">
      <side-bar></side-bar>
    </el-aside>
    <el-container>
      <!--   右边顶部   -->
      <el-header height="160px" class="header">
        <page-head>
          <manage-head v-show="nowPath === '/rent/management'"></manage-head>
        </page-head>
      </el-header>
      <!--   右边主体   -->
      <el-main class="main">
        <!-- router -->
        <slot></slot>
      </el-main>
      <!--   右边页脚   -->
      <el-footer height="60px" class="footer">Footer</el-footer>
    </el-container>
  </el-container>
</template>

<script>
import SideBar from "components/common/sidebar/SideBar";
import PageHead from "components/common/pageheader/PageHead";
import ManageHead from "components/common/headtop/ManageHead";

export default {

  name: "FrameWeb",
  components: {
    SideBar,
    PageHead,
    ManageHead
  },
  data() {
    return {
      nowPath: '/rent/management'
    }
  },
  watch: {
    $route(to, from) {
      this.nowPath = to.path
    }
  }
}
</script>

<style scoped>
  .aside {
    background-color: #002140;
  }

  .header {
    background-color: #fff;
    margin: 10px 10px 0 10px;
    border-radius: 10px;
  }

  .main {
    padding: 10px;
    height: calc(100% - 320px);
  }

  .footer {
    background-color: green;
  }
</style>