## ------------------------------------
library("rstudioapi")    
setwd(dirname(getActiveDocumentContext()$path))       # Set working directory to source file location
rm(list=ls())
cat("\f")
graphics.off()
library(lattice)
library(plotrix)

# T statistic for n = 4
n = 4
m = 10000
Tstat4 = rep(0,m)
for (i in 1:m){
  sampleData = rnorm(n)
  Tstat4[i] = mean(sampleData)/(sd(sampleData)/sqrt(n))
}

histogram(Tstat4,nint=100, type="density",ylim=c(0,0.45))
x = seq(from=-10, to=10, length=100)
trellis.focus("panel",1,1,highlight = FALSE)
llines(x,dt(x,df=n-1), lwd=2,col='red')
llines(x,dnorm(x), lwd=2,col='blue')
trellis.unfocus()

# T statistic for n = 8
n = 8
m = 10000
Tstat8 = rep(0,m)
for (i in 1:m){
  sampleData = rnorm(n)
  Tstat8[i] = mean(sampleData)/(sd(sampleData)/sqrt(n))
}

histogram(Tstat8,nint=100, type="density",ylim=c(0,0.45))
x = seq(from=-10, to=10, length=100)
trellis.focus("panel",1,1,highlight = FALSE)
llines(x,dt(x,df=n-1), lwd=2,col='red')
llines(x,dnorm(x), lwd=2,col='blue')
trellis.unfocus()

# T statistic for n = 100
n = 100
m = 10000
Tstat100 = rep(0,m)
for (i in 1:m){
  sampleData = rnorm(n)
  Tstat100[i] = mean(sampleData)/(sd(sampleData)/sqrt(n))
}

histogram(Tstat100,nint=100, type="density",ylim=c(0,0.45))
x = seq(from=-10, to=10, length=100)
trellis.focus("panel",1,1,highlight = FALSE)
llines(x,dt(x,df=n-1), lwd=2,col='red')
llines(x,dnorm(x), lwd=2,col='blue')
trellis.unfocus()

# Student's t has heavier tails than standard normal
tSamples = rt(n = 1000,df = 3)
qqmath(tSamples,dist = qnorm)
