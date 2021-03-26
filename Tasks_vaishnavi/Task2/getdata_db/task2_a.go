package main

import (
	"database/sql"
	"fmt"
	"log"
	"net/http"

	_ "github.com/go-sql-driver/mysql"
)

type books struct {
	Isbn   string  `json:"Isbn"`
	Title  string  `json:"Title"`
	Author string  `json:"Author"`
	Price  float32 `json:"Price"`
}

func helloHandler(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/book" {
		http.Error(w, "404 not found.", http.StatusNotFound)
		return
	}

	if r.Method != "GET" {
		http.Error(w, "Method is not supported.", http.StatusNotFound)
		return
	}

	fmt.Println("go mysql")

	db, err := sql.Open("mysql", "root:root@tcp(localhost)/book")

	if err != nil {
		panic(err.Error())
	}
	defer db.Close()
	result, err := db.Query("select * from books")
	if err != nil {
		panic(err.Error())
	}
	for result.Next() {
		var books books
		err = result.Scan(&books.Isbn, &books.Title, &books.Author, &books.Price)
		if err != nil {
			panic(err.Error())
		}
		fmt.Printf(books.Isbn, " ", books.Title, " ", books.Author, " ", books.Price)
		fmt.Fprintf(w, "Isbn : %s\n", books.Isbn)
		fmt.Fprintf(w, "Title : %s\n", books.Title)
		fmt.Fprintf(w, "Author : %s\n", books.Author)
		fmt.Fprintf(w, "Price : %f\n", books.Price)
	}
}

func main() {
	fileServer := http.FileServer(http.Dir("./static")) // New code
	http.Handle("/", fileServer)                        // New code

	//http.HandleFunc("/form", formHandler)
	//http.HandleFunc("/articles", returnAllArticles)
	http.HandleFunc("/book", helloHandler)

	fmt.Printf("Starting server at port 8080\n")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatal(err)
	}
}
