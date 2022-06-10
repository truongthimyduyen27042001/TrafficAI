<template>
  <div>
    <div class="panel-body">
      <table class="table table-striped">
        <thead>
          <tr>
            <th>Title</th>
            <th>Author</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="book in books" v-bind:key="book['.key']">
            <td>
              <a v-bind:href="book.url">{{ book.title }}</a>
            </td>
            <td>{{ book.author }}</td>
            <td>
              <span
                class="glyphicon glyphicon-trash"
                aria-hidden="true"
                v-on:click="removeBook(book)"
              ></span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
import Firebase from "firebase";

const firebaseConfig = {
  apiKey: "AIzaSyDhoLlngcuh9u7ClXWQxzD-r3SEl4jgekI",
  authDomain: "testvuejspbl5.firebaseapp.com",
  databaseURL: "https://testvuejspbl5-default-rtdb.firebaseio.com",
  projectId: "testvuejspbl5",
  storageBucket: "testvuejspbl5.appspot.com",
  messagingSenderId: "413422867853",
  appId: "1:413422867853:web:2f024848ab66d3398b59c4",
  measurementId: "G-JS5ZPMBKD0",
};

let app = Firebase.initializeApp(firebaseConfig);
let db = app.database();
let booksRef = db.ref("books");

export default {
  name: "books",
  data() {
    return {
      newBook: {
        title: "",
        author: "",
        url: "http://",
      },
    };
  },
  firebase: {
    books: booksRef,
  },
  methods: {
    addBook() {
      booksRef.push(this.newBook);
      this.newBook.title = "";
      this.newBook.author = "";
      this.newBook.url = "http://";
    },
    removeBook(book) {
      booksRef.child(book[".key"]).remove();
    },
  },
};
</script>
<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 20px;
}
</style>
