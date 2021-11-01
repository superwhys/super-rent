<template>
  <div class="man-head-box">
    <div class="user-icon-box">
      <el-avatar :size="60" icon="el-icon-user-solid"></el-avatar>
    </div>
    <div class="total-info">
      <div class="total-box">
        <span>出租单位总数</span>
        <span class="total-count">8</span>
      </div>
      <div class="total-box">
        <span>楼栋数</span>
        <span class="house-count">7</span>
      </div>
      <div class="total-box">
        <span>公寓数</span>
        <span class="apartment-count">6</span>
      </div>
      <div class="total-box">
        <span>店铺数</span>
        <span class="store-count">5</span>
      </div>
      <div class="total-box">
        <span>其他类型数</span>
        <span class="other-count">4</span>
      </div>
      <div class="total-box">
        <span>当月收取金额总数</span>
        <span class="total-price">3</span>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: "ManageHead"
}
</script>

<style scoped>

  .man-head-box{
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    display: flex;
    /*overflow: hidden;*/
    flex-wrap: nowrap;
    flex-direction: row;
  }

  .user-icon-box {
    width: 15%;
    height: 100%;
    flex: 15%;
    line-height: 120px;
    padding-top: 24px;
    padding-left: 100px;
  }

  .total-info{
    width: 80%;
    height: 100%;
    flex: 80%;
    padding-top: 30px;
    padding-left: 10px;
  }
  .total-box{
    width: 16%;
    height: 60%;
    float: left;
    /*padding: 0px 0px;*/
  }
  .total-box span{
    text-align: center;
    display: block;
  }
  .total-box span:first-child {
    padding-top: 5px;
    font-size: 14px;
    color: #87888A;
  }
  .total-box span:nth-child(2) {
    text-align: center;
    padding-top: 10px;
    font-size: 20px;
    font-weight: bold;
  }
  .total-box:first-child {
    width: 130px;
    border-right: 1px solid #E9E9E9;
  }
  .total-box:last-child {
    width: 160px;
    border-left: 1px solid #E9E9E9;
  }
</style>