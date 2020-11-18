package dao

import (
	"github.com/jinzhu/gorm"
)

var (
	DB *gorm.DB
)

func InitMySQL() (err error) {
	DB, err = gorm.Open("mysql", "root:@buaa21@tcp(101.132.227.56:3306)/test?charset=utf8&parseTime=True&loc=Local")
	if err != nil {
		panic(err)
	}
	// 为模型`User`创建表
	//DB.CreateTable(&User{})

	// 创建表`users'时将“ENGINE = InnoDB”附加到SQL语句
	//DB.Set("gorm:table_options", "ENGINE=InnoDB").CreateTable(&User{})
	//user := User{ID: 100, Name: "Jinzhu"}
	//service.CreateAUser(&user)
	//DB.Create(&user)
	return DB.DB().Ping()
}

func Close() {
	DB.Close()
}
