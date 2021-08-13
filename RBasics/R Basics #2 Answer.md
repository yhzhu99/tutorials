# R Basics #2 Answer

## Q1

Use a for loop to take the square root of each value in the following vector: `vec1 <- c(4, 9, 81, 100, 1000, 10^6)`. Save the results to a new vector called `vec2`.

**Answer:**

```r
vec1 <- c(4, 9, 81, 100, 1000, 10^6)
vec2 <- rep(NA,length(vec1))
for (i in 1:length(vec1)){
  vec2[i]<-sqrt(vec1[i])
}

vec2
[1]    2.00000    3.00000    9.00000   10.00000   31.62278 1000.00000
```

## Q2

Monte Carlo Simulation: Imagine that the values in the vector `pop` below represent vote shares for a presidential candidate across the  3,144 counties in the United States. If we were to take a sample of 50  counties and estimate mean support for the presidential candidate, would we, on average, estimate the vote share across all counties accurately? (Don’t worry about the fact that we really should be weighing counties  by their population size to estimate overall support.) Draw 10,000  samples of 50 counties from `pop` and estimate mean support for each sample, saving each mean estimate into a vector called `smpl_means`. How does the mean of the sample means compare to the population mean?  Do we, on average, do a good job of estimating the population mean?

> `pop <- runif(n = 3144, min = 0, max = 1)`

**Answer:**

```r
pop <- runif(n = 3144, min = 0, max = 1)

mean(pop) # population mean
[1] 0.5052021

n <- 10000
smpl_means <- rep(NA, n)
for(i in 1:n){
  smpl <- sample(pop, 50)
  smpl_means[i] <- mean(smpl)
}

mean(smpl_means)
[1] 0.5051876
```
