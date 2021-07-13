<template>
  <div id="login">
    <div class="left">
      <div class="title"><span>房屋租金管理平台</span></div>
      <div class="short-text">
        <span>一个简单易用的管理平台</span>
        <br>
        <span>——Design by SuperYong</span>
      </div>
      <div>
        <img src="~assets/img/login/computer.png" alt="" class="computer">
      </div>
    </div>
    <div class="right">
      <div class="welcome"><span>欢迎登录</span></div>

    </div>
  </div>
</template>

<script>
export default {
  name: "Login"
}
</script>

<style scoped>
  #login {
    width: 765px;
    height: 360px;
    margin: 100px auto;
  }

  .left {
    background-color: rgba(58, 98, 215, 100);
    width: 45%;
    height: 100%;
    opacity: 0.9;
    color: #fff;
  }
  .title{
    font-size: 25px;
    text-align: center;
    margin-top: 70px;
    padding-bottom: 10px;
  }
  .short-text {
    font-size: 12px;
    margin: 0 auto;
    margin-left: 50px;
  }
  .short-text span {
    display: inline-block;
    margin-top: 10px;
  }
  .computer {
    display: block;
    width: 270px;
    height: 200px;
    margin: 0 auto;
  }


  .right {
    width: 55%;
    height: 100%;
    background-color: #fff;
  }
  .welcome {
    margin-top: 70px;
    text-align: center;
  }

  .welcome span{
    /*display: block;*/
    font-size: 20px;
    border-bottom: 2px solid #3A62D7;
    font-weight: bold;
  }





</style>