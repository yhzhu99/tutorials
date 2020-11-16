# Golang 后端环境配置

## Go

> Go is an open source programming language that makes it easy to build simple, reliable, and efficient software.

[Download Go](https://golang.org/dl/)

### 检查环境

- 环境变量(应该已经配好了)

![](2020-11-16-14-14-06.png)

- 设置代理

在cmd中：

```go
go env -w GOPROXY=https://goproxy.cn,direct`
```

- 检查Go是否安装成功

![](2020-11-16-14-15-32.png)

## Goland

> GoLand is a cross-platform IDE built specially for Go developers

[Download Goland](https://www.jetbrains.com/go/)

- Example: create a new project: "awesomeProject"

[Reference: 让你的Golang项目在IDE里跑起来](https://cloud.tencent.com/developer/article/1596713)

![](2020-11-16-16-08-01.png)

```go
go build main.go
go run main.go
```

## Gin

## GORM

> ORM