package controller

import (
	"gin-project/dao"
	"gin-project/server"

	"github.com/gin-gonic/gin"
)

func Test(c *gin.Context) {
	user := dao.User{ID: 102, Name: "施哲纶"}
	server.CreateAUser(&user)
	c.JSON(200, gin.H{
		"message": "create a user",
	})
}
