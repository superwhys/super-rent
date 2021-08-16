<template>
  <div>
    <div class="up">
      <span class="name">租客姓名 : </span>
      <el-input size="small" style="width: 115px" placeholder="请输入" v-model="nameInput"></el-input>
      <span class="houseNum">房间(公寓)号 : </span>
      <el-input size="small" style="width: 80px" placeholder="请输入" v-model="houseNumInput"></el-input>
      <span class="status">状态 : </span>
      <el-select v-model="choseStatus" placeholder="请选择" size="small" class="status-chose">
        <el-option v-for="item in options"
                   :key="item.value" :label="item.label"
                   :value="item.value"></el-option>
      </el-select>
      <el-button type="primary" size="small" class="search" @click="searchClick">查询</el-button>
      <el-button size="small" @click="resetClick">重置</el-button>
    </div>
    <div class="down">
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
      houseNumInput: '',
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
  destroyed() {
    this.$bus.$off('searchClick')
  },
  methods: {
    handleCommand(command) {
      // TODO
      console.log('click on item ' + command);
    },
    createClick() {
      // TODO
      console.log('create');
    },
    searchClick() {
      this.$bus.$emit('searchClick', {'name': this.nameInput, 'houseNum': this.houseNumInput})
    },
    resetClick() {
      this.nameInput = ""
      this.houseNumInput = ""
      this.$bus.$emit('resetClick')
      this.$bus.$emit('searchClick', {'name': "", 'houseNum': ""})
    }
  }
}
</script>

<style scoped>

  .status, .houseNum{
    margin-left: 20px;
  }

  .status-chose {
    width: 150px;
  }

  .search {
    margin-left: 20px;
  }

  .up {
    height: 60px;
    padding-top: 10px;
  }

  .down {
    height: 50px;
  }

  .batchOperation {
    margin-left: 10px;
  }
</style>