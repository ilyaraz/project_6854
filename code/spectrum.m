#!/opt/local/bin/octave --silent

input = fopen('input.txt');
n = fscanf(input, '%d', 1);
d = fscanf(input, '%d', 1);
l = zeros(n, n);
for i = 1 : n
    for j = 1 : d
        t = fscanf(input, '%d', 1);
        l(i, t) = l(i, t) + 1.0 / d;
    end
end
disp(poly(l));
d = eig(l);
output = fopen('output.txt', 'w');
for i = 1 : n
    fprintf(output, '%.20f\n', d(i));
end
fclose(output);
