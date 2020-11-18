package router

import (
	"gin-project/controller"

	"github.com/gin-gonic/gin"
)

func SetupRouter() *gin.Engine {
	r := gin.Default()

	// api
	apiGroup := r.Group("api")
	{
		apiGroup.GET("/ping", controller.Test)
	}
	return r
}
