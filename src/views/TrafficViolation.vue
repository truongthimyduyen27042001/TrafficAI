<template>
  <div class="traffic-violation">
      <h1>This is traffic violation</h1>
      <button @click="downloadFile">Click me</button>
        <b-button  @click="downloadFile" variant="outline-primary">Download</b-button>

  </div>
</template>

<script>
export default {
    name: 'violation',
    methods: {
      downloadFile() {
        console.log('2@@@@')
      }
    }
}
</script>

<style lang="scss" scoped>
.traffic-violation {
  width: 100vw;
  height: 100vh;
  background: green;
}

</style>