<template>
  <div>
    <div class="info">
      <div class="info-item-table">
        <slot name="table"></slot>
      </div>
    </div>
    <div class="plot">
      <div class="info-item-plot">
        <slot name="plot"></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "BaseMain"
}
</script>

<style scoped>

  .info {
    width: 72%;
    height: 100%;
    float: left;
    background-color: #fff;
    border-radius: 10px;
    margin-right: 10px;
  }

  .info-item-table {
    height: 100%;
  }

  .plot {
    background-color: gold;
    border-radius: 10px;
    width: 27%;
    height: 100%;
    float: left;
  }
</style>