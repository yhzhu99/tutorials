package v1

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

// Register doc
// @description 注册
// @Tags user
// @Param username formData string true "用户名"
// @Param password1 formData string true "密码1"
// @Param password2 formData string true "密码2"
// @Param email formData string true "邮箱"
// @Param info formData string true "个人信息"
// @Success 200 {string} string "{"success": true, "message": "用户创建成功"}"
// @Router /user/register [post]
func Register(c *gin.Context) {
	username := c.Request.FormValue("username")
	password := c.Request.FormValue("password")

	// user := model.User{Username: username, Password: password}
	// service.CreateAUser(&user)
	c.JSON(http.StatusOK, gin.H{"success": true, "message": username + "/" + password})
	return

}
