package main

import (
	"fmt"
	"gin-project/src/dao"
	"time"

	"github.com/gin-gonic/gin"

	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/mysql"
)

type User struct {
	gorm.Model
	Birthday time.Time
	Age      int
	Name     string `gorm:"size:255"`       // string默认长度为255, 使用这种tag重设。
	Num      int    `gorm:"AUTO_INCREMENT"` // 自增
}

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

	// 创建表`users'时将“ENGINE = InnoDB”附加到SQL语句
	db.Set("gorm:table_options", "ENGINE=InnoDB").CreateTable(&User{})

	// 检查模型`User`表是否存在
	fmt.Println(db.HasTable(&User{}))

	// 检查表`users`是否存在
	fmt.Println(db.HasTable("users"))

	fmt.Println("--------------------------------")

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
