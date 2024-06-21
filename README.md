# gene_cleaner
small script to extract unique PValue data  

# DATA EXAMPLE 
```
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
```
# ACCEPED DATA EXAMPLE
```
,transcript_id,log2FC_pe_soltub,PValue_pe_soltub,FDR_pe_soltub,Inf_pe_soltub_Mean_TPM,Ctrl_pe_soltub_Mean_TPM,annotation
0,Soltu.DM.01G000020.1,3.82,3.13714e-05,0.000267686,411.28,42.59,low-molecular-weight cysteine-rich
1,Soltu.DM.01G000090.1,-2.19,0.000303463,0.0019242,1.26,9.2,C2H2-like zinc finger protein
2,Soltu.DM.01G000120.1,-2.71,3.66813e-05,0.000308499,0.56,6.27,Microtubule associated protein (MAP65/ASE1) family protein
3,Soltu.DM.01G000160.1,-2.01,4.31761e-06,4.77513e-05,2.58,16.99,xyloglucan endotransglucosylase/hydrolase
4,Soltu.DM.01G000240.1,3.58,1.9439e-08,3.9946e-07,5.51,0.81,ARM repeat superfamily protein
5,Soltu.DM.01G000250.1,-2.41,0.000252041,0.001645512,0.06,0.52,ENTH/ANTH/VHS superfamily protein
6,Soltu.DM.01G000300.1,3.58,4.7682e-10,1.48217e-08,8.34,1.3,MAC/Perforin domain-containing protein
7,Soltu.DM.01G000470.1,-2.04,0.000151981,0.001067432,0.37,2.55,NB-ARC domain-containing disease resistance protein
8,Soltu.DM.01G000480.1,-2.6,0.000644452,0.003648261,0.14,1.44,NB-ARC domain-containing disease resistance protein
9,Soltu.DM.01G000500.1,-4.01,5.20694e-11,2.04992e-09,0.12,3.18,DYNAMIN-like 1C
10,Soltu.DM.01G000510.1,-1.61,0.014754323,0.046967777,1.39,6.79,microtubule-associated proteins 70-2
11,Soltu.DM.01G000520.1,-2.14,6.95855e-05,0.000540757,0.76,5.54,Ankyrin repeat family protein
12,Soltu.DM.01G000540.1,-1.26,0.012088612,0.040006674,3.83,15.1,hypothetical protein

```

# REJECTED DATA EXAMPLE
```
,transcript_id,log2FC_pe_soltub,PValue_pe_soltub,FDR_pe_soltub,Inf_pe_soltub_Mean_TPM,Ctrl_pe_soltub_Mean_TPM,annotation,rejection_reason
0,Soltu.DM.01G000120.2,-2.71,3.66813e-05,0.000308499,0.56,6.27,Microtubule associated protein (MAP65/ASE1) family protein,Duplicate PValue 3.66813e-05 for Gene ID: 01G000120
1,Soltu.DM.01G000520.2,-2.14,6.95855e-05,0.000540757,0.76,5.54,Ankyrin repeat family protein,Duplicate PValue 6.95855e-05 for Gene ID: 01G000520
2,Soltu.DM.01G000520.3,-2.14,6.95855e-05,0.000540757,0.76,5.54,Ankyrin repeat family protein,Duplicate PValue 6.95855e-05 for Gene ID: 01G000520
3,Soltu.DM.01G000520.4,-2.14,6.95855e-05,0.000540757,0.76,5.54,Ankyrin repeat family protein,Duplicate PValue 6.95855e-05 for Gene ID: 01G000520
4,Soltu.DM.01G000520.5,-2.14,6.95855e-05,0.000540757,0.76,5.54,Ankyrin repeat family protein,Duplicate PValue 6.95855e-05 for Gene ID: 01G000520
5,Soltu.DM.01G001340.2,-1.54,0.000526622,0.003077218,2.79,13.57,MAK16 protein-related,Duplicate PValue 0.000526622 for Gene ID: 01G001340
6,Soltu.DM.01G001340.3,-1.54,0.000526622,0.003077218,2.79,13.57,MAK16 protein-related,Duplicate PValue 0.000526622 for Gene ID: 01G001340
7,Soltu.DM.01G001360.3,-1.56,0.005358157,0.020885546,0.26,1.33,O-Glycosyl hydrolases family 17 protein,Duplicate PValue 0.005358157 for Gene ID: 01G001360
8,Soltu.DM.01G001360.5,-1.56,0.005358157,0.020885546,0.26,1.33,O-Glycosyl hydrolases family 17 protein,Duplicate PValue 0.005358157 for Gene ID: 01G001360
9,Soltu.DM.01G001360.6,-1.56,0.005358157,0.020885546,0.26,1.33,O-Glycosyl hydrolases family 17 protein,Duplicate PValue 0.005358157 for Gene ID: 01G001360
10,Soltu.DM.01G001570.3,-1.44,0.003694396,0.015515139,0.38,1.83,RNA-binding KH domain-containing protein,Duplicate PValue 0.003694396 for Gene ID: 01G001570
11,Soltu.DM.01G002500.2,-1.94,0.006504539,0.024373341,0.56,3.42,RING-H2 group F2A,Duplicate PValue 0.006504539 for Gene ID: 01G002500
12,Soltu.DM.01G002520.2,-1.45,0.004970763,0.019682174,1.47,6.62,TPX2 (targeting protein for Xklp2) protein family,Duplicate PValue 0.004970763 for Gene ID: 01G002520
```