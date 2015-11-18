bsub bowtie2-build ncbi_bacterial_genomes2.fa 
for i in {4..11}
do
bsub -M 122999990 -o "$i"_16S_gg.txt -e "$i"_16S_gg_error.txt bowtie2 --local -x ../gg_13_5_idxbowtie -k 100 -p 8 -N 1 -q --phred33 -U "$i"_*_unpaired_derep.fq -S "$i"_16S_gg.sam
done
#get_info_gg
rm bowtie2_GreenGenes_info.txt
for i in {2..11}
do
        a="Granule "
        c=$a$i
        echo $c >> bowtie2_GreenGenes_info.txt
        cat "$i"*error.txt >> bowtie2_GreenGenes_info.txt
        echo $i
done

