<template>
  <div class="base-main">
    <div class="table">
      <slot name="table"></slot>
    </div>
    <div class="plot">
      <slot name="plot"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "BaseMain"
}
</script>

<style scoped>
  .base-main {
    /*width: 100%;*/
    height: 100%;
  }

  .table {
    width: 69%;
    float: left;
  }
  .plot {
    width: 30%;
    height: 472px;
    background-color: gold;
    float: left;
    margin-left: 10px;
  }

</style>