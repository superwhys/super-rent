<template>
  <div class="manageTablePart">
    <div class="tableMain">
      <el-table :fit="true"
                :data='showData'
                tooltip-effect="dark"
                style="margin: 10px auto 0"
                :stripe=true>
        <el-table-column
            type="index"
            align="center"
            fixed>
        </el-table-column>
        <el-table-column prop="name" label="出租单位地址" align="center" min-width="100" :show-overflow-tooltip="showOverflow" fixed></el-table-column>
        <el-table-column prop="owner" label="拥有者" align="center"></el-table-column>
        <el-table-column prop="unitType" label="出租单位类型" align="center"></el-table-column>
        <el-table-column prop="startTime" label="开始时间" width="155" align="center"></el-table-column>
        <el-table-column prop="roomNum" label="数量" align="center"></el-table-column>
        <el-table-column prop="thisMonthRentPrice" label="本月已收金额" align="center"></el-table-column>
        <el-table-column
            fixed="right"
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
    <div class="pagination">
      <el-pagination
          background
          hide-on-single-page
          layout="prev, pager, next"
          :total='totalPage'
          :page-size="pageSize"
          :pager-count='pageCount'
          :current-page="currentPage"
          @current-change='currentChange'
          style="float: right;">
      </el-pagination>
    </div>
  </div>
</template>

<script>
export default {
  name: "ManageTable",
  data() {
    return {
      showOverflow: true,
      totalPage: 1,
      pageSize: 1,
      pageCount: 5,
      currentPage: 1,
      unitRentTotal: [
        {
          name: "111广东省广州市xxx区xxx街道xxx社区xxx栋",
          owner: '张有一', unitType: '楼栋', startTime: '2017-10-31 23:12:00',
          roomNum: 30, thisMonthRentPrice: '24567元'
        },
        {
          name: "222广东省广州市xxx区xxx街道xxx社区xxx栋有",
          owner: '张三三', unitType: '楼栋', startTime: '2017-10-31 23:12:00',
          roomNum: 30, thisMonthRentPrice: '24567元'
        },
        {
          name: "333广东省广州市xxx区xxx街道xxx社区xxx栋",
          owner: '张三三', unitType: '楼栋', startTime: '2017-10-31 23:12:00',
          roomNum: 30, thisMonthRentPrice: '24567元'
        },
        {
          name: "444广东省广州市xxx区xxx街道xxx社区xxx栋",
          owner: '张三三', unitType: '楼栋', startTime: '2017-10-31 23:12:00',
          roomNum: 30, thisMonthRentPrice: '24567元'
        },
        {
          name: "555广东省广州市xxx区xxx街道xxx社区xxx栋",
          owner: '张三三', unitType: '楼栋', startTime: '2017-10-31 23:12:00',
          roomNum: 30, thisMonthRentPrice: '24567元'
        },
        {
          name: "666广东省广州市xxx区xxx街道xxx社区xxx栋",
          owner: '张三三', unitType: '楼栋', startTime: '2017-10-31 23:12:00',
          roomNum: 30, thisMonthRentPrice: '24567元'
        },
        {
          name: "777广东省广州市xxx区xxx街道xxx社区xxx栋",
          owner: '张三三', unitType: '楼栋', startTime: '2017-10-31 23:12:00',
          roomNum: 30, thisMonthRentPrice: '24567元'
        },
        {
          name: "888广东省广州市xxx区xxx街道xxx社区xxx栋",
          owner: '张三三', unitType: '楼栋', startTime: '2017-10-31 23:12:00',
          roomNum: 30, thisMonthRentPrice: '24567元'
        },
        {
          name: "999广东省广州市xxx区xxx街道xxx社区xxx栋",
          owner: '张三三', unitType: '楼栋', startTime: '2017-10-31 23:12:00',
          roomNum: 30, thisMonthRentPrice: '24567元'
        },
        {
          name: "1010广东省广州市xxx区xxx街道xxx社区xxx栋",
          owner: '张三三', unitType: '楼栋', startTime: '2017-10-31 23:12:00',
          roomNum: 30, thisMonthRentPrice: '24567元'
        },
        {
          name: "1111广东省广州市xxx区xxx街道xxx社区xxx栋",
          owner: '张三三', unitType: '楼栋', startTime: '2017-10-31 23:12:00',
          roomNum: 30, thisMonthRentPrice: '24567元'
        },
        {
          name: "1212广东省广州市xxx区xxx街道xxx社区xxx栋",
          owner: '张三三', unitType: '楼栋', startTime: '2017-10-31 23:12:00',
          roomNum: 30, thisMonthRentPrice: '24567元'
        },
        {
          name: "1313广东省广州市xxx区xxx街道xxx社区xxx栋",
          owner: '张三三', unitType: '楼栋', startTime: '2017-10-31 23:12:00',
          roomNum: 30, thisMonthRentPrice: '24567元'
        },
        {
          name: "1414广东省广州市xxx区xxx街道xxx社区xxx栋",
          owner: '张三三', unitType: '楼栋', startTime: '2017-10-31 23:12:00',
          roomNum: 30, thisMonthRentPrice: '24567元'
        },
      ],
      flagData: [],
      showData: [],
    }
  },
  methods: {
    currentChange(page) {
      if (this.flagData.length === 0) {
        this.flagData = this.unitRentTotal
      }
      this.currentPage = page
      this.showData = this.flagData.slice(this.pageSize * (page - 1), this.pageSize * page)
    },
  },
  created() {
    const windowHeight = window.innerHeight;
    const tableHeight = windowHeight - 470;
    const pageSize = Math.floor(tableHeight / 57)
    this.pageSize = pageSize
    this.totalPage = this.unitRentTotal.length
    this.showData = this.unitRentTotal.slice(0, pageSize)
    console.log("page size: %d", pageSize)
  },
  mounted() {
    this.$bus.$on('inputSearchClick', (inputSearchText) => {
      console.log(inputSearchText);
      let filterData = []
      if(inputSearchText.searchText !== "") {
        filterData = this.unitRentTotal.filter(data =>
            data.name.includes(inputSearchText.searchText))

        filterData = filterData.concat(this.unitRentTotal.filter(data =>
            data.owner.includes(inputSearchText.searchText)))
      } else {
        filterData = this.unitRentTotal
      }

      this.flagData = filterData
      this.totalPage = this.flagData.length
      this.showData = this.flagData.length > this.pageSize ? this.flagData.slice(0, this.pageSize) : this.flagData
      this.currentPage = 1
    })
  }
}
</script>

<style scoped>
  .manageTablePart {
    width: 100%;
    height: 100%;
  }

  .tableMain {
    width: 100%;
    padding: 0 20px;
    height: calc(100% - 60px);
  }

  .pagination {
    width: 100%;
    height: 40px;
    padding-top: 4px;
    padding-right: 5px;
  }

  .itemLi div {
    display: inline-block;
    margin-right: 20px;
  }
</style>