# gene_cleaner
small script to extract unique PValue data  

# DATA EXAMPLE 
transcript_id;log2FC_pe_soltub;PValue_pe_soltub;FDR_pe_soltub;Inf_pe_soltub_Mean_TPM;Ctrl_pe_soltub_Mean_TPM;annotation
Soltu.DM.01G000780.1;-2,52;0,001071851;0,005584416;0,57;5,29;Dynein light chain type 1 family protein
Soltu.DM.12G025280.1;-1,08;0,011119733;0,037359114;2,18;7,63;golgin candidate
Soltu.DM.12G025460.1;1,09;0,007499678;0,027292643;17,6;14,82;Protein kinase family protein with leucine-rich repeat domain
Soltu.DM.12G025530.1;-2,17;0,000771668;0,004249862;0,86;6,82;O-Glycosyl hydrolases family 17 protein
Soltu.DM.12G025540.1;1,16;0,003878686;0,016146989;637,4;409,83;profilin
Soltu.DM.12G025560.1;-4,14;0,000709194;0,00396254;0,61;19,77;Protein of unknown function (DUF1005)
Soltu.DM.12G025600.1;1,44;0,000191619;0,001300112;75,25;47,06;Insulinase (Peptidase family M16) protein
Soltu.DM.12G025620.1;6,49;2,70409E-13;1,76409E-11;481,34;9,48;myo-inositol oxygenase
Soltu.DM.12G025620.2;5,93;3,38327E-09;8,39918E-08;4,26;0,13;myo-inositol oxygenase
Soltu.DM.12G025620.3;4,2;6,99067E-09;1,60698E-07;8,62;0,86;myo-inositol oxygenase
Soltu.DM.12G025620.4;7,91;0,000173744;0,001197113;89,59;0,78;myo-inositol oxygenase
Soltu.DM.12G025620.5;5,93;3,38327E-09;8,39918E-08;4,26;0,13;myo-inositol oxygenase
Soltu.DM.12G025640.1;3,74;0,000226565;0,001501631;4,14;0,57;myb domain protein
Soltu.DM.01G001340.1;-1,54;0,000526622;0,003077218;2,79;13,57;MAK16 protein-related
Soltu.DM.01G001340.2;-1,54;0,000526622;0,003077218;2,79;13,57;MAK16 protein-related
Soltu.DM.01G001340.3;-1,54;0,000526622;0,003077218;2,79;13,57;MAK16 protein-related

# ACCEPED DATA EXAMPLE

,transcript_id,log2FC_pe_soltub,PValue_pe_soltub,FDR_pe_soltub,Inf_pe_soltub_Mean_TPM,Ctrl_pe_soltub_Mean_TPM,annotation
23,Soltu.DM.12G025560.1,"-4,14","0,000709194","0,00396254","0,61","19,77",Protein of unknown function (DUF1005)
24,Soltu.DM.12G025600.1,"1,44","0,000191619","0,001300112","75,25","47,06",Insulinase (Peptidase family M16) protein
25,Soltu.DM.12G025620.1,"6,49","2,70409E-13","1,76409E-11","481,34","9,48",myo-inositol oxygenase
26,Soltu.DM.12G025620.2,"5,93","3,38327E-09","8,39918E-08","4,26","0,13",myo-inositol oxygenase
27,Soltu.DM.12G025620.3,"4,2","6,99067E-09","1,60698E-07","8,62","0,86",myo-inositol oxygenase
28,Soltu.DM.12G025620.4,"7,91","0,000173744","0,001197113","89,59","0,78",myo-inositol oxygenase
29,Soltu.DM.12G025640.1,"3,74","0,000226565","0,001501631","4,14","0,57",myb domain protein
30,Soltu.DM.12G025650.1,"2,98","0,002920685","0,012819476","7,13","1,41",Mnd1 family protein
44,Soltu.DM.01G001330.1,"1,1","0,012064263","0,039943978","2,12","1,79",calmodulin-binding family protein
45,Soltu.DM.01G001340.1,"-1,54","0,000526622","0,003077218","2,79","13,57",MAK16 protein-related


# REJECTED DATA EXAMPLE

,transcript_id,log2FC_pe_soltub,PValue_pe_soltub,FDR_pe_soltub,Inf_pe_soltub_Mean_TPM,Ctrl_pe_soltub_Mean_TPM,annotation
4,Soltu.DM.01G000520.5,"-2,14","6,95855E-05","0,000540757","0,76","5,54",Ankyrin repeat family protein,"Duplicate PValue 6,95855E-05 for Gene ID: 01G000520"
5,Soltu.DM.12G025620.5,"5,93","3,38327E-09","8,39918E-08","4,26","0,13",myo-inositol oxygenase,"Duplicate PValue 3,38327E-09 for Gene ID: 12G025620"
6,Soltu.DM.01G001340.2,"-1,54","0,000526622","0,003077218","2,79","13,57",MAK16 protein-related,"Duplicate PValue 0,000526622 for Gene ID: 01G001340"
7,Soltu.DM.01G001340.3,"-1,54","0,000526622","0,003077218","2,79","13,57",MAK16 protein-related,"Duplicate PValue 0,000526622 for Gene ID: 01G001340"
