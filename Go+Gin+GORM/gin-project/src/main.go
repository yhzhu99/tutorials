package main

import (
	"fmt"
	"gin-project/src/dao"

	"github.com/gin-gonic/gin"

	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/mysql"
)

func main() {
	db, err := gorm.Open("mysql",
		"root:@buaa21@tcp(101.132.227.56:3306)/test?charset=utf8&parseTime=True&loc=Local")
	db.SingularTable(true)
	if err != nil {
		fmt.Println(err)
		return
	} else {
		fmt.Println("connection succeeded")
	}
	defer db.Close()

	dao.New()

	r := gin.Default()
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": 43,
		})
	})
	r.Run()
}
