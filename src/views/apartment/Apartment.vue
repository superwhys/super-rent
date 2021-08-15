<template>
  <div class="apartment-main">
    <apartment-main></apartment-main>
  </div>
</template>

<script>
import ApartmentMain from "components/content/webmain/ApartmentMain";

export default {
  name: "Apartment",
  components: {
    ApartmentMain
  }
}
</script>

<style scoped>
  .apartment-main {
    height: 100%;
  }
</style>