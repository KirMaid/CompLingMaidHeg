<template>
  <Header />
  <HelloWorld />
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import Header from "./components/Header.vue";
// const {exec} = require('child_process');

export default {
  name: "App",
  components: {
    Header,
    HelloWorld,
  },
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
