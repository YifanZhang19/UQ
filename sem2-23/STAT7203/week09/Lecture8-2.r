## ------------------------------------
library("rstudioapi")    
setwd(dirname(getActiveDocumentContext()$path))       # Set working directory to source file location
rm(list=ls())
cat("\f")
graphics.off()
library(lattice)
## ------------------------------------

MRT = read.csv('MRT.csv')

# Summary statistics
table(MRT$Group)
aggregate(Change ~ Group, data=MRT, mean)
aggregate(Change ~ Group, data=MRT, sd)

qqmath(~Change, groups=Group, data=MRT, auto.key=TRUE)
bwplot(Change~Group, data=MRT)

# The test statistic for testing H0: mu = 0 against H1: mu > 0 is
testStat = (3.94 - 0)/(4.72/sqrt(17))
testStat

# The resulting p-value is
1 - pt(testStat, df = 16)

# t-test as implemented in R
t.test(MRT$Change[18:34], alternative = 'greater')


MRT = read.csv('MRT.csv')
aggregate(Change~Group, data=MRT, mean)
aggregate(Change~Group, data=MRT, sd)
t.test(MRT$Change[1:17], MRT$Change[18:34], data=MRT, alternative='greater',var.equal = TRUE)
t.test(MRT$Change[1:17], MRT$Change[18:34], data=MRT, alternative='greater')





