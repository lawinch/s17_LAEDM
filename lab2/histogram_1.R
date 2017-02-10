# Method:         Histogram
# Data Variables: numbers
# Author:         Dilyara Galieva

# data import
Data <- read.table(url("http://assets.datacamp.com/blog_assets/chol.txt"), header=TRUE)


# installing package for colors
install.packages("RColorBrewer")
library(RColorBrewer)

# saving data into a variable
Age <- data[,1]

# plotting a histogram with three color palette
hist(Age,
      breaks = 30,
      col = brewer.pal(3,"Set3"),
      main = "Age of passengers")