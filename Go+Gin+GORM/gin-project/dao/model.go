package dao

type User struct {
	ID   uint   `gorm:"primary_key"`
	Name string `gorm:"size:255"` // string默认长度为255, 使用这种tag重设。
}
