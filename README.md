# DeepRabGTPSite: A Multi-Window Protein Language Model Framework for Predicting GTP-Binding Sites in Rab GTPases as Dually-Actionable Cancer Drug Targets
Wei-En Jhang, Sin-Siang Wei, Yu-Han Weng, Yi-Ting Chung, Yu-Yen Ou
|[🎇&nbsp;Abstract](#abstract) |[📃&nbsp;Dataset](#Dataset) |[💾&nbsp;Requirements ](#requirement)|[ 📚&nbsp;License](#License)|
|-------------------------------|-----------------------------|------------------------------------|-----------------------------|

## 🎇Abstract <a name="abstract"></a>
The Rab subfamily of RAS superfamily GTPases are master regulators of intracellular vesicular transport, and their dysregulation is increasingly implicated in cancer progression. The precise identification of their GTP-binding sites is a critical first step for the rational design of novel cancer therapeutics. Interestingly, targeting Rab proteins offers a unique therapeutic duality: small-molecule activators of RAB7 can enhance lysosomal degradation of oncogenic receptors, while inhibitors of RAB27 can block the secretion of tumor-promoting extracellular vesicles. Both strategies hinge on accurately targeting their GTP-binding pockets. To address this, we introduce DeepRabGTPSite, an advanced computational framework that leverages the synergy of Protein Language Models (PLMs) and a Multi-window Convolutional Neural Network (MCNN). By learning deeply, DeepRabGTPSite is designed to accurately predict GTP-binding residues across the diverse Ras family. When evaluated on an independent test set, our model achieves superior performance (Sensitivity 0.9507, MCC 0.8219, and AUC 0.9946) compared to existing general-purpose predictors.  This work provides a powerful and specialized tool to accelerate the discovery of both activators and inhibitors targeting Ras proteins, opening new avenues for function-specific cancer therapies.
<br>

![workflow](figure/workflow.png)

## 📃Dataset <a name="Dataset"></a>

| Dataset            | Protein Sequence |    Similarity < 40%  | 
|--------------------|------------------|--------------------------|
| Vesicle_Trafficking_Related_Proteins   |   1086             |          131             |      

| Dataset            | Protein Sequence |    GTP Binding Residues  | Non-Binding Residues    |
|--------------------|------------------|--------------------------|--------------------------|
| Training Data    |   104             |          1,815             |44,815                      |
| Independent Testing Data     |    27         |                    446    |     10,218                  |

## 💾Requirements <a name="requirement"></a>
```bash
h5py==3.15.0
tqdm==4.67.1
numpy==2.3.3
scikit-learn==1.7.2 
tensorflow==2.20.0 
```

## 📚&nbsp;License <a name="License"></a>
Licensed under the Academic Free License version 3.0
