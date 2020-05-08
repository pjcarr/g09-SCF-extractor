import matplotlib.pyplot as plt
import numpy as np

lggfile = open("d:/Desktop/Codes/B12H12_4C6H6F6_tet_opt.log","r")
logfile = lggfile.readlines()
lggfile.close()

scflines=[]

for x in logfile:
    if x[:10] == " SCF Done:":
        scflines.append([x])

scfstep = list(range(len(scflines)))

scfline_ext = []

for x in scflines[:]:
    scfline_ext.append(x[0])

scf_nrg = []

for x in scfline_ext[:]:
    scf_nrg.append(float(x.split(' ')[7]))

min_scfnrg = min(scf_nrg)
min_scf_step = np.argmin(scf_nrg)

count = 0

for x in logfile:
    if x[:8] == " NAtoms=":
        numatoms = int(x.split(" ")[4])
        break

geom = []

for x in logfile:
    count = count + 1
    if x == scfline_ext[min_scf_step]:
        geom = logfile[count+8:count+8+numatoms]

for x in geom:
    print(x.strip("\n"))

plt.figure()
plt.plot(scfstep,scf_nrg)
plt.show()