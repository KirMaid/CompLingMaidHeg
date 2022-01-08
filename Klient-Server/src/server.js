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

const MongoClient = require("mongodb").MongoClient;
const {exec} = require('child_process');
const express        = require('express');
const bodyParser     = require('body-parser');
const app            = express();


exec('/usr/bin/python3.6 /home/virtual/PycharmProjects/CompLingMaidHeg/main.py')

const port = 8000;
app.listen(port, () => {
  console.log('We are live on ' + port);
});

let dbClient;



// создаем объект MongoClient и передаем ему строку подключения
const mongoClient = new MongoClient("mongodb://localhost:27017/");

mongoClient.connect(function(err, client){
    // обращаемся к базе данных
    const db = client.db("news_base");
    const collection = db.collection("news");
    app.locals.collection = db.collection("news");
    if(err) return console.log(err);
    // collection.find().toArray(function(err, results){ 
    //     // const tr = document.createElement("tr");
    //     // const LinkTd = document.createElement("td");
    //     // const TextTd = document.createElement("td");
    //     // const Td = document.createElement("td");
    //     // const LinkTd = document.createElement("td");
    //     //console.log(results[0].link);
    //     //client.close();
    // });
});

app.get("/", function(req, res){
    const collection = req.app.locals.collection;
    collection.find({}).toArray(function(err, news){
        if(err) return console.log(err);
        res.send(news)
    });
     
});

// mongoClient.connect(function(err, client){
//     if(err) return console.log(err);
//     dbClient = client;
//     app.locals.collection = client.db("usersdb").collection("users");
//     app.listen(3000, function(){
//         console.log("Сервер ожидает подключения...");
//     });
// });
 







