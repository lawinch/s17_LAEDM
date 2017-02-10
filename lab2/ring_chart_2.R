# Method:         Ring chart
# Data Variables: numbers
# Author:         Dilyara Galieva
# install ggplot2 for ring chart visualization
install.packages("ggplot2")
library(ggplot2)

# data import
Data <- read.table(url("http://assets.datacamp.com/blog_assets/chol.txt"), header=TRUE)

# creating a dataframe
data_ring = data.frame(count =c(30, 10, 50), category = c("30 y.o.", "10 y.o.", "50 y.o"))

# Adding additional columns, needed for drawing geom_rect
data_ring$fraction = data_ring$count / sum(data_ring$count)
data_ring = data_ring[order(data_ring$fraction), ]
data_ring$ymax = cumsum(data_ring$fraction)
data_ring$ymin = c(0, head(data_ring$ymax, n=-1))

# Make the plot
plot = ggplot(data_ring, aes(fill = category, ymax = ymax, ymin = ymin, xmax = 4, xmin = 3 )) +
       geom_rect() +
       coord_polar(theta="y") +
       xlim(c(0, 4)) +
       theme(panel.grid=element_blank()) +
       theme(axis.text=element_blank()) +
       theme(axis.ticks=element_blank()) +
       annotate("text", x=0, y=0, label = "Ages of the passengers") +
       labs(title="")

# showing the plot
plot

