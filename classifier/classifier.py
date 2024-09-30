'''
Gene lists, extracted by clustering and random forest, would be served to machine learning model.
210329
'''
classifier_dict = {}
# The list of six genes chosen from hiearachically-clustered heatmap
basic_classifier = ['ZNF764', 'QARS', 'MRM1', 'HELZ2', 'PCBD1', 'HIPK2']
classifier_dict['basic'] = basic_classifier

'''
Union classifiers: Combined gene lists constructed by combining 
previously trained top 10 gene classifiers
'''


#Metacore&GSEA target genes
MandG_classifier = ['CHKB', 'CYP2C18','DCAKD', 'MAMDC4', 'MDP1', 'NUBP2', 'PCDH17',
                    'RPAP1', 'RPL13AP20', 'RPL9', 'TMEM63A' 'TXLNGY', 'WFDC8', 'ZNF592',
                    'ZNF615', 'ZNF626', 'ZNF764', ]
classifier_dict['MandG'] = MandG_classifier

#GSEA_R enrichment_all
GSEA_R_enrichment_all = ['CD3E', 'CSF2', 'CXCL10', 'CXCL11', 'CXCL9', 'GBP1',
                         'HIST1H2BF', 'IFIT1', 'IL12B', 'IL1B', 'IL2',
                         'ISG15', 'ITGB2', 'KIR3DL1', 'KLRD1', 'MX1', 'MX2','OAS2']
classifier_dict['GSEA_R_enrichment_all'] = GSEA_R_enrichment_all

#GSEA_R enrichment_intersection
GSEA_R_enrichment_intersection = ['CD247', 'CD3D', 'CD3E', 'CD3G',
                                  'CSF2','HIST1H2BF', 'ICAM1', 'IL1B',
                                  'KIR3DL1', 'KIR3DL2' 'KLRD1']
classifier_dict['GSEA_R_enrichment_intersection'] = GSEA_R_enrichment_intersection

#Bladder cancer basal type
BC_basal = ['GATA3', 'HIF1A', 'IRF3', 'IRF7', 'MEOX2', 'NCOR1',
            'NFKB1', 'PIAS4', 'PPARA', 'RELA', 'SP1', 'STAT1',
            'STAT3', 'TP63', 'TRIM24']
classifier_dict['BC_basal'] = BC_basal

BC_basal_9gene = ['CD44', 'CDH3', 'KRT1', 'KRT14', 'KRT16', 'KRT5', 'KRT6A'
                  'KRT6B', 'KRT6C']
classifier_dict['BC_basal_9gene'] = BC_basal_9gene
#Bladder cancer luminal type
BC_luminal = ['AHR', 'CD24', 'ERBB2', 'ERBB3', 'FABP4', 'FGFR3',
              'FOXA1', 'GATA3','GPX2', 'HDAC1', 'HTT', 'KRT18',
              'KRT19', 'KRT20', 'KRT7', 'KRT8', 'MKL1', 'MYC',
              'NFKB1', 'PGR', 'PPARA', 'PPARG', 'SMAD3', 'SMAD7',
              'SREBF2', 'SRF', 'STAT1', 'TP53', 'TRIM24', 'XBP1']
classifier_dict['BC_luminal'] = BC_luminal

BC_luminal_16gene= ['CD24', 'ERBB2', 'ERBB3', 'FABP4', 'FGFR3',
                    'FOXA1', 'GATA3', 'GPX2', 'KRT18', 'KRT19',
                    'KRT20', 'KRT7', 'KRT8', 'PPARG', 'XBP1']
classifier_dict['BC_luminal_16gene'] = BC_luminal_16gene
#Bladder cancer p53 type and its like
BC_p53_pathway = ['ANLN', 'ANXA2', 'CRYAB', 'CSRP1', 'FEN1', 'FHL1',
                 'GRB2', 'MAD2L1', 'MBNL2', 'NUPR1', 'PDGFRA', 'PPP1CA',
                 'PRKD1', 'PTPRE', 'RRM2', 'SORBS1', 'TBL1X', 'UBE2C', 'ZMAT3']
classifier_dict['BC_p53_pathway'] = BC_p53_pathway

BC_p53_like = ['AHR', 'E2F2', 'FOXM1', 'MKL1', 'MYOCD', 'RB1', 'SMAD7', 'SMARCB1',
               'SRF', 'TBX2', 'TCF3', 'TP53']
classifier_dict['BC_p53_like'] = BC_p53_like
#Bladder cancer p63 pathway
BC_p63_pathway = ['ADA', 'CCNA2', 'CCNG1', 'CDK6', 'F3', 'GFI1', 'IGFBP3',
                  'IGFBP6', 'IL1B', 'KIF23', 'LYN', 'MYC', 'PRNP', 'PTPN12', 'S100A4',
                  'SERPINE1', 'SFN']
classifier_dict['BC_p63_pathway'] = BC_p63_pathway

#Bladder cancer reference.eau-cancer genome (Reference based)

squamous_ref = ['BARX2', 'CD44', 'CXCL9', 'FYB', 'GBP5', 'GNLY', 'HMGA2',
                'IDO1', 'IL20RB', 'MUC16', 'PCSK9', 'PDZK1IP1', 'SAA1', 'SERPINA1',
                'SERPINB7', 'SH2D5', 'TGFBI', 'TGM1', 'TMEM45A', 'WARS']
classifier_dict['squamous_ref'] = squamous_ref

luminal_ref = ['ADH6', 'AGAP11', 'C19orf45', 'CCR7', 'FMO9P', 'GABBR2',
               'IGDCC3', 'IGF2', 'KRT20', 'PVALB', 'SCNN1B', 'SCNN1G',
               'SLC1A6', 'SLC6A4', 'SNX31', 'SPINK1', 'UPK1A', 'UPK3A']
classifier_dict['luminal_ref'] = luminal_ref

luminal_infiltrated_ref = ['ADAM33', 'C7', 'COMP', 'HSPB6', 'IGF1', 'MS4A1',
                           'MYH11', 'OGN', 'OMD', 'PDLIM3', 'PRELP', 'PRUNE2',
                           'SFRP4', 'SMOC2', 'SPON1', 'TCEAL2', 'ZEB2']
classifier_dict['luminal_infiltrated_ref'] = luminal_infiltrated_ref

luminal_papillary_ref = ['ATOH8', 'CHD2', 'CLCA4', 'CYP3A5', 'CYP4F8',
                         'ERN2', 'FAM3D', 'FOXA1', 'HS6ST3', 'LGALS4',
                         'REG4', 'SLC14A1', 'TFF1', 'TRIM31', 'UCA1', 'UGT1A1']
classifier_dict['luminal_papillary_ref'] = luminal_ref

neuronal_ref = ['ART5', 'CHGB', 'CHRNB2', 'CLGN', 'CNTFR','DLX5', 'DPF1', 'GFRA3',
                'GNG4', 'HUNK', 'NAT8L', 'NKAIN1', 'PEG10', 'RIMS4', 'RND2',
                'SCG2', 'SLC38A3', 'STAC2', 'UCHL1', 'YBX2']
classifier_dict['neuronal_ref'] = neuronal_ref

#GESA_YES_Genes
GESA_YES_genes = ['AFAP1', 'C11orf95', 'CARD16', 'CDK6', 'DPH2', 'ITGAX',
                  'KCTD14', 'MAP7D3', 'NEK6', 'NT5E', 'P3H1', 'PCDHB9',
                  'PPIL2', 'PTPRC', 'RFX7', 'TCAF2', 'TMEM132A']
classifier_dict['GESA_yes_genes'] = GESA_YES_genes

#Up regulated genes
up_regulated = ['AFAP1', 'BHLHE40', 'C11orf95', 'COX17', 'HCFC1R1',
                'ITGAX', 'KCTD14', 'KIAA1671', 'NT5E', 'PCDHB9',
                'PLEK', 'POSTN', 'POU2F2', 'PPP1R35', 'RFX7',
                'SLC15A3', 'THBS2', 'TNFAIP8']
classifier_dict['up_regulated'] = up_regulated



