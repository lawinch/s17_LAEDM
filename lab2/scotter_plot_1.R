# Method:         Scotter plot
# Data Variables: Ordinal values for both x and y
# Author:         Dilyara Galieva

# the eruption durations
duration = faithful$eruptions

# the waiting interval
waiting = faithful$waiting

# plot the variables
plot(duration,
     waiting,
     col=brewer.pal(name="RdBu",n=4),
     xlab="Eruption duration",
     ylab="Time waited")

# plotting the median
abline(lm(waiting ~ duration),col=c("red"))
