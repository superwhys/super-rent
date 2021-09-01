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
    <!-- TODO:表单提交 -->
    <div class="right">
      <div class="welcome"><span>欢迎登录</span></div>
      <el-input
        placeholder="请输入账号"
        prefix-icon="el-icon-user"
        v-model="username"
        class="username">
      </el-input>
      <el-input
        type="password"
        placeholder="请输入密码"
        prefix-icon="el-icon-lock"
        class="password"
        v-model="password">
      </el-input>
      <div class="status">
        <el-checkbox v-model="checked" class="remenber-password"><span style="font-size: 12px">记住密码</span></el-checkbox>
        <div class="forget"><a href="#">忘记密码</a></div>
      </div>
      <el-button type="primary" class="loginBtn" @click="login">登录</el-button>
    </div>
  </div>
</template>

<script>

export default {
  name: "Login",
  components: {

  },
  data() {
    return {
      username: '',
      password: '',
      checked: false,
    }
  },
  methods: {
    login() {
      console.log(this.username);
      console.log(this.password);
    }
  }
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
    display: flex;
    /* 从上往下排列*/
    flex-direction: column;
    /* 水平居中*/
    align-items: center;
  }
  .welcome {
    margin-top: 70px;
    margin-bottom: 35px;
  }
  .welcome span {
    font-size: 20px;
    border-bottom: 2px solid #3A62D7;
    font-weight: bold;
  }
  .username {
    width: 265px;
  }
  .username input {
    border: none
  }
  .password {
    width: 265px;
  }
  .username ,.password {
    margin-bottom: 5px;
  }
  .remenber-password {
    align-content: flex-start;
    margin-right: 140px;
  }
  .forget {
    display: inline;
    font-size: 12px;
  }
  .forget a:hover {
    color: #409EFF;
  }
  .loginBtn {
    width: 265px;
    margin-top: 10px;
  }




</style>