<template>
  <div class="background-img">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "LoginBg"
}
</script>

<style scoped>
  .background-img{
    width: 100%;
    height: 100%;
  }
</style>