## ------------------------------------
library("rstudioapi")    
setwd(dirname(getActiveDocumentContext()$path))       # Set working directory to source file location
rm(list=ls())
cat("\f")
library(lattice)

# geyser
?faithful
str(faithful)
qqmath(~eruptions, data=faithful,dist=qunif)
qqmath(~eruptions, data=faithful,dist=qnorm)

# How would you interpret this? One clump of values around 2 and another around
# 4.5. very few values around 3.
histogram(~eruptions, data=faithful)
bwplot(~eruptions, data=faithful)


# survey data
## ------------------------------------
library(lattice)
# remember to set working directory
survey = read.csv("../../../notes/data/Survey2021.csv")
table(survey$Handed,survey$Eyes)
addmargins(table(survey$Handed,survey$Eyes))

prop.table(table(survey$Handed,survey$Eyes))
prop.table(table(survey$Handed,survey$Eyes),margin=2)
