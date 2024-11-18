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
MandG_classifier = ['CCDC64', 'CHKB', 'DCAKD', 'EIF2S1', 'EIF4E', 'GAMT', 'MAMDC4', 'MDP1',
                    'NUBP2', 'PM20D2', 'RPAP1', 'RPL9', 'STK36', 'TATDN1', 'TMEM63A', 'WFDC8',
                     'ZNF493', 'ZNF592', 'ZNF615','ZNF626', 'ZNF697',]
classifier_dict['MandG'] = MandG_classifier

#GSEA_R enrichment_all
GSEA_R_enrichment_all = ['BCL2A1', 'CCL2', 'CD247', 'CD3E', 'CSF2', 'CXCL10', 'CXCL11', 'CXCL9',
                         'FCGR2B', 'GBP1', 'HIST1H2BF', 'ICAM1', 'IFIT1', 'IFNA2', 'IL11',
                         'IL12B', 'IL1B', 'IL2', 'ITGAL', 'ITGB2', 'KIR3DL1', 'KIR3DL2',
                         'KLRD1', 'LCK', 'MX2', 'OAS2', 'SLA',]
classifier_dict['GSEA_R_enrichment_all'] = GSEA_R_enrichment_all

#GSEA_R enrichment_intersection
GSEA_R_enrichment_intersection = ['CD247', 'CD3D', 'CD3E', 'CD3G',
                                  'CSF2','HIST1H2BF', 'ICAM1', 'IL1B',
                                  'KIR3DL1', 'KIR3DL2' 'KLRD1']
classifier_dict['GSEA_R_enrichment_intersection'] = GSEA_R_enrichment_intersection

#Bladder cancer basal type
BC_basal = ['GATA3', 'HDAC1', 'HIF1A', 'IRF3', 'IRF7', 'JUN', 'KLF2',
            'MEOX2', 'NCOR1', 'NFKB1', 'PIAS4', 'PPARA', 'RELA', 'SP1',
            'SPDEF', 'STAT1', 'TP63', 'TRIM24',]
classifier_dict['BC_basal'] = BC_basal

BC_basal_9gene = ['CD44', 'CDH3', 'KRT1', 'KRT14', 'KRT16', 'KRT5', 'KRT6A'
                  'KRT6B', 'KRT6C']
classifier_dict['BC_basal_9gene'] = BC_basal_9gene
#Bladder cancer luminal type
BC_luminal = ['AHR', 'CD24', 'CYP2J2', 'ERBB2', 'ERBB3', 'FGFR3', 'FOXA1',
              'GATA3', 'GPX2', 'HTT', 'KRT18', 'KRT19', 'KRT20', 'KRT7',
              'KRT8', 'MKL1', 'MYC', 'NFKB1', 'PGR', 'PPARA', 'PPARG',
              'SMAD3', 'SMAD7', 'SMARCA4', 'SPDEF', 'SREBF2', 'SRF',
              'STAT1', 'STAT3', 'TP53', 'TRIM24', 'XBP1',]
classifier_dict['BC_luminal'] = BC_luminal

BC_luminal_18gene= ['CD24', 'ERBB2', 'ERBB3', 'FABP4', 'FGFR3',
                    'FOXA1', 'GATA3', 'GPX2', 'KRT18', 'KRT19',
                    'KRT20', 'KRT7', 'KRT8', 'PPARG', 'XBP1']
classifier_dict['BC_luminal_16gene'] = BC_luminal_18gene
#Bladder cancer p53 type and its like
BC_p53_pathway = ['ANLN', 'ANXA2', 'BUB1', 'CA9', 'CHEK1', 'CKAP2', 'CKS1B',
                  'CNN1', 'CSRP1', 'DLGAP5', 'FEN1', 'FHL1', 'GRB2', 'HSPA8',
                  'IGFBP5', 'KIAA0101', 'MAD2L1', 'MBNL2', 'MMP23B', 'NDC80',
                  'NME1', 'NUPR1', 'PDGFRA', 'PPP1CA', 'PRKD1', 'PTPRE',
                  'PTTG1', 'RRM2', 'SERPING1', 'SORBS1', 'TBL1X', 'TSC22D3',
                  'TTK', 'VRK1', 'ZMAT3',]
classifier_dict['BC_p53_pathway'] = BC_p53_pathway

BC_p53_like = ['AHR', 'CDKN2A', 'E2F2', 'FOXM1', 'HEY2', 'HTT', 'MKL1', 'MYC',
               'MYOCD', 'NFE2L2', 'RB1', 'SMAD7', 'SMARCB1', 'SPDEF', 'SRF',
               'TBX2', 'TCF3', 'TP53']
classifier_dict['BC_p53_like'] = BC_p53_like
#Bladder cancer p63 pathway
BC_p63_pathway = ['ADA', 'CCNA2', 'CCNB1', 'CCNG1', 'CD82', 'CKS2', 'F3', 'GFI1', 'HBEGF',
                  'IGFBP6', 'IL1B', 'ITGA3', 'LYN', 'MYC', 'PI3', 'PLAU', 'PRNP',
                  'PTHLH', 'PTPN12', 'S100A4', 'S100A8', 'SERPINB2', 'SERPINE1',
                  'SFN', 'SH2B3', 'TNFRSF10A']
classifier_dict['BC_p63_pathway'] = BC_p63_pathway

#Bladder cancer reference.eau-cancer genome (Reference based)

squamous_ref = ['AHNAK2', 'AREG', 'BARX2', 'CD44', 'CDH3', 'CDSN',
                'CPA4', 'CXCL10', 'CXCL5', 'CXCL9', 'DSG3', 'F3',
                'HEPHL1', 'HMGA2', 'IDO1', 'IL20RB', 'KLK11', 'KRT6A',
                'L1CAM', 'LAMA3', 'MFI2', 'MUC16', 'NRG1', 'PCSK9',
                'PDZK1IP1', 'PI3', 'SAA1', 'SAA2', 'SERPINA1', 'SERPINA3',
                'SERPINB7', 'SPRR2A', 'SPRR2D', 'TGM1', 'TMEM45A',
                'TNC', 'VSNL1']
classifier_dict['squamous_ref'] = squamous_ref

luminal_ref = ['ADH6', 'AGAP11', 'B3GAT1', 'BHMT', 'DHRS2',
               'EMX1', 'FMO9P', 'GABBR2', 'GATA3', 'HIC2',
               'HS3ST6', 'IGFL1', 'KRT20', 'MAL', 'PKD1L1',
               'PRAP1', 'PSD2', 'PTN', 'PVALB', 'SCNN1B',
               'SCNN1G', 'SLC1A6', 'SLC30A2', 'SLC6A4',
               'SNX31', 'SPINK1', 'UPK1A', 'UPK2',]
classifier_dict['luminal_ref'] = luminal_ref

luminal_infiltrated_ref = ['ACTC1', 'ACTG2', 'ADAM33', 'ADH1B',
                           'BLK', 'C7', 'CCL19', 'CNN1', 'CSDC2',
                           'DES', 'ELN', 'FGF7', 'HSPB6', 'IGF1',
                           'MFAP4', 'MS4A1', 'MYH11', 'OGN', 'OMD',
                           'P2RX1', 'PDLIM3', 'PLA2G2D', 'PRUNE2',
                           'PSD', 'SLC2A4', 'SMOC2', 'SPON1', 'TCEAL2',
                           'WBSCR17', 'ZEB2']
classifier_dict['luminal_infiltrated_ref'] = luminal_infiltrated_ref

luminal_papillary_ref = ['ATOH8', 'BTBD16', 'CHD2', 'CLCA4', 'CYP3A5', 'CRTAC1', 'CYP4F8',
                         'ERN2', 'FAM3D', 'FGFR3',  'FOXA1', 'HS6ST3', 'LGALS4',
                         'REG4', 'SLC14A1', 'TFF1', 'TRIM31', 'UCA1', 'UGT1A1']
classifier_dict['luminal_papillary_ref'] = luminal_ref

neuronal_ref = ['ART5', 'BEX1', 'BRSK1', 'BRSK2',
                'CHGB', 'CHRNB2', 'CLGN', 'ENHO', 'FSD1', 'GFRA3',
                'GNG4', 'HOXC10', 'HRASLS', 'HUNK', 'IGF2BP1',
                'JPH3', 'KCNA6', 'KCNH2', 'LHX2', 'MAGED4B', 'NAT8L',
                'NKAIN1', 'NOTUM', 'PEG10', 'PPM1E', 'RIMS4', 'SLC38A3',
                'SNAP25', 'SV2A', 'TWIST1', 'YBX2']
classifier_dict['neuronal_ref'] = neuronal_ref

#GESA_YES_Genes
GESA_YES_genes = ['AFAP1', 'ATAD3B', 'CADM4', 'CARD16', 'CD53', 'CDK6',
                  'DPH2', 'INHBA', 'ITGAX', 'KCTD1', 'KCTD14', 'MYLK',
                  'NEK6', 'NT5E', 'OLFM4', 'PCDHB9', 'PLEK', 'POSTN',
                  'PPIL2', 'PTPRC', 'RFX7', 'SHANK3', 'SIX5', 'TFAM', 'TMEM132A']
classifier_dict['GESA_yes_genes'] = GESA_YES_genes

#Up regulated genes
up_regulated = ['AFAP1', 'BGN', 'CADM4', 'CARD16', 'CD53', 'CDK6', 'COX17',
                'DPH2', 'FYB', 'GADD45B', 'HCFC1R1', 'INHBA', 'ITGAX',
                'KCTD1', 'KCTD14', 'NEK6', 'NT5E', 'NUDT12', 'OLFM4',
                'PCDHB9', 'POSTN', 'POU2F2', 'PPIL2', 'RFX7', 'SLC15A3',
                'TFAM', 'THBS2', 'TMEM132A', 'TNFAIP8']
classifier_dict['up_regulated'] = up_regulated



