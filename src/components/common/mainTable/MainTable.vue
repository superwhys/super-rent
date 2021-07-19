<template>
  <div>
    <div class="total">
      <div class="inner-text">
        <i class="el-icon-warning"></i>
        <span>已选择  <i class="choseNum">{{choseNum}}</i>项</span>
        <span>租客总计: <i>{{chosePeopleNum}}</i>人</span>
      </div>
    </div>
    <div class="table">
      <el-table ref="multipleTable"
                :data='showDatas'
                tooltip-effect="dark"
                style="width: 735px; margin: 10px auto 0"
                :stripe=stripeBool
                @selection-change="handleSelectionChange">
        <el-table-column
            type="selection"
            width="55">
        </el-table-column>
        <el-table-column prop="homeNum" label="房间号" width="65px" align="center"></el-table-column>
        <el-table-column prop="status" label="状态" width="65px" align="center"></el-table-column>
        <el-table-column prop="personName" label="租客姓名" width="80px" align="center"></el-table-column>
        <el-table-column prop="houseType" label="房间类型" width="80px" align="center"></el-table-column>
        <el-table-column prop="price" label="租金" width="74px" align="center"></el-table-column>
        <el-table-column prop="rentDate" label="租房时间" width="85x" align="center"></el-table-column>
        <el-table-column prop="rentTotalMonth" label="出租月数" width="80px" align="center"></el-table-column>
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

      <el-pagination
          background
          :hide-on-single-page='hideSingle'
          layout="prev, pager, next"
          :page-size='pageSize'
          :total='total'
          :pager-count='pageCount'
          :current-page="currentPage"
          @current-change='currentChange'
          class="pagination">
      </el-pagination>
    </div>
  </div>
</template>

<script>
export default {
  name: "MainTable",
  data() {
    return {
      // choseNum: 0,
      chosePeopleNum: 0,
      stripeBool: true,
      pageSize: 7,
      pageCount: 5,
      currentPage: 1,
      total: 0,
      hideSingle: true,
      tableDatas: [
      {
        homeNum: 201,
        status: '已出租',
        personName: '张三三',
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
          personName: '张三三',
          houseType: '一房一厅',
          price: 550,
          rentDate: '2021-7-10',
          rentTotalMonth: '1个月'
        }

      ],
      showDatas:[],
      multipleSelection: []
    }
  },
  methods: {
    handleSelectionChange(val) {
      this.multipleSelection = val;
    },
    currentChange(page) {
      // console.log(page);
      this.currentPage = page
      this.showDatas = this.tableDatas.slice(this.pageSize * (page - 1), this.pageSize * page)

    }
  },
  computed: {
    choseNum() {
      return this.multipleSelection.length
    }
  },
  created() {
    this.total = this.tableDatas.length
    this.showDatas = this.tableDatas.slice(0, 7)
  }
}
</script>

<style scoped>
  .total {
    /*display: flex;*/
    width: 750px;
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

  .pagination {
    float: right;
    margin-right: 20px;
    margin-top: 20px;
  }
</style>