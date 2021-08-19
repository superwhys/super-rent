<template>
  <div class="head">
    <div class="breadcrumb">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>活动管理</el-breadcrumb-item>
        <el-breadcrumb-item>活动列表</el-breadcrumb-item>
        <el-breadcrumb-item>活动详情</el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div class="user">
      <div class="icon">
        <a><i class="el-icon-search"></i></a>
        <a><i class="el-icon-bell"></i></a>
        <div class="user-name">
          <a><i class="el-icon-user"></i></a>
          <span>用户名</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PageHead"
}
</script>

<style scoped>
  .breadcrumb{
    display: inline-block;
    float: left;
    width: 300px;
    height: 40px;
    margin-top: 15px;
  }

  .user {
    height: 40px;
    display: inline-block;
    float: right;
  }

  .head {
    height: 40px;
    border-bottom: 1px solid #F0F0F0
  }

  .icon {
    line-height: 45px;
    float: right;
    margin-right: 10px;
  }

  .icon i {
    font-size: 17px;
    margin: 0 12px 0 0;
  }

  .icon i:hover {
    cursor: pointer;
  }

  .user-name {
    display: inline-block;
  }
</style>