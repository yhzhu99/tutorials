package main

import (
	"gin-project/src/dao"

	"github.com/gin-gonic/gin"
)

func main() {
	dao.New()
	r := gin.Default()
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": 43,
		})

	})
	r.Run()
}
