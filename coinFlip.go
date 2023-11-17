package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())
	if rand.Intn(2) == 0 {
		fmt.Println("Heads")
	} else {
		fmt.Println("Tails")
	}
}
