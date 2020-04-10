/*
                    Import all node modules

                    @ Core node modules
*/

var express = require("express");
var http = require("http");
var mysql = require("mysql");
var app = express();
var bodyParser = require("body-parser");


/*
                    Parse all form data
*/
app.use(bodyParser.urlencoded({
    extended: true
}));



/*
                    This is view engine
                    Template parsing
                    We are using EJS types
*/
app.set("view engine", "ejs");


/*
        Import all related JavaScript and CSS files to inject in our APP
*/
app.use("/js", express.static(__dirname + "/node_modules/bootstrap/dist/js"));
app.use("/js", express.static(__dirname + "/node_modules/tether/dist/js"));
app.use("/js", express.static(__dirname + "/node_modules/jquery/dist"));
app.use("/css", express.static(__dirname + "/node_modules/bootstrap/dist/css"));


/*
 * Database is connection details
 * Localhost - when in production mode change this to your host
 * User - User name of the database
 * Password - Database password
 * Database - Database is the name of the database
 */
const con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "1234",
    database: "application"
});


/*
Global site title and base url
*/
const siteTitle = "Agami";
const baseURL = "http://localhost:4000/"

/*
When page is loaded
Default page is loaded and the data is being called from MySQL database
We also adding some JavaScript and CSS styles
For all the dependencies - see the package.json file for more information
*/
app.get("/", function (req, res) {
    /* 
    Get the event list
    */
    con.query("USE application")
    con.query("SELECT * FROM user_data", function (err, result) {
        res.render("pages/index", {
            siteTitle: siteTitle,
            pageTitle: "Even list",
            items: result
        });
    })

});

/* 
        Add new event
*/
app.get("/event/add", function (req, res) {
    /* 
    Adding new event
    */
    res.render("pages/add-event.ejs", {
        siteTitle: siteTitle,
        pageTitle: "Adding New Event",
        items: ""

    });

});

/*
        This is a POST method to data and pre-populate to the firm
*/
app.post("/event/add", function (req, res) {
    /*
            Get the record base on ID
    */
    var query = "INSERT INTO user_data VALUES (NULL,";
    var the_name = req.body.name;
    query += " '" + the_name[1] + "'," + req.body.bill + ")";

    console.log(query)
    console.log(the_name)

    con.query(query, function (err, result) {
        res.redirect(baseURL);
    });
});


/*
Updating data
*/
app.get("/event/edit/:id", function (req, res) {
    /*
            Get the record base on ID
    */
    con.query("SELECT * FROM user_data WHERE id= '" + req.params.id + "'", function (err, result) {

        res.render("pages/edit-event", {
            siteTitle: siteTitle,
            pageTitle: "Editing : " + result[0].name,
            item: result
        });
    });
});

/*
Updating with post
*/
app.post("/event/edit/:id", function(req, res) {
    var query = "UPDATE user_data SET";
        query += " name = '"+req.body.name+"',";
        query += " bill = "+req.body.bill+" ";
        query += "WHERE id = "+req.params.id+"";
    console.log(query)
    con.query(query, function(err, result) {
            res.redirect(baseURL);
    });
});


/*
This is a GET method to delete from the database
*/
app.get("/event/delete/:id", function(req, res) {
    con.query("DELETE FROM user_data WHERE id="+req.params.id, function (err, result) {
        res.redirect(baseURL);
    })
})

/*
            Connect to the server
*/
var server = app.listen(4000, function () {
    console.log("Server started on 4000...");
});