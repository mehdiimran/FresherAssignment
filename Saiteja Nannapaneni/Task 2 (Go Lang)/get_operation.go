package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
)

func getRequestTest() {
	const httpbin = "https://httpbin.org/get"

	//perform get operation
	resp, err := http.Get(httpbin)
	if err != nil {
		return
	}

	//caller is responsible for closing the response
	defer resp.Body.Close()

	//we can access parts of the response to get info:
	fmt.Println("Status:", resp.Status)
	fmt.Println("Status Code:", resp.StatusCode)
	fmt.Println("Protocol:", resp.Proto)
	fmt.Println("Content Length:", resp.ContentLength)

	//use string builder to build content from bytes
	var sb strings.Builder

	//read content and write it to builder

	content, _ := ioutil.ReadAll(resp.Body)
	bytecount, _ := sb.Write(content)

	//format the output
	fmt.Println(bytecount, sb.String())
}

func main() {
	//execute the get request
	getRequestTest()
}
