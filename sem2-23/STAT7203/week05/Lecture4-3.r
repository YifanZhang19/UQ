## ------------------------------------
library("rstudioapi")    
setwd(dirname(getActiveDocumentContext()$path))       # Set working directory to source file location
rm(list=ls())
cat("\f")
graphics.off()
library(lattice)
library(manipulate)



# Plot of exponential density for various values of lambda
x=seq(from=0,to=2.5,length=100)
manipulate(
  xyplot(dexp(x,rate=lambda)~x,type='l',ylab='density',lwd=2, ylim=c(0,5)), 
  lambda=slider(min=0.1,max=5, initial=1, step=0.1)
)

1-pexp(2,rate=seq(from=0.01,to=5,length=10))


# Plot of P(X > x) for an Exp(lambda) distribution
manipulate(
  xyplot(1-pexp(x,rate=lambda)~x,type='l',ylab=expression(P(X>x)),lwd=2, ylim=c(0,1.2)), 
  lambda=slider(min=0.1,max=5, initial=1, step=0.1)
)

# Simulating exponential random variables with mean 3
Y = rexp(10000,rate=1/3)
histogram(Y,type='density',breaks=50)

# a more elaborate plot
y = seq(from = 0, to = 20, length=100)
histogram(~ Y, 
          type = "density", breaks=50,
          panel=function(x, ...) {
            panel.histogram(x, ...)
            panel.lines(dexp(y,rate=1/3)~y,lwd=2,col=2)
          })

# Simulating exponential random variables using the inverse transform

W = qexp(runif(10000),rate=1/3)
histogram(~ W, 
          type = "density", breaks=50,
          panel=function(x, ...) {
            panel.histogram(x, ...)
            panel.lines(dexp(y,rate=1/3)~y,lwd=2,col=2)
          })

