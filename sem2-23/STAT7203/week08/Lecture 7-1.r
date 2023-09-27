## ------------------------------------
library("rstudioapi")    
setwd(dirname(getActiveDocumentContext()$path))       # Set working directory to source file location
rm(list=ls())
cat("\f")
graphics.off()
## ------------------------------------

## Law of Large Numbers
coin = c(0,1)

sample(coin,size = 10,replace = TRUE, prob = c(0.4,0.6))

?cumsum

cumsum(sample(coin,size = 10,replace = TRUE, prob = c(0.4,0.6)))

cumsum(sample(coin,size = 10,replace = TRUE, prob = c(0.4,0.6))) / 1:10

N = 1000
cumsum(sample(coin,size = N,replace = TRUE, prob = c(0.4,0.6))) / 1:N

plot(cumsum(sample(coin,size = N,replace = TRUE, prob = c(0.4,0.6))) / 1:N, type ='l')
