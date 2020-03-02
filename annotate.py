f2 = open("C:/Users/varsha/Downloads/sample_files-2(3)/sample_files-2/annotate/coordinates_to_annotate.txt",'r')
f1 = open("C:/Users/varsha/Downloads/sample_files-2(3)/sample_files-2/gtf/hg19_annotations.gtf",'r')
d = {}
while True:
    line = f1.readline()
    if not line:
        break
    c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17 = line.split()
    d[(c0,c3)] = (c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17)
while True:
    line = f2.readline()
    if not line:
        break
    c0,c1 = line.split()
    if (c0,c1) in d:
        vals = d[(c0,c1)]
        print (c0,c1,vals[1],vals[2],vals[3],vals[4],vals[5],vals[6],vals[7],vals[8],vals[9],vals[10],vals[11],vals[12],vals[13],vals[14],vals[15],vals[16],vals[17])