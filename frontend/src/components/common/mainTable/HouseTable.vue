<template>
  <div>
    <div class="total">
      <div class="inner-text">
        <i class="el-icon-warning"></i>
        <span>已选择  <i class="choseNum">{{ choseNum }}</i>项</span>
        <span>租客总计: <i>{{ chosePeopleNum }}</i>人</span>
      </div>
    </div>
    <div class="table">
      <base-table :show-datas="showDatas"
                  @choseNum="choseNumChange">
      </base-table>
    </div>
    <div class="pagination">
      <el-pagination
          background
          :hide-on-single-page='hideSingle'
          layout="prev, pager, next"
          :page-size='pageSize'
          :total='total'
          :pager-count='pageCount'
          :current-page="currentPage"
          @current-change='currentChange'
          style="float: right">
      </el-pagination>
    </div>
  </div>
</template>

<script>
import BaseTable from "./BaseTable";

export default {
  name: "HouseTable",
  components: {
    BaseTable
  },
  data() {
    return {
      choseNum: 0,
      chosePeopleNum: 0,
      stripeBool: true,
      pageCount: 5,
      pageSize: 7,
      currentPage: 1,
      total: 0,
      hideSingle: true,
      tableDatas: [
        {
          homeNum: 201,
          status: '已出租',
          personName: '张一山',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        },
        {
          homeNum: 202,
          status: '未出租',
          personName: '张三三',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        },
        {
          homeNum: 203,
          status: '未出租',
          personName: '张三三',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        },
        {
          homeNum: 204,
          status: '未出租',
          personName: '张三三',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        },
        {
          homeNum: 205,
          status: '未出租',
          personName: '张三三',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        },
        {
          homeNum: 207,
          status: '未出租',
          personName: '张三三',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        },
        {
          homeNum: 207,
          status: '未出租',
          personName: '张三三',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        },
        {
          homeNum: 301,
          status: '已出租',
          personName: '张三三',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        },
        {
          homeNum: 302,
          status: '未出租',
          personName: '张三三',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        },
        {
          homeNum: 303,
          status: '未出租',
          personName: '张三三',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        },
        {
          homeNum: 304,
          status: '未出租',
          personName: '张三三',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        },
        {
          homeNum: 305,
          status: '未出租',
          personName: '张三三',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        },
        {
          homeNum: 307,
          status: '未出租',
          personName: '张三三',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        },
        {
          homeNum: 307,
          status: '未出租',
          personName: '张三三',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        },
        {
          homeNum: 401,
          status: '已出租',
          personName: '张三三',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        },
        {
          homeNum: 402,
          status: '未出租',
          personName: '张三三',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        },
        {
          homeNum: 403,
          status: '未出租',
          personName: '张三三',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        },
        {
          homeNum: 404,
          status: '未出租',
          personName: '张三三',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        },
        {
          homeNum: 405,
          status: '未出租',
          personName: '张三三',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        },
        {
          homeNum: 407,
          status: '未出租',
          personName: '张三三',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        },
        {
          homeNum: 407,
          status: '未出租',
          personName: '张三三',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        },
        {
          homeNum: 501,
          status: '未出租',
          personName: '张三三',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        },
        {
          homeNum: 502,
          status: '未出租',
          personName: '杨浩文',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        }

      ],
      showDatas: [],
      flagData: [],
      multipleSelection: []
    }
  },
  mounted() {
    // search
    this.$bus.$on('searchClick', (searchItem) => {
      console.log(searchItem)
      let filterNameData = []
      let filterHouseNumData = []

      if (searchItem.name !== "") {
        filterNameData = this.tableDatas.filter(data =>
         data.personName.includes(searchItem.name));
      } else {
        filterNameData = this.tableDatas
      }
      console.log(filterNameData);
      if (searchItem.houseNum !== "") {
        filterHouseNumData = filterNameData.filter(data =>
          data.homeNum === parseInt(searchItem.houseNum))
      } else {
        filterHouseNumData = filterNameData
      }
      console.log(filterHouseNumData);
      if (searchItem.choseStatus !== "请选择") {
        this.flagData = filterHouseNumData.filter(data =>
          data.status === searchItem.choseStatus)
      } else {
        this.flagData = filterHouseNumData
      }

      this.total = this.flagData.length
      this.showDatas = this.flagData.length > this.pageSize ? this.flagData.slice(0, this.pageSize) : this.flagData
      this.currentPage = 1
    })
  },
  methods: {
    currentChange(page) {
      if (this.flagData.length === 0) {
        this.flagData = this.tableDatas
      }
      this.currentPage = page
      this.showDatas = this.flagData.slice(this.pageSize * (page - 1), this.pageSize * page)
    },
    choseNumChange(item) {
      this.choseNum = item
    }
  },
  created() {
    let that = this
    that.$bus.$on('pageSizeCount', (page) => {
      that.pageSize = page
      this.total = this.tableDatas.length
      this.showDatas = this.tableDatas.slice(0, this.pageSize)
      console.log("page size: %d", that.pageSize)
    })
  }
}
</script>

<style scoped>
.total {
  width: calc(100% - 10px);
  height: 39px;
  background-color: #E6F7FF;
  border: 1px solid #BAE7FF;
  border-radius: 5px;
  margin: 5px auto 0;
}

.inner-text {
  line-height: 39px;
  margin-left: 10px;
  overflow: hidden;
}

.choseNum {
  color: #1890FF;
}

.total i {
  font-style: normal;
  margin-right: 5px;
  margin-left: 2px;
}

.total span {
  margin-right: 20px;
}

.table {
  width: 100%;
  height: 100%;
}

.pagination {
  width: 100%;
  height: 45px;
  margin-right: 20px;
  margin-top: 20px;
}
</style>