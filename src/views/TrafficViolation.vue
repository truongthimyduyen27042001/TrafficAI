<template>
  <div class="traffic-violation">
    <h1>This is traffic violation</h1>
    <div class="embed-responsive embed-responsive-4by3">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/RnLAdC3u2KA?autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
  </div>
</template>

<script>
export default {
  name: "violation",
};
</script>

<style lang="scss" scoped>
.traffic-violation {
  width: 100vw;
  height: 100vh;
  background: green;
}
</style>
