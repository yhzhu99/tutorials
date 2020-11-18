package main

import (
	"gin-project/dao"
	"gin-project/router"

	_ "github.com/jinzhu/gorm/dialects/mysql"
)

func main() {
	err := dao.InitMySQL()
	if err != nil {
		panic(err)
	}
	defer dao.Close()
	r := router.SetupRouter()
	r.Run()
}
