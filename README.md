# DeepRabGTPSite: Protein Language Model Embeddings and Multi-Window Convolutional Networks for Predicting GTP-Binding Residues in Rab GTPases

Wei-En Jhang, Sin-Siang Wei, Yu-Han Weng, Yi-Ting Chung, Yu-Yen Ou

| [🎇 Abstract](#abstract) | [📃 Dataset](#Dataset) | [💾 Requirements](#requirement) | [📚 License](#License) |
| --- | --- | --- | --- |

## 🎇Abstract <a name="abstract"></a>

DeepRabGTPSite is a sequence-based predictor of GTP-binding residues that combines frozen ProtT5 (`Rostlab/prot_t5_xl_half_uniref50-enc`) residue embeddings with a four-branch multi-window convolutional neural network (MCNN; kernel widths 4, 6, 8, and 10 over a 15-residue window). Trained on 104 non-redundant vesicle-trafficking GTPase sequences and evaluated on 27 sequences (40% CD-HIT identity cutoff), the selected model achieved a sensitivity of 0.9798, specificity of 0.9684, accuracy of 0.9689, MCC of 0.7378, AUROC of 0.9951, and AUPRC of 0.8583.

DeepRabGTPSite provides candidate residue-level GTP-binding annotations from sequence alone to support structural mapping, mutagenesis prioritization, and functional studies across Rab and vesicle-trafficking GTPases. Predictions do not establish functional modulation direction, compound selectivity, or therapeutic efficacy. <br>

## 📃Dataset <a name="Dataset"></a>

Sequences and UniProt `BINDING` ("GTP") annotations were collected from UniProtKB (1,086 vesicle-trafficking-related entries) and clustered with CD-HIT at 40% sequence identity, yielding 131 non-redundant sequences totaling 57,294 residues (mean 437.4 aa, median 260.0 aa, range 163–1,500 aa; encompassing both canonical \~200–250 aa Rab/Ras-family GTPases and larger multi-domain trafficking GTPases).

| Dataset | Protein Sequences | After CD-HIT (Identity < 40%) |
| :--- | :---: | :---: |
| Vesicle-Trafficking-Related Proteins | 1,086 | 131 |

| Dataset | Protein Sequences | GTP-Binding Residues | Non-Binding Residues |
| :--- | :---: | :---: | :---: |
| Training Set | 104 | 1,815 | 44,815 |
| Evaluation Set\* | 27 | 446 | 10,218 |

*\*The evaluation set was also used for configuration comparison and decision-threshold selection.*

## 💾Requirements <a name="requirement"></a>

```bash
h5py==3.15.0
tqdm==4.67.1
numpy==2.3.3
scikit-learn==1.7.2
tensorflow==2.20.0
```

## 📚License <a name="License"></a>

Licensed under the Academic Free License version 3.0