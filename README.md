# DeepRabGTPSite: A Multi-Window Protein Language Model Framework for Predicting GTP-Binding Sites in Rab GTPases as Dually-Actionable Cancer Drug Targets
Wei-En Jhang, Sin-Siang Wei, Yu-Han Weng, Yi-Ting Chung, Yu-Yen Ou
|[ 🎇&nbsp;Abstract](#abstract) |[📃&nbsp;Dataset](#Dataset) |[ 🚀&nbsp;Quick Prediction ](#colab)|[ 📚&nbsp;License](#License)|
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

## 🚀Quick Prediction <a name="colab"></a>
[<img src="https://colab.research.google.com/assets/colab-badge.svg">](https://colab.research.google.com/drive/19pOze_jxxAq3XOQd6yuIiCBLEpbGBI29?usp=sharing)<br>
https://colab.research.google.com/drive/19pOze_jxxAq3XOQd6yuIiCBLEpbGBI29?usp=sharing

### Step 1: Environment Setup
Open the link of Google colab and change the hardware to a CPU device(recommended).

### Step 2: Excute the program
This Colab notebook will automatically import all necessary dependencies and download the required files.

### Step 3: Submit your fasta file and wait for the Prediction result 

Upload your FASTA file to run the prediction.
The format of the FASTA file will be as follows:
```bash
>Q9C7T7
MSRRPDLLRGSVVATVAATFLLFIFPPNVESTVEKQALFRFKNRLDDSHNILQSWKPSDSPCVFRGIT
>"Name"
(Animo Acid Sequence)
```
(Or use our dataset for RTK testing. [⬇️link](https://github.com/B1607/RTK_RAG/tree/main/Data/Fasta/RTK_Test)<br>
The result will be formatted as follows:
```bash
Fasta     :  >Q9C7T7
Amino acid:  MSRRPDLLRGSVVATVAATFLLFIFPPNVESTVEKQALFRFKNRLDDSHNILQSWKPSDSPCVFRGIT...
Prediction:  1000000000000000000000000000000000000000000000000000000000000000000...
```
1 indicates the amino acid is predicted to be a ATP-Binding residue.<br>
0 indicates the amino acid is predicted to be a non-ATP-Binding residue.

## 📚&nbsp;License <a name="License"></a>
Licensed under the Academic Free License version 3.0
