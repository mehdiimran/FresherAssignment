package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"net/http"

	_ "github.com/mattn/go-sqlite3"
)

var port = 8080

type Employee struct {
	FirstName string `json:"first_name"`
	LastName  string `json:"last_name"`
	Email     string `json:"email"`
}

func getAllEmployees(w http.ResponseWriter, req *http.Request) {
	db, err := sql.Open("sqlite3", "./employees.db")
	if err != nil {
		panic(err)
	}
	defer db.Close()

	rows, err := db.Query("SELECT firstname, lastname, email FROM employees")
	if err != nil {
		panic(err)
	}
	defer rows.Close()

	var employee Employee
	var employees []Employee

	for rows.Next() {
		rows.Scan(&employee.FirstName, &employee.LastName, &employee.Email)
		employees = append(employees, employee)
	}

	employeesJSON, err := json.Marshal(employees)
	if err != nil {
		panic(err)
	}

	w.Write(employeesJSON)
}

func getEmployee(w http.ResponseWriter, req *http.Request) {
	ids, ok := req.URL.Query()["id"]

	if !ok || len(ids) < 1 || len(ids[0]) < 1 {
		fmt.Fprintf(w, "URL parameter 'id' is missing")
		return
	}

	id := ids[0]

	db, err := sql.Open("sqlite3", "./employees.db")
	if err != nil {
		panic(err)
	}
	defer db.Close()

	rows, err := db.Query("SELECT firstname, lastname, email FROM employees WHERE id = ?", id)
	if err != nil {
		panic(err)
	}
	defer rows.Close()

	var employee Employee

	for rows.Next() {
		rows.Scan(&employee.FirstName, &employee.LastName, &employee.Email)
		break
	}

	employeeJSON, err := json.Marshal(employee)
	if err != nil {
		panic(err)
	}

	w.Write(employeeJSON)
}

func main() {

	http.HandleFunc("/employees", getAllEmployees)
	http.HandleFunc("/employee", getEmployee)

	fmt.Printf("Started listening to port %v\n", port)

	addr := fmt.Sprintf(":%v", port)

	if err := http.ListenAndServe(addr, nil); err != nil {
		panic(err)
	}
}
