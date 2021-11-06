<template>
  <div class="manageMain">
    <div class="manageTop">
      <div class="searchBar">
        <span class="pageName">出租单位列表</span>
        <div class="searchInput">
          <el-input placeholder="请输入内容" size="medium" v-model="inputSearchText" @blur="inputBlur">
            <el-button slot="append" icon="el-icon-search" size="small" @click="inputSearchClick"></el-button>
          </el-input>
        </div>
      </div>
      <div class="addLine">
        <span>+ 添加</span>
      </div>
    </div>
    <div class="manageTable">
      <manage-table></manage-table>
    </div>
  </div>
</template>

<script>
import ManageTable from "components/common/mainTable/ManageTable";

export default {
  name: "BaseManageMain",
  components: {
    ManageTable
  },
  data() {
    return {
      inputSearchText: "",
    }
  },
  methods: {
    inputSearchClick() {
      this.$bus.$emit('inputSearchClick', {'searchText': this.inputSearchText})
    },
    inputBlur() {
      this.inputSearchClick()
    }
  }
}
</script>

<style scoped>
  .manageMain {
    width: 100%;
    height: 100%;
    background-color: #fff;
    border-radius: 10px;
  }

  .manageTop {
    width: 100%;
    height: 100px;
  }

  .searchBar {
    width: 100%;
    height: 60px;
    line-height: 60px;
  }
  .pageName {
    font-size: 16px;
    font-weight: bold;
    margin-left: 30px;
   }
  .searchInput {
    float: right;
    display: inline-block;
    margin-right: 30px;
  }

  .addLine {
    width: 100%;
    height: 40px;
    text-align: center;
    /*background-color: red;*/
  }
  .addLine span {
    display: block;
    height: 40px;
    width: calc(100% - 40px);
    margin: 0 auto;
    line-height: 40px;
    border: 1px dashed #D9D9D9;
    border-radius: 10px;
    font-size: 14px;
  }

  .addLine span:hover {
    color: white;
    border: 0;
    cursor: pointer;
    background-color: #819CF4;
  }

  .manageTable {
    width: 100%;
    height: calc(100% - 100px);
  }



</style>