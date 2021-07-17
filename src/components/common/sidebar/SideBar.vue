<template>
  <div>
    <el-menu
        class="el-menu-vertical-demo"
        default-active="1-1"
        background-color="#002140"
        text-color="#fff"
        active-text-color="#ffd04b">
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-odometer"></i>
          <span>服务中心</span>
        </template>
        <el-menu-item index="1-1">
          <span slot="title">管理大厅</span>
        </el-menu-item>
      </el-submenu>
      <el-submenu index="2">
        <template slot="title">
          <i class="el-icon-office-building"></i>
          <span slot="title">出租单位中心</span>
        </template>
        <el-menu-item index="2-1">
          <span slot="title">楼栋管理</span>
        </el-menu-item>
        <el-menu-item index="2-2">
          <span slot="title">公寓管理</span>
        </el-menu-item>
        <el-menu-item index="2-3">
          <span slot="title">店铺管理</span>
        </el-menu-item>
        <el-menu-item index="2-4">
          <span slot="title">其他管理</span>
        </el-menu-item>
      </el-submenu>
      <el-menu-item index="3">
        <i class="el-icon-setting"></i>
        <span slot="title">关于</span>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: "SideBar",
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    }
  }
}
</script>

<style scoped>
  .el-menu-vertical-demo {
    width: 213px;
    min-height: calc(100vh)
  }

</style>