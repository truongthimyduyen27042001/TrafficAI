<template>
  <div class="intro">
      <h3>System Functions</h3>
      <div class="posts">
          <div class="post">
              <div class="image" :style="{backgroundImage: `url('${require('../assets/traffic1.jpg')}')`}"></div>
              <h4>Vehicle Identification</h4>
          </div>
          <div class="post col-2 row-2">
              <div class="image" :style="{backgroundImage: `url('${require('../assets/traffic2.jpg')}')`}"></div>
              <h4>Vehicle Speed Prediction</h4>
          </div>
          <div class="post row-2">
              <div class="image" :style="{backgroundImage: `url('${require('../assets/post-3-image@2x.png')}')`}"></div>
              <h4>Everything wrong with AI</h4>
          </div>
          <div class="post row-2">
              <div class="image" :style="{backgroundImage: `url('${require('../assets/traffic4.jpg')}')`}"></div>
              <h4>Vehicle Classification</h4>
          </div>
          <div class="post">
              <div class="image" :style="{backgroundImage: `url('${require('../assets/post-5-image@2x.png')}')`}"></div>
              <h4>Node Packages Manager</h4>
          </div>
          <div class="post col-2">
              <div class="image" :style="{backgroundImage: `url('${require('../assets/post-6-image@2x.png')}')`}"></div>
              <h4>Learn to take break</h4>
          </div>
      </div>
  </div>
</template>

<script>
export default {
    name: 'Intro',


}
</script>

<style lang="scss" scoped>
.intro {
    display: block;
    width: 100%;
    max-width: 1280px;
    margin: 0 auto;
    .posts {
        display: grid;
        grid-template-columns: repeat(4,1fr);
        grid-template-rows: repeat(3,196px);
        grid-gap: 30px;
        margin: 15px;
        .post {
            display:flex;
            flex-direction: column;
            background-color: #FFFFFF;
            box-shadow: 3px 3px 8px 0px rgba(0,0,0,0.2);
            cursor: pointer;

            .image {
                flex: 1;
                background-position: center;
                background-size: cover;
                background-repeat: no-repeat;
            }

            h4 {
                box-sizing: border-box;
                padding: 3px 15px 0px 15px;
                height: 50px;
                line-height: 50px;
                margin: 0px;
            }

            &.col-2 {
                grid-column: span 2;
            }
            &.row-2 {
                grid-row: span 2;
            }
        }
        .col-2 {
            max-width: none!important;
        }
    }
}
</style>