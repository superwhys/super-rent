<template>
  <div>
    <el-table :fit="true"
              :data='showDatas'
              tooltip-effect="dark"
              style="margin: 10px auto 0"
              :stripe=stripeBool
              @selection-change="handleSelectionChange">
      <el-table-column
          type="selection"
          width="55"
          align="center">
      </el-table-column>
      <el-table-column prop="homeNum" label="房间号" width="65" align="center"></el-table-column>
      <el-table-column prop="status" label="状态" align="center"></el-table-column>
      <el-table-column prop="personName" label="租客姓名" align="center"></el-table-column>
      <el-table-column prop="houseType" label="房间类型" align="center"></el-table-column>
      <el-table-column prop="price" label="租金" align="center"></el-table-column>
      <el-table-column prop="rentDate" label="租房时间" align="center"></el-table-column>
      <el-table-column prop="rentTotalMonth" label="出租月数" align="center"></el-table-column>
      <el-table-column
          label="操作"
          width="150"
          align="center">
        <template slot-scope="scope">
          <el-button @click="handleClick(scope.row)" type="text" size="small">查看</el-button>
          <el-button type="text" size="small">编辑</el-button>
          <el-button type="text" size="small">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "BaseTable",
  props: {
    showDatas: Array,
  },
  data() {
    return {
      stripeBool: true,
      multipleSelection: [],
    }
  },
  methods: {
    handleSelectionChange(val) {
      this.multipleSelection = val;
      this.$emit('choseNum', this.multipleSelection.length)
    },
  },
  created() {
    const windowHeight = window.innerHeight;
    const tableHeight = windowHeight - 505;
    const pageSize = Math.floor(tableHeight / 57)
    this.$bus.$emit('pageSizeCount', pageSize)
    this.$emit('pageSizeCount', pageSize)
    // console.log(pageSize)
  }
}
</script>

<style scoped>

</style>