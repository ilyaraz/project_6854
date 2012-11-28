input = fopen('input.txt');
n = fscanf(input, '%d', 1);
m = fscanf(input, '%d', 1);
l = zeros(n, n);
id = eye(n);
for i = 1 : m
    a = fscanf(input, '%d', 1);
    b = fscanf(input, '%d', 1);
    u = id(:,a) - id(:,b);
    l = l + u * u';
end
d = eig(l);
output = fopen('output.txt', 'w');
for i = 1 : n
    fprintf(output, '%.20f %.20f\n', d(i), i / n);
end
fclose(output);
