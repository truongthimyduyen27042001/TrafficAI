<template>
  <div class="test_main">
    <div class="form-add-card">
      <b-form-group
        id="userid"
        description="Let us know your id."
        label="Enter your id"
        label-for="input-1"
        valid-feedback="Thank you!"
        v-model="cardActive.id"
      >
        <b-form-input id="input-1" v-model="cardActive.id" trim></b-form-input>
      </b-form-group>
      <b-form-group
        id="usertitle"
        description="Let us know your title."
        label="Enter your title"
        label-for="input-1"
        valid-feedback="Thank you!"
        v-model="cardActive.title"
      >
        <b-form-input
          id="input-1"
          v-model="cardActive.title"
          trim
        ></b-form-input>
      </b-form-group>
      <b-form-group
        id="userurl"
        description="Let us know your url."
        label="Enter your url"
        label-for="input-1"
        valid-feedback="Thank you!"
        v-model="cardActive.url"
      >
        <b-form-input id="input-1" v-model="cardActive.url" trim></b-form-input>
      </b-form-group>
      <b-form-group
        id="usertext"
        description="Let us know your text."
        label="Enter your text"
        label-for="input-1"
        valid-feedback="Thank you!"
        v-model="cardActive.text"
      >
        <b-form-input
          id="input-1"
          v-model="cardActive.text"
          trim
        ></b-form-input>
      </b-form-group>
      <button
        class="btn btn-block btn-success m-auto"
        type="submit"
        @click="submit"
      >
        Submit
      </button>
    </div>
    <button
      class="btn btn-block btn-success ml-11"
      type="button"
      @click="getAllData"
      style="width: 80%"
    >
      Get Data
    </button>
    <div class="lst-cards">
      <b-card
        v-for="card in cards"
        :key="card.id"
        :title="card.title"
        :img-src="card.url"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 20rem"
        class="mb-2 card"
      >
        <b-card-text>
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </b-card-text>

        <b-button href="#" variant="primary">Go somewhere</b-button>
      </b-card>
    </div>
  </div>
</template>

<script>
import firebase from 'firebase';
export default {
  name: "test",
  beforeCreate() {
    console.log("before create");
    const firebaseConfig = {
      apiKey: "AIzaSyDhoLlngcuh9u7ClXWQxzD-r3SEl4jgekI",
      authDomain: "testvuejspbl5.firebaseapp.com",
      databaseURL: "https://testvuejspbl5-default-rtdb.firebaseio.com",
      projectId: "testvuejspbl5",
      storageBucket: "testvuejspbl5.appspot.com",
      messagingSenderId: "413422867853",
      appId: "1:413422867853:web:2f024848ab66d3398b59c4",
      measurementId: "G-JS5ZPMBKD0"
    };
    let app = firebase.initializeApp(firebaseConfig)
    let db = app.database()
    let apiCards = db.ref('cards')
    console.log('Cards: ',apiCards)
  },
  data() {
    return {
      cardActive: {
        id: "",
        title: "",
        url: "",
        text: "",
      },
      cards: [
        {
          id: 1,
          title: "Mỹ Duyên",
          url: "https://scontent.fdad3-4.fna.fbcdn.net/v/t39.30808-6/280182294_1976525705881561_8386645149956684074_n.jpg?_nc_cat=105&ccb=1-6&_nc_sid=730e14&_nc_ohc=yXNNdxjQH2IAX9UdFuu&_nc_ht=scontent.fdad3-4.fna&oh=00_AT94pX1HtIoaYyWVH8XmyJU_F6rOeHQEzvstCkcOUz3y-Q&oe=62892CA4",
          text: "Some quick example text to build on the card title and make up the bulk of the card's content.",
        },
        {
          id: 2,
          title: "Lâm Toàn",
          url: "https://scontent.fdad3-3.fna.fbcdn.net/v/t39.30808-6/280101011_1976525759214889_5194054413878958857_n.jpg?_nc_cat=100&ccb=1-6&_nc_sid=730e14&_nc_ohc=RygrBvhg7lYAX9jb1LE&_nc_ht=scontent.fdad3-3.fna&oh=00_AT8i_NDqGK9fqdu8cqOh-GLuWQLhPkefKOEnDxcKEDBhEw&oe=6287B286",
          text: "Some quick example text to build on the card title and make up the bulk of the card's content.",
        },
        {
          id: 3,
          title: "Lê Tuân",
          url: "https://scontent.fdad3-4.fna.fbcdn.net/v/t39.30808-6/280760557_1976525512548247_8645010038496126044_n.jpg?_nc_cat=101&ccb=1-6&_nc_sid=730e14&_nc_ohc=2c9xPSIxavAAX8pns8l&_nc_ht=scontent.fdad3-4.fna&oh=00_AT8OF4Dsw5mqnkhzuanRgntT6qcrSsCw96NCSDmsxZPv-A&oe=6287702D",
          text: "Some quick example text to build on the card title and make up the bulk of the card's content.",
        },
        {
          id: 4,
          title: "Phương Dung",
          url: "https://scontent.fdad3-4.fna.fbcdn.net/v/t39.30808-6/280575934_1976525285881603_5136454990827298573_n.jpg?_nc_cat=107&ccb=1-6&_nc_sid=730e14&_nc_ohc=xhGHkUIAEXUAX8Ymfu0&_nc_ht=scontent.fdad3-4.fna&oh=00_AT_5vQ1Ta8FkX9owaO34M--6oEZPmZk-GpZp-tox6lbY6w&oe=628925E2",
          text: "Some quick example text to build on the card title and make up the bulk of the card's content.",
        },
        {
          id: 5,
          title: "Bách Khoa",
          url: "https://scontent.fdad3-1.fna.fbcdn.net/v/t39.30808-6/280362458_1976525642548234_7260503626422927675_n.jpg?_nc_cat=103&ccb=1-6&_nc_sid=730e14&_nc_ohc=pMobKyRtwTgAX-WfR1v&tn=rgZo8VAy55WC-WUR&_nc_ht=scontent.fdad3-1.fna&oh=00_AT__aOP8wtR_QDo5kHOdSoV8LSO3Tqqx36E1rVDA1ycoyA&oe=6287C00B",
          text: "Some quick example text to build on the card title and make up the bulk of the card's content.",
        },
        {
          id: 6,
          title: "Trường Vũ",
          url: "https://scontent.fdad3-3.fna.fbcdn.net/v/t39.30808-6/280110823_1976525592548239_2526562642132735991_n.jpg?_nc_cat=100&ccb=1-6&_nc_sid=730e14&_nc_ohc=UxcxEYvMSnQAX-7prwD&tn=rgZo8VAy55WC-WUR&_nc_ht=scontent.fdad3-3.fna&oh=00_AT_VVAoOBJFJ-n6oqQWzU76TUFfAR3sXRAX48g14ZKbFkQ&oe=6287D3C1",
          text: "Some quick example text to build on the card title and make up the bulk of the card's content.",
        },
      ],
    };
  },
  methods: {
    submit() {
      // POST /someUrl
      this.$http
        .post(
          "https://testvuejspbl5-default-rtdb.firebaseio.com/cards.json",
          this.cardActive
        )
        .then(
          (response) => {
            console.log("Response: ", response);
          },
          (error) => {
            console.log("Error: ", error);
          }
        );
    },
    getAllData() {
      this.$http
        .get("https://testvuejspbl5-default-rtdb.firebaseio.com/cards.json")
        .then((response) => {
          console.log("Success");
          console.log("Response: ", response.json());
          return response.json();
        })
        .then((data) => {
          console.log("Data: ", data);
          const newArr = [];
          for (let key in data) {
            console.log("key: ", key);
            newArr.push(data[key]);
          }
          this.cards = newArr;
        });
    },
  },
};
</script>

<style lang="scss" scoped>
.test_main {
  width: 100vw;
  .form-add-card {
    width: 60%;
    margin: 30px auto;
  }
  .lst-cards {
    margin-top: 50px;
    display: flex;
    flex-wrap: wrap;
    .card {
      margin-right: 10px;
      margin-left: 10px;
    }
  }
}
</style>
