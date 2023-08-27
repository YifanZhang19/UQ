## ------------------------------------
library("rstudioapi")    
setwd(dirname(getActiveDocumentContext()$path))       # Set working directory to source file location
rm(list=ls())
cat("\f")

# Set working directory to the folder where your data is stored.
# Go to the menu Session > Set Working Directory > Choose Directory
# Once the working directory is set we can read in the data.

MRT = read.csv("MRT.csv")
print(MRT)

# lattice library for plots
library(lattice)

# Plots of the change in MRT scores
stripplot(Change ~ Group, data=MRT)
stripplot(Change ~ Group, data=MRT,jitter=TRUE)

# Mean change in MRT
mean(MRT$Change[1:17])
mean(MRT$Change[18:34])

# Alternative way to compute mean change in MRT
aggregate(Change ~ Group, data=MRT, mean)

mean(MRT$Change[1:17]) - mean(MRT$Change[18:34])

# function to compute the mean difference
diff.mean = function(data){
  mean(data[1:17]) - mean(data[18:34])
}

diff.mean(MRT$Change)

# random permutations
1:6
sample(1:6)
sample(c('a','b','c','d'))

MRT$Change
sample(MRT$Change)


# mean difference of a permutation of the data
diff.mean(sample(MRT$Change))

replicate(100,diff.mean(sample(MRT$Change)))

replicate(100,diff.mean(sample(MRT$Change)) >= 2.4)

sum(replicate(10000,diff.mean(sample(MRT$Change))>=2.47))/10000



