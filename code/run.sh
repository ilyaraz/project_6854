#!/opt/local/bin/zsh

./gen_random.py 900 4 > input.txt
octave --silent laplacian.m
mv output.txt random.txt
./gen_grid.py 30 30 > input.txt
octave --silent laplacian.m
mv output.txt grid.txt
R --no-save <plot.r
