package main

import (
	"fmt"
	"runtime"
)

func main() {
	fmt.Println("Go环境报告:")
	fmt.Printf("版本: %s\n", runtime.Version())
	fmt.Printf("操作系统: %s\n", runtime.GOOS)
	fmt.Printf("架构: %s\n", runtime.GOARCH)
	fmt.Printf("GOROOT: %s\n", runtime.GOROOT())
	fmt.Println("环境验证通过！")
}
