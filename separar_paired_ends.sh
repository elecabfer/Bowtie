#separar paired-reads:
file= '4_S19_L001_paired_intervealed_derep_6sub.fq'
out1= open('4_paired_N1.fq', 'w')
out2= open('4_paired_N2.fq', 'w')
inp  = open(file, 'r').read()
read=inp.split('@M01072')
for i in read:
        if '1:N:0:' in i:
                out1.write('@M01072'+i)
        if '2:N:0:' in i:
                out2.write('@M01072'+i)
