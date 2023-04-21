import numpy as np
import distrs

import os

def calc_quart(arr, p):
    new_arr = np.sort(arr)
    k = len(arr) * p
    if k.is_integer():
        return new_arr[int(k)]
    else:
        return new_arr[int(k) + 1]

def calc_z_q(arr):
    return (calc_quart(arr, 0.25) + calc_quart(arr, 0.75)) / 2

def calc_z_tr(arr):
    r = int(len(arr) * 0.25)
    new_arr = np.sort(arr)
    sum = 0
    for i in range(r + 1, len(arr) - r):
        sum += new_arr[i]
    return sum / (len(arr) - 2 * r)

def task2():
    repeats = 1000
    sizes = [10, 100, 1000]
    if not os.path.isdir("task2_tables"):
      os.makedirs("task2_tables")
    for name in distrs.distr_names:
        rows = []
        for N in sizes:
            mean = []
            med = []
            z_r = []
            z_q = []
            z_tr = []
            for rep in range(0, repeats):
                arr = distrs.get_distr(name, N)
                arr_sorted = np.sort(arr)
                mean.append(np.mean(arr))
                med.append(np.median(arr))
                z_r.append((arr_sorted[0] + arr_sorted[-1]) / 2)
                z_q.append(calc_z_q(arr))
                z_tr.append(calc_z_tr(arr))
            rows.append(["n =" + str(N)])

            div1=np.around(
                (np.around(np.mean(mean), decimals=4) - np.sqrt(
                np.around(np.mean(np.multiply(mean, mean)) - np.mean(mean) * np.mean(mean), decimals=4))), decimals=4)
            div2=np.around(
                ( np.around(np.mean(med), decimals=4) 
                - np.sqrt(
                np.around(np.mean(np.multiply(med, med)) - np.mean(med) * np.mean(med), decimals=4)
                )), decimals=4)
            div3=np.around(
                (np.around(np.mean(z_r), decimals=4) 
                - np.sqrt(
                np.around(np.mean(np.multiply(z_r, z_r)) - np.mean(z_r) * np.mean(z_r), decimals=4)
                )), decimals=4)
            div4=np.around(
                ( np.around(np.mean(z_q), decimals=4) 
                - np.sqrt(
                np.around(np.mean(np.multiply(z_q, z_q)) - np.mean(z_q) * np.mean(z_q), decimals=4)
                  )), decimals=4)
            div5=np.around(
                ( np.around(np.mean(z_tr), decimals=4) 
                - np.sqrt(
                np.around(np.mean(np.multiply(z_tr, z_tr)) - np.mean(z_tr) * np.mean(z_tr), decimals=4)
                )), decimals=4)
            

            sum1=np.around(
                (np.around(np.mean(mean), decimals=4) + np.sqrt(
                np.around(np.mean(np.multiply(mean, mean)) - np.mean(mean) * np.mean(mean), decimals=4))), decimals=4)
            sum2=np.around(
                ( np.around(np.mean(med), decimals=4) 
                + np.sqrt(
                np.around(np.mean(np.multiply(med, med)) - np.mean(med) * np.mean(med), decimals=4)
                )), decimals=4)
            sum3=np.around(
                (np.around(np.mean(z_r), decimals=4) 
                + np.sqrt(
                np.around(np.mean(np.multiply(z_r, z_r)) - np.mean(z_r) * np.mean(z_r), decimals=4)
                )), decimals=4)
            sum4=np.around(
                ( np.around(np.mean(z_q), decimals=4) 
                + np.sqrt(
                np.around(np.mean(np.multiply(z_q, z_q)) - np.mean(z_q) * np.mean(z_q), decimals=4)
                  )), decimals=4)
            sum5=np.around(
                ( np.around(np.mean(z_tr), decimals=4) 
                + np.sqrt(
                np.around(np.mean(np.multiply(z_tr, z_tr)) - np.mean(z_tr) * np.mean(z_tr), decimals=4)
                )), decimals=4)





            rows.append(["$E(z) \\, $",
                        np.around(np.mean(mean), decimals=4),
                        np.around(np.mean(med), decimals=4),
                        np.around(np.mean(z_r), decimals=4),
                        np.around(np.mean(z_q), decimals=4),
                        np.around(np.mean(z_tr), decimals=4),
                        ])
            rows.append(["$D(z) \\, $",
                        np.around(np.mean(np.multiply(mean, mean)) - np.mean(mean) * np.mean(mean), decimals=4),
                        np.around(np.mean(np.multiply(med, med)) - np.mean(med) * np.mean(med), decimals=4),
                        np.around(np.mean(np.multiply(z_r, z_r)) - np.mean(z_r) * np.mean(z_r), decimals=4),
                        np.around(np.mean(np.multiply(z_q, z_q)) - np.mean(z_q) * np.mean(z_q), decimals=4),
                        np.around(np.mean(np.multiply(z_tr, z_tr)) - np.mean(z_tr) * np.mean(z_tr), decimals=4),
                        ])
            rows.append(["$E(z)-\sqrt(D(z)) \\, $", div1, div2, div3, div4, div5 ])
            rows.append(["$E(z)+\sqrt(D(z)) \\, $", sum1, sum2, sum3, sum4, sum5 ])
            
        with open("task2_tables/" + name + ".tex", "w") as f:
            f.write("\\begin{tabular}{|c|c|c|c|c|c|}\n")
            f.write("\\hline\n")
            f.write(" & $\\bar{x} \\, $ & $med \\, x \\, $ & $z_R \\, $ & $z_Q \\, $ & $z_{tr} \\, $ \\\\\n")
            f.write("\\hline\n")
            for row in rows:
                if len(row) == 1:
                    f.write(row[0] + " & " * 5 + "\\\\\n")
                else:
                    f.write(" & ".join([str(i) for i in row]) + "\\\\\n")
                f.write("\\hline\n")
            f.write("\\end{tabular}")

if __name__ == "__main__":
    task2()