data_random = read.table("random.txt")
data_grid = read.table("grid.txt")

pdf("plot.pdf")
plot(data_grid, type = "l", col = "red")
lines(data_random, col = "blue")
dev.off()

