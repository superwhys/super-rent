<template>
  <div>
    <el-menu
        class="el-menu-vertical-demo"
        :default-active=routePath
        background-color="#002140"
        text-color="#fff"
        active-text-color="#ffd04b"
        :router=router
        ref="menu"
        @close="handleClose">
      <el-submenu index="serivceCenter">
        <template slot="title">
          <i class="el-icon-odometer"></i>
          <span>服务中心</span>
        </template>
        <el-menu-item index="/rent/management">
          <span slot="title">管理大厅</span>
        </el-menu-item>
      </el-submenu>
      <el-submenu index="rentCenter">
        <template slot="title">
          <i class="el-icon-office-building"></i>
          <span slot="title">出租单位中心</span>
        </template>
        <el-menu-item index="/rent/house">
          <span slot="title">楼栋管理</span>
        </el-menu-item>
        <el-menu-item index="/rent/apartment">
          <span slot="title">公寓管理</span>
        </el-menu-item>
        <el-menu-item index="/rent/store">
          <span slot="title">店铺管理</span>
        </el-menu-item>
        <el-menu-item index="/rent/other">
          <span slot="title">其他管理</span>
        </el-menu-item>
      </el-submenu>
      <el-menu-item index="/rent/about">
        <i class="el-icon-setting"></i>
        <span slot="title">关于</span>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: "SideBar",
  data () {
    return {
      router: true,
      routePath: ''
    }
  },
  beforeMount() {
    this.routePath = this.$route.fullPath
  },
  mounted() {
    this.$refs.menu.open(['serivceCenter'])
    this.$refs.menu.open(['rentCenter'])
  },
  methods: {
    // serviceCenter 禁止关闭
    handleClose(index, indexPath) {
      this.$refs.menu.open(indexPath)
    }
  }
}
</script>

<style scoped>
  .el-menu-vertical-demo {
    /*width: 213px;*/
    min-height: calc(100vh);
    border: none;
  }

</style>