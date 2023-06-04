

figure
errorbar(mid(input_int), rad(input_int), "b")
title("Data")
xlabel("n")
ylabel("mV")
xlim([0, size(input, 1)])

print -dpdfcrop ../figures/data_int.png

