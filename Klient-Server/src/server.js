const express = require('express');
const mongoose = require("mongoose");
const Schema = mongoose.Schema;

var cors = require('cors')

const objectId = require("mongodb").ObjectId;
const MongoClient = require("mongodb").MongoClient;
const spawn = require("child_process").spawnSync;
const bodyParser = require('body-parser');

const app = express();
app.use(cors())
cors({ credentials: true, origin: true })
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

app.post("/", function(req, res) {
    console.log("Сервер запускает краулер...");
    const pythonProcess = spawn('D:/Kirill/Labs 3 kurs/Ling_Sema/Parser/venv/Scripts/python.exe', ["D:/Kirill/Labs 3 kurs/Ling_Sema/Parser/Krauler.py"]);
    res.send("Ok")
    console.log("Сервер отправил ответ...");
});