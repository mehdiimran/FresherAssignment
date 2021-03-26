package main

import (
	"database/sql"
	"fmt"
	"log"
	"net/http"

	_ "github.com/go-sql-driver/mysql"
)

type Persons struct {
    PersonID int `json:"PersonID"`
    LastName string `json:"LastName"`
    FirstName string `json:"FirstName"`
    Address string `json:"Address"`
    City string `json:"City"`
}

func gosqlhandler(w http.ResponseWriter, r *http.Request) {
    if r.URL.Path != "/gosql" {
        http.Error(w, "404 not found.", http.StatusNotFound)
        return
    }

    if r.Method != "GET" {
        http.Error(w, "Method is not supported.", http.StatusNotFound)
        return
    }
    
    fmt.Println("Go MySQL")

    db, err := sql.Open("mysql", "root:manager@tcp(127.0.0.1:3306)/gosql")

    if err != nil {
        panic(err.Error())
    }

    defer db.Close()
    result, err := db.Query("SELECT * FROM Persons")
    if err != nil {
        panic(err.Error())
    }

    for result.Next() {
        var person Persons
        err = result.Scan(&person.PersonID, &person.LastName, &person.FirstName, &person.Address, &person.City)
        if err != nil {
            panic(err.Error())
        }

        fmt.Println(person.PersonID," ", person.LastName," ", person.FirstName," ", person.Address," ", person.City)
        fmt.Fprintf(w, "Person ID : %d\n", person.PersonID)
        fmt.Fprintf(w, "Last Name : %s\n", person.LastName)
        fmt.Fprintf(w, "First Name: %s\n", person.FirstName)
        fmt.Fprintf(w, "Address   : %s\n", person.Address)
        fmt.Fprintf(w, "City      : %s\n", person.City)
    }
}

func main() {
    fileServer := http.FileServer(http.Dir("./static"))
    http.Handle("/", fileServer)
    http.HandleFunc("/gosql", gosqlhandler)

    fmt.Printf("Starting server at port 8080\n")
    if err := http.ListenAndServe(":8080", nil); err != nil {
        log.Fatal(err)
    }
}