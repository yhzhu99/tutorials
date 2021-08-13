package model

import "gorm.io/gorm"

type User struct {
	gorm.Model
	UserID    uint64 `gorm:"primary_key; not null;" json:"user_id"`
	Username  string `gorm:"size:15; not null; unique" json:"username"`
	Password  string `gorm:"size:20; not null" json:"password"`
	Email     string `gorm:"size:20; not null; unique" json:"email"`
	UserType  int    `gorm:"not null;default:1" json:"user_type"` // 1：普通用户，2：已入柱用户；3：管理员
	BasicInfo string `gorm:"size:100" json:"basic_info"`
	Ban       bool   `gorm:"default:false" json:"ban"`
	// Favorites []Favorite `gorm:"ForeignKey:UserID;AssociationForeignKey:UserID" json:"favorites"`
	// Wishes    []Wish     `gorm:"ForeignKey:UserID;AssociationForeignKey:UserID" json:"wishes"`
}
