## ------------------------------------
library("rstudioapi")    
setwd(dirname(getActiveDocumentContext()$path))       # Set working directory to source file location
rm(list=ls())
cat("\f")
library(lattice)

# remember to set working directory
survey = read.csv("/Users/meviusz/UQ/sem2-23/STAT7203/Survey2021.csv")

#Boxplot
bwplot(~Forearm,data=survey)

bwplot(Superpower~Mass,data=survey, ylab = 'Mass', xlab = 'Superpower')


# Skewness
bwplot(~Exercise,data=survey)
bwplot(Handed~Exercise,data=survey)



#Histogram
# histogram
histogram(~Height, data=survey)
histogram(~Height, data=survey, nint=9)
histogram(~Height, data=survey, nint=10)
histogram(~Height, data=survey, nint=11)
histogram(~Height, data=survey, breaks=seq(120,240,by=5))
histogram(~Height | Handed,data=survey)
histogram(~Height | Superpower,data=survey)

# density plot
densityplot(~Height, data=survey)
densityplot(~Height, data=survey, bw=0.1)
densityplot(~Height, data=survey, bw=0.3)
densityplot(~Height, data=survey, bw=3)
densityplot(~Height, data=survey, bw=10)
densityplot(~Height, groups=Handed, data=survey, auto.key=TRUE)

# stripplots
stripplot(~Height,data=survey)
stripplot(~Height,data=survey,jitter=TRUE, factor = 3)
stripplot(Handed~Height,data=survey,jitter=TRUE)

# scatter plot
plot(survey$Mass ~ survey$Height,type='p',xlab = 'Height', ylab = 'Mass')
xyplot(Mass ~ Height, data=survey, type='p')
xyplot(Mass ~ Height, data=survey, type=c('p','smooth'))
xyplot(Mass ~ Height, data=survey, type=c('p','smooth'),lwd=2,col.line='red')
xyplot(Mass ~ Height, data=survey, type=c('p','r'),lwd=2,col.line='red')
xyplot(Mass ~ Height | Superpower, data=survey, type=c('p','r'),lwd=2,col.line='red')


# Quantile-Quantile plot

# Comparing the distribution of a variable with a given model
qqmath(~Height,data=survey,dist=qnorm) # comparing with a normal distribution
qqnorm(survey$Height); qqline(survey$Height,col=2) # A similar command but draws a line through the plot
histogram(~Height, data=survey,nint = 15)

qqmath(~Height,data=survey,dist=qunif) # comparing a the uniform distribution

qqmath(~Mass,data=survey,dist=qnorm)
qqnorm(survey$Mass); qqline(survey$Mass,col=2)
histogram(~Mass, data=survey,nint = 15)

qqmath(~Mass|Handed,data=survey,dist=qnorm)
qqmath(~Mass, groups=Handed,data=survey,dist=qnorm,auto.key = TRUE)
histogram(~Mass, data=subset(survey,survey$Handed == "Right"))
histogram(~Mass, data=subset(survey,survey$Handed == "Left"))

# Comparing the distribution of of two variables
qq(Handed~Mass,data=survey,type = c("p", "g"))
histogram(~Mass | Handed, data=survey)





