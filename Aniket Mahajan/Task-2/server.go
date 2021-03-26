package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"log"
	"net/http"

	_ "github.com/go-sql-driver/mysql"
)

type Ingredient struct {
	Title  string `json:"Title"`
	Colour string `json:"Colour"`
	Price  string `json:"Price"`
}

type Ingredients []Ingredient

func allIngredients(w http.ResponseWriter, r *http.Request) {
	ingredients := Ingredients{
		Ingredient{Title: "Test1", Colour: "Test", Price: "12000"},
	}
	fmt.Println("All Ingredients")
	json.NewEncoder(w).Encode(ingredients)
}
func helloHandler(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/hello" {
		http.Error(w, "404 not found.", http.StatusNotFound)
		return
	}
	if r.Method != "GET" {
		http.Error(w, "Method is not supported.", http.StatusNotFound)
		return
	}

	fmt.Fprintf(w, "Hello!")
}

func main() {
	http.HandleFunc("/hello", helloHandler)
	http.HandleFunc("/ingredients", allIngredients)
	fmt.Println("go mysql")
	db, err := sql.Open("mysql", "root:manager@tcp(127.0.0.1:3306)/user")
	if err != nil {
		panic(err.Error())
	}
	defer db.Close()

	insert, err := db.Query("INSERT INTO user values('Aniket')")

	if err != nil {
		panic(err.Error())
	}
	defer insert.Close()

	fmt.Println("successfully added into tables")
	fmt.Println("successfully Connected to mysql database")
	fmt.Printf("Starting server at port 8080\n")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatal(err)
	}
}
