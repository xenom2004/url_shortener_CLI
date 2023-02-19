import pickle
a={'www.google.com':'jinji'}
with open('bin_file.bin','wb') as f:
    pickle.dump(a,f)    
