<template>
  <div>
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
  .user {
    width: 100%;
    height: 40px;
    /* background-color: green; */
  }

  .user {
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