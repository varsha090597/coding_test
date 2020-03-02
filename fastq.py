import glob

reads = 0
bases = []
count=0


path = "C:/Users/varsha/Downloads/sample_files-2(3)/sample_files-2/fastq/"

files = [f for f in glob.glob(path + "read*/*.fastq", recursive=True)]

for f in files:
    print(f)
    read = open(f, 'rb')
    for id in read:
        seq = next(read)
        reads += 1
        bases.append(len(seq.strip())) 
        #next(read)
        #next(read)
    
    for element in bases:
        if element > 30:
            count +=1
           
    print("no of reads greater than 30nt =",count)
  
    print("total reads =", reads)
    
    percent=(count/reads)*100
    print("percentage of sequences greater than 30 nt =",percent)
    count=0
    reads=0
    bases.clear()
