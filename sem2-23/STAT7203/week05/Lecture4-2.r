## ------------------------------------
library("rstudioapi")    
setwd(dirname(getActiveDocumentContext()$path))       # Set working directory to source file location
rm(list=ls())
cat("\f")
graphics.off()
library(lattice)
library(manipulate)

# The function dbinom computes the pmf of the Binomial distribution
n=10
p=0.7
x = 0:n
pmf = dbinom(x,size=n,prob=p)
barplot(pmf,names.arg=x,xlab="x", ylab="P(X=x)", main="PMF for Binomial (n=10, p=0.7)")

manipulate(
  barplot(dbinom(x,size=n,prob=p),names.arg=x,xlab="x", ylab="P(X=x)", main="PMF for Binomial (n=10, p)"), 
  p=slider(min=0,max=1, initial=0, step=0.1)
)

# Suppose 70 percent of all students live at home. If we take a random sample of 
# 5 students, what is the probability that exactly 3 of them live at home? 
dbinom(3,5,0.7)

# The function pbinom computes the cdf of the Binomial distribution
cdf = pbinom(x,size=n,prob=p)
barplot(cdf,names.arg=x,xlab="x", ylab= expression(P(X<=x)), main="CDF for Binomial (n=10, p=0.7)")
manipulate(
  barplot(pbinom(x,size=n,prob=p),names.arg=x,xlab="x", ylab= expression(P(X<=x)), main="CDF for Binomial (n=10, p)")
  , 
  p=slider(min=0,max=1, initial=0, step=0.1)
)

# Suppose 70 percent of all students live at home. If we take a random sample of 
# 5 students, what is the probability that no more than 3 of them live at home? 
pbinom(3,5,0.7)
sum(dbinom(0:3,5,0.7))

# Suppose 70 percent of all students live at home. If we take a random sample of 
# 5 students, what is the probability that at least 3 of them live at home? 
1 - pbinom(2,5,0.7)
1-sum(dbinom(0:2,5,0.7))
sum(dbinom(3:5,5,0.7))

# The function rbinom simulates random variables from a Binomial distribution
rbinom(10,size=10,prob=0.7)

mean(rbinom(10000,size=10,prob=0.7))
10*0.7

var(rbinom(10000,size=10,prob=0.7))
10*0.7*(1-0.7)

rbinom(100,size=10,prob=0.7)
table(rbinom(1000,size=10,prob=0.7))
barplot(table(rbinom(1000,size=10,prob=0.7))/1000)


# Vinny's experiment
1 - pbinom(20,size = 30,prob = 0.5)
sum(dbinom(21:30,size = 30,prob = 1/2))

# The functions dpois, ppois, and rpois are the corresponding functions for 
# the Poisson distribution

dpois(2,lambda=3)
3^2*exp(-3)/factorial(2)

ppois(3,lambda=3)
sum(dpois(0:3,lambda=3))

rpois(100,5)
table(rpois(10000,5))
barplot(table(rpois(10000,5))/10000)

x = 0:100
pmf = dpois(x,lambda=5)
barplot(pmf,names.arg=x,xlab="x", ylab="P(X=x)", main="PMF for Poisson (lambda=5)")

manipulate(
  barplot(dpois(x,lambda),names.arg=x,xlab="x", ylab="P(X=x)"), 
  lambda=slider(min=0.1,max=100, initial=0.1, step=1)
)
