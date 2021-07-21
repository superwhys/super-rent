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
  .table {
    width: 790px;
    height: 693px;
    float: left;
    background-color: #fff;
  }

  .plot {
    background-color: gold;
    width: 348px;
    height: 472px;
    float: left;
    margin-left: 10px;
  }
</style>