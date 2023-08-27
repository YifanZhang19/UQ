## ------------------------------------
library("rstudioapi")    
setwd(dirname(getActiveDocumentContext()$path))       # Set working directory to source file location
rm(list=ls())
cat("\f")
graphics.off()
## ------------------------------------

monty <- function(switch=F) {
  doors = sample(c('Cookie', 'empty', 'empty'), 3)
  pick = sample(1:3, 1)
  
  if (switch) {
    # if you switch after Monty showed you a "empty" behind the other two doors,
    # you win if the "Cookie" is not behind the door you initially picked.
    doors[pick] != 'Cookie'
  } else {
    # if you aredo not switch after Monty showed you a "empty" behind the other two doors,
    # you win if the "Cookie" is indeed behind the door you initially picked.
    doors[pick] == 'Cookie'
  }
}
monty()
replicate(10, monty())
replicate(10, monty(switch=T))

no_switch = replicate(1000, monty())
switch = replicate(1000, monty(switch=T))

c(mean(no_switch), mean(switch))

