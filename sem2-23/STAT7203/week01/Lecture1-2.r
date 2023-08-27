## ------------------------------------
library("rstudioapi")    
setwd(dirname(getActiveDocumentContext()$path))       # Set working directory to source file location
rm(list=ls())
cat("\f")

# remember to set working directory
survey = read.csv("/Users/meviusz/UQ/sem2-23/STAT7203/Survey2021.csv")
head(survey)
names(survey)
str(survey)

## Summarising and visualising categorical data

# One-way table and barplot
unique(survey$Superpower)
table(survey$Superpower)
prop.table(table(survey$Superpower))
sum(prop.table(table(survey$Superpower)))

# Two-way table and barplot
table(survey$Superpower,survey$Eyes)
prop.table(table(survey$Superpower,survey$Eyes),margin=1) # 
myTable = prop.table(table(survey$Superpower,survey$Eyes),margin=1)
sum(myTable[1,])
sum(myTable[2,])
sum(myTable[,2])
myTable = prop.table(table(survey$Superpower,survey$Eyes),margin=2)
print(myTable)
sum(myTable[,2])
sum(myTable[2,])


# visualising categorical variable - one variable
barplot(table(survey$Superpower))
library(lattice)
barchart(table(survey$Superpower))

# visualising categorical variable - Two variable
barplot(table(survey$Superpower,survey$Eyes),legend=T)
barchart(table(survey$Eyes,survey$Superpower),auto.key=TRUE)


## Summarising quantitative data

# Summary statistics
mean(c(10,12,30,40,50))
mean(c(10,12,30,40,50,400))

median(c(10,12,30,40,50))
median(c(10,12,30,40,50,400))

mean(survey$Exercise)
var(survey$Exercise)
sd(survey$Exercise)


##
vals = sort(sample(1:100,11,replace = T))
print(vals)
quantile(vals)
quantile(vals,type=6)
quantile(vals,probs = c(1/8,7/8))
quantile(vals,probs = c(1/8,7/8), type = 6)
summary(vals)
summary(vals,quantile.type = 6)
IQR(vals)
IQR(vals,type = 6)






