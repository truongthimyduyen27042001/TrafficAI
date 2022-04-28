<template>
  <div class="default">
    <Navbar />
    <main class="main">
        <slot/>
    </main>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
export default {
  components: { Navbar },

}
</script>

<style lang="scss" scoped>
</style>