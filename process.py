rm 1_*
rm 21_*
head *error.txt >> info_gg_unpaired.txt
source /mnt/common/epfl/etc/bbcf_bashrc ### para llamar a todos los programas de bbcf
module add UHTS/Analysis/samtools/1.2;
python -c "from bbcflib import mapseq"
for i in {2..48}
do
  	add_nh_flag "$i"_16S_gg.sam "$i"_SE_gg.bam
    samtools sort "$i"_SE_gg.bam "$i"_SE_gg_s
    samtools view -F0x4 $i"_SE_gg_s.bam | cut -f 3 | uniq -c >> "$i"_counts.txt
done
