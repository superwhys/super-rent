<template>
  <div>
    <el-menu
        class="el-menu-vertical-demo"
        default-active="Management"
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
        <el-menu-item index="Management">
          <span slot="title">管理大厅</span>
        </el-menu-item>
      </el-submenu>
      <el-submenu index="rentCenter">
        <template slot="title">
          <i class="el-icon-office-building"></i>
          <span slot="title">出租单位中心</span>
        </template>
        <el-menu-item index="house">
          <span slot="title">楼栋管理</span>
        </el-menu-item>
        <el-menu-item index="apartment">
          <span slot="title">公寓管理</span>
        </el-menu-item>
        <el-menu-item index="store">
          <span slot="title">店铺管理</span>
        </el-menu-item>
        <el-menu-item index="other">
          <span slot="title">其他管理</span>
        </el-menu-item>
      </el-submenu>
      <el-menu-item index="about">
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
      router: true
    }
  },
  methods: {
    // serviceCenter 禁止关闭
    handleClose(index, indexPath) {
      if(index === 'serivceCenter'){
        this.$refs.menu.open(indexPath)
      }
    }
  }
}
</script>

<style scoped>
  .el-menu-vertical-demo {
    width: 213px;
    min-height: calc(100vh);
    border: none;
  }

</style>