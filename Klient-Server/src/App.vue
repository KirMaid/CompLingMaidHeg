<template>
  <HelloWorld msg="Welcome to Your Vue.js App" />
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import axios from 'axios';

// const {exec} = require('child_process');

export default {
  name: "App",
  data:()=>({
      news: []
  }),
  created() {
    axios.get("http://localhost:8000/").then((response) => {
      this.news = response.data;
      alert(response.data);
    });
    // alert(news);
  },
  methods: {},
  components: {
    HelloWorld,
  }
};


// const MongoClient = require("mongodb").MongoClient;

// // const express        = require('express');
// // const bodyParser     = require('body-parser');
// // const app            = express();
// const mongoClient = new MongoClient("mongodb://localhost:27017/");
// mongoClient.connect(function(err, client){
//     // обращаемся к базе данных
//     const db = client.db("news_base");
//     const collection = db.collection("news");
//     if(err) return console.log(err);
//     collection.find().toArray(function(results){
//       alert(results[0].link);
//       client.close();
//     });
// });

// exec(
//   "/usr/bin/python3.6 /home/virtual/PycharmProjects/CompLingMaidHeg/main.py"
// );
//alert('aboba');
</script>

<style>
#app {
}
</style>
