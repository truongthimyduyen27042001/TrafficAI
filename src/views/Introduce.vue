<template>
  <div class="introduce">
      <Header />
      <intro-func/>
      <Posts />
  </div>
</template>

<script>
import Header from '@/components/Header.vue'
import IntroFunc from '@/components/IntroFunc.vue'
import Posts from '@/components/Posts.vue'
export default {
  name: 'introduce',
  components: { Header, IntroFunc,Posts },
}
</script>

<style>

</style>