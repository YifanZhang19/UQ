## ------------------------------------
library("rstudioapi")    
setwd(dirname(getActiveDocumentContext()$path))       # Set working directory to source file location
rm(list=ls())
cat("\f")
graphics.off()
library(lattice)
library(plotrix)

# Survey data from Lecture 1-2
survey = read.csv("../../../notes/data/Survey2021.csv")
histogram(survey$Height)
qqmath(survey$Height)

# Construct a 95% confidence interval for population mean height from a 
# sample of 20 students.
data = sample(survey$Height, 20)
t.test(data)

# Did it cover the population mean?
PopMean = mean(survey$Height)
PopMean


# How often do these confidence intervals cover the population mean height?
m = 100
means = rep(0,m)
limits = matrix(0, nrow=m, ncol=2)
for (i in 1:m){
  data = sample(survey$Height, 20)  # Take a sample of size 20
  means[i] = mean(data)   # compute the sample mean for plottting later
  limits[i,] = t.test(data)$conf.int[1:2] # Extracts the confidence interval from t.test
}

# Identify which of these intervals did not cover the population mean height.
colours = rep(4,m)
colours[limits[,2] < PopMean] = 2
colours[limits[,1] > PopMean] = 2

# Plot of confidence intervals. Red intervals do not cover the population mean.
plotCI(1:m, means, ui = limits[,2], li = limits[,1],ylim=c(160,190), pch=21, pt.bg=par("bg"),sfrac=0, scol=colours, main='Confidence intervals for mean height (cm), n=20', xlab="", ylab="")
lines(1:m, rep(PopMean,m))


