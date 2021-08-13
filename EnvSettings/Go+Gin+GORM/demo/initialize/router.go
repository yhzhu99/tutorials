package initialize

import (
	"demo/middleware"
	"demo/router"

	"github.com/gin-gonic/gin"
)

func SetupRouter() *gin.Engine {
	r := gin.Default()
	r.Use(middleware.Cors())
	Group := r.Group("")
	{
		router.InitUserRouter(Group) // 注册用户路由
	}
	return r
}
