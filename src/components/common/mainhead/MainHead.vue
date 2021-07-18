<template>
  <div class="main-head">
    <div>
      <span class="name">租客姓名 : </span>
      <el-input size="small" style="width: 115px" placeholder="请输入" v-model="nameInput"></el-input>
      <span class="status">状态 : </span>
      <el-select v-model="choseStatus" placeholder="请选择" size="small">
        <el-option v-for="item in options"
                   :key="item.value" :label="item.label"
                   :value="item.value"></el-option>
      </el-select>
      <el-button type="primary" size="small" class="search">查询</el-button>
      <el-button size="small">重置</el-button>
    </div>
    <div class="operation">
      <el-button icon="el-icon-plus" type="primary" size="small" @click="createClick">新建</el-button>
      <el-dropdown @command="handleCommand" trigger="click" class="batchOperation">
        <el-button size="small">批量操作</el-button>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="delect">删除</el-dropdown-item>
          <el-dropdown-item command="change">修改</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
  </div>
</template>

<script>
export default {
  name: "MainHead",
  data() {
    return {
      nameInput: '',
      choseStatus: '请选择',
      options: [{
        value: 'rent',
        label: '已出租'
      },{
        value: 'norent',
        label: '未出租'
      }]
    }
  },
  methods: {
    handleCommand(command) {
      // TODO
      console.log('click on item ' + command);
    },
    createClick() {
      // TODO
      console.log('create');
    }
  }
}
</script>

<style scoped>
  .main-head {
    width: 770px;
    height: 110px;
    line-height: 55px;
  }

  .name{

  }
  .status {
    margin-left: 20px;
  }

  .search {
    margin-left: 20px;
  }

  .batchOperation {
    margin-left: 10px;
  }
</style>