data_random = read.table("random.txt")
data_grid = read.table("grid.txt")

pdf("plot.pdf")
plot(data_random, type = "l", col = "red")
lines(data_grid, col = "blue")
dev.off()

