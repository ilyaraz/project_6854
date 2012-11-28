data_random = read.table("random.txt")
data_grid = read.table("grid.txt")
data_trees = read.table("trees.txt")

pdf("plot.pdf")
plot(data_trees, type = "l", col = "red")
lines(data_random, col = "blue")
lines(data_grid, col = "green")

