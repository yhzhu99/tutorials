# R Basics #1 Answer

My vector: `vec<-c(35,27,18,23,55,44,90,6)`

## Q1

What is the mean age of the people in your vector? Find out in two ways, with and without using the `mean()` command.

**Answer:**

```r
# with using the mean()
print(mean(vec))
# without using the mean()
print(sum(vec)/length(vec))
```

## Q2

How old is the youngest person in your vector? (Use an R command to find out.)

**Answer:**

```r
print(min(vec))
```

## Q3

What is the age gap between the youngest person and the oldest  person in your vector? (Again use R to find out, and try to be as general as possible in the sense that your code should work even if the  elements in your vector, or their order, change.)

**Answer:**

```r
print(max(vec)-min(vec))
```

## Q4

How many people in your vector are above age 25? (Again, try to make your code work even in the case that your vector changes.)

**Answer:**

```r
print(length(which(vec>25)))
```

## Q5

Replace the age of the oldest person in your vector with the age of someone else you know.

**Answer:**

```r
vec[which(vec==max(vec))]<-20
```

## Q6

Create a new vector that indicates how old each person in your vector will be in 10 years.

**Answer:**

```r
vec1<-vec+10
```

## Q7

Create a new vector that indicates what year each person in your vector will turn 100 years old.

**Answer:**

```r
vec2<-2020-vec+100
```

## Q8

Create a new vector with a random sample of 3 individuals from  your original vector. What is the mean age of the people in this new  vector?

**Answer:**

```r
vec3<-sample(vec,3)
print(mean(vec3))
```
