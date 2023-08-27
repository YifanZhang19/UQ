library(lattice)
data <- read.csv("/Users/meviusz/UQ/sem2-23/STAT7203/ass1/CloudSeedingData.csv")
stacked <- stack(data)
stacked
bwplot(values ~ ind, data = stacked,
       main = "Boxplot of Rainfall for Seeded and Unseeded Clouds",
       xlab = "Experiment Type", ylab = "Rainfall Measurements")

n <- 10
x1 <- 2
x2 <- 5
x3 <- 3
p1 <- 1/4
p2 <- 1/2
p3 <- 1/4

probability <- (factorial(n) / (factorial(x1) * factorial(x2) * factorial(x3))) * (p1^x1) * (p2^x2) * (p3^x3)

probability

# Number of simulations
num_simulations <- 100000

# Initialize counters for part (a) and (b)
count_part_b <- 0



count <- 0

for (i in 1:100000) {
  box_number <- sample(c(1, 2, 3), 10, replace = TRUE, prob = c(1/4, 1/2, 1/4))
  if (sum(box_number == 1) == 2 && sum(box_number == 2) == 5 && sum(box_number == 3) == 3) {
    count <- count + 1
  }
}

probability <- count / 100000
cat("Simulated Probability:", probability, "\n")




# Number of simulations
num_simulations <- 100000
  # Check if it meets the conditions for part (b)
  if (sum(box_assignments == 1) == 0) {
    count_part_b <- count_part_b + 1
  }
}
# Calculate probabilities
probability_part_b <- count_part_b / num_simulations

# Print results
cat("Probability for part (a):", probability_part_a, "\n")
cat("Probability for part (b):", probability_part_b, "\n")


pdf <- function(x) {
  exp(-x) / (1 + exp(-x))^2
}

x_values <- seq(-5, 5, length.out = 1000)
y_values <- pdf(x_values)
plot(x_values, y_values, type = "l", col = "purple", lwd = 2,
     main = "PDF", xlab = "x", ylab = "y")

count <- 0

for (i in 1:100000) {
  box_number <- sample(c(1, 2, 3), 10, replace = TRUE, prob = c(1/4, 1/2, 1/4))
  if (sum(box_number == 1) == 0) {
    count <- count + 1
  }
}

probability <- count / 100000
cat("Simulated Probability:", probability, "\n")





