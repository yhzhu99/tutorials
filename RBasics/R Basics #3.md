# R Basics #3 Writing Functions

> This tutorial explains how you can write your own functions in R. Why do this? Functions are useful when you want to execute a task over and  over again, resulting in less verbose and more easily interpretable code. After explaining the basics of writing functions, this tutorial  covers two data science applications for writing functions. 	

## Motivation

To illustrate the value of functions, let’s start by a thought  experiment: say R didn’t provide a function for finding the median of a  numeric vector. (Of course this is not true — R has a built-in function  called `median()` for this purpose.) In this annoying scenario, it would still be possible to find the median using a few lines of code.

```r
# Create a numeric vector 
v <- c(2, 5, 8, 0, 10)

# Find the number of elements in v  
n <- length(v)

# Is n odd?
n %% 2  # use mod to find remainder after dividing by 2; if remainder is 1 --> odd
 [1] 1
# Cool, it's odd so let's find the mid-value after sorting v
v_sort <- sort(v)
v_sort[n / 2 + 1] # this is the median
 [1] 5
```

Ok, we found the median, but what a nightmare! Imagine if we had to  go through these steps every time we wanted to find the median. Plus,  the code above isn’t general enough to account for scenarios in which  the numeric vector has an even number of elements. In scenarios like  this, it’s therefore extremely useful to write a function. Here’s one  way of doing so for finding the median:

```r
median2 <- function(vec) {
    n <- length(vec)
    odd <- n %% 2 == 1
    vec_sort <- sort(vec)

    if(odd) {
        result <- vec_sort[n / 2 + 1]
    } else {
        result <- (vec_sort[n / 2] + vec_sort[n / 2 + 1]) / 2
    }

    return(result)
}
```

Let’s test if it works on two vectors, one with an odd number of elements and the other with an even number:

```r
v1 <- c(2, 5, 8, 0, 10)
median2(v1)
 [1] 5
v2 <- c(2, 5, 8, 0, 10, 12)
median2(v2)
 [1] 6.5
```

This motivating example shows that writing functions can save us many lines of code and avoid mistakes that inevitably will happen if you  rely too heavily on copying and pasting code.

## Building blocks

### 单一参数

Remind yourself of a basic mathematical principle: a function takes  some input, transforms it, and outputs the transformation. For example,  the function *f(x) = 2x* takes a vector *x* and transforms each element to twice its original value. Functions in R (and other languages) do the same thing. For example:

```r
doubleval <- function(x) 2 * x # write a function that doubles x
doubleval(c(3, 5, 7)) # test the function on a vector
 [1]  6 10 14
```

Here are other, equivalent, ways of writing this function:

```r
doubleval <- function(x) return(2 * x)
doubleval <- function(x) {
    tranformation <- 2 * x
    transformation # 虽然可以不指明return的参数，还是写return(transformation)得好
}
doubleval <- function(x) {
    tranformation <- 2 * x
    return(transformation)
}
```

Observe the following:

1. Functions include some input or, more technically, one or many *parameters*. The function `doubleval` has one parameter called `x`; `median2` also has one parameter (`vec`). The name of parameters are arbitrary: you can call them whatever you  want as long as you reference the same name within the function. Note  that functions often have more than one parameter.

2. Functions include a line that specifies the output of the function. For clarity, it is useful to use the `return()` statement for indicating what the function is outputting, although this is not necessary.

3. If a function includes several operations, those operations  should be written on separate lines and be surrounded by curly brackets (`{}`). Very simple functions can be written on one line, omitting the curly brackets.

   ```r
   func<-function(x) return(x*2) # 即可以不使用{}。建议不管函数多简单，都写{}
   ```

4. Objects created within functions do not exist in the global variable space. For example, `vec_sort` in the function `median2` (and other objects created within the function) cannot be accessed  outside the function. This relates to an important feature of  programming called [scope](http://www.wikiwand.com/en/Scope_(computer_science)). (全局变量 & 局部变量的概念：在函数中所使用到的新定义的参数都是局部变量，函数执行完便不存在了。全局变量会出现在Environment - Global Environment里。)

### 多参数

```r
func<-function(a,b){
  res<-a+b
  return(res)
}
# R里面很智能，a可以是单纯的一个numeric，也可以是vector，只要传入的参能与运算相匹配即可
func(3,4)
func(c(1,2),c(3,4))
```

## Exercises

1. Write a function called `second_largest` that finds the  second largest value in a vector of numeric values. That is, the input  should be a numeric vector and the output should be the second largest  value in the vector. You can assume that the input vector has at least  two values. Test your function on the following two vectors:

- `v1 <- 1:10`
- `v2 <- c(15, 1000, 2, 3, 8)`

2. Modify the `second_largest` function so that it accounts  for two special cases: (1) when the user inputs a numeric vector with  only one value, the function should return the message “Invalid input:  at least two values required”; (2) when the user inputs a vector that is **not** numeric, the function should return the message  “Invalid input: only numeric vectors accepted”. Test your new function  on the following vectors:

- `v1 <- 1:10`
- `v2 <- 2`
- `v3 <- c("banana", "apple", "orange")`
- `v4 <- as.factor(1:10)`

