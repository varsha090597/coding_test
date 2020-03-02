from collections import Counter 

with open('C:/Users/varsha/Downloads/sample_files-2(3)/sample_files-2/fasta/sample.fasta') as f:
    mylist = [line.rstrip('\n') for line in f]
    
Counter = Counter(mylist) 
  
 
most_occur = Counter.most_common(4) 
  
print(most_occur)