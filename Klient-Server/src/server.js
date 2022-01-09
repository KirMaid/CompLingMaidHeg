// const express = require('express');
// const mongoose = require('mongoose');
// const morgan = require('morgan');
// const path = require('path');
// const app = express();

// app.set('port', 3000);

// mongoose.connect('mongodb://localhost:27017/news_base', { useNewUrlParser: true });

// var newsSchema = new Schema({
//     link:  String,
//     title: String,
//     date:   String,
//     content:   String,
//     videolink:   String,
// });


// app.use(express.json());
// app.use(express.urlencoded({extended: false}));
// app.use(morgan('dev'));
const express = require('express');
const mongoose = require("mongoose");
// const express = require("express");
const Schema = mongoose.Schema;
//const app = express();

const objectId = require("mongodb").ObjectId;
const MongoClient = require("mongodb").MongoClient;
const { exec } = require('child_process');

const bodyParser = require('body-parser');
const jsonParser = express.json();

const app = express();
const port = 3000;
var newsScheme = new Schema({
    id: String,
    link: String,
    title: String,
    date: String,
    content: String,
    videolink: String,
});
const newsModel = mongoose.model("new", newsScheme);

mongoose.connect("mongodb://localhost:27017/news_base", { useUnifiedTopology: true, useNewUrlParser: true }, function(err) {
    if (err) return console.log(err);
    app.listen(3000, function() {
        console.log("Сервер ожидает подключения...");
    });
});

app.get("/", function(req, res) {
    newsModel.find({}, function(err, news) {
        if (err) return console.log(err);
        res.header("Access-Control-Allow-Origin", "*");
        console.log("Сервер передаёт данные...");
        res.send(news)
    });
});






//exec('/usr/bin/python3.6 /home/virtual/PycharmProjects/CompLingMaidHeg/main.py')

// let dbClient;

// // создаем объект MongoClient и передаем ему строку подключения
// const mongoClient = new MongoClient("mongodb://localhost:27017/");

// mongoClient.connect(function(err, client) {
//     // обращаемся к базе данных
//     if (err) return console.log(err);
//     dbClient = client;
//     app.locals.collection = client.db("news_base").collection("news");
//     app.listen(3000, function() {
//         console.log("Сервер ожидает подключения...");
//     });
// });

// app.get("/", function(req, res) {
//     console.log("Сервер передаёт данные...");
//     const collection = req.app.locals.collection;
//     res.header("Access-Control-Allow-Origin", "*");
//     collection.find({}).toArray(function(err, news) {
//         if (err) return console.log(err);
//         res.header("Access-Control-Allow-Origin", "*");
//         res.send(news);
//     });
// });

// process.on("SIGINT", () => {
//     dbClient.close();
//     process.exit();
// });