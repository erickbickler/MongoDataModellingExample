const path = require('path');
const express = require('express');
const mongo = require('mongodb')

const PORT = process.env.PORT || 3001;

const app = express();

// middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const uri = ;
const client = new mongo.MongoClient(uri);

app.use(express.static(path.resolve(__dirname, '../client/build')));

app.get("/api", (req, res) => {
    res.json({ message: "Hello from server!" });
});



app.get('*', (req, res) => {
    res.sendFile(path.resolve(__dirname, '../client/build', 'index.html'));
});

app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`);
  console.log(`Go to http://localhost:${PORT}/\n`);
});