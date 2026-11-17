# Datasets

## File format

The dataset is released as a CSV file with the following columns per instance:

- `id`: Sentence identifier
- `source`: Data source (e.g., `sigmorphon_st`, `wav2gloss`, language-specific source)
- `transcription`: Unsegmented **source** sentence (main input)
- `segmentation`: Morphological segmentation of the sentence
- `glosses`: Interlinear gloss (target)
- `translation`: Translation (in English)
- `glottocode`: Glottocode of the source language
- `language`: Source language
- `metalang_glottocode`: Glottocode of the translation language
- `metalanguage`: Translation language


## Phase 1 (`existing_set`)
This set covers the 5 following languages:
- Gitksan (`git`, `gitx1241`)
- Hokkaido Ainu (`ain`, `ainu1240`)
- Lezgi (`lez`, `lezg1247`)
- Natugu (`ntu`, `natu1246`)
- Nyangbo (`nyb`, `nyan1302`)

The development sets for all five languages are merged into one CSV file.  
We report the number of sentences and words (based on whitespaces) below.

| Language      | Sentences |     Words |
|---------------|----------:|----------:|
| Gitksan       |        42 |       388 |
| Hokkaido Ainu |       214 |       987 |
| Lezgi         |        51 |       492 |
| Natugu        |        99 |     1,280 |
| Nyangbo       |       225 |       959 |
| **Total**     |   **631** | **4,106** |

We note that Nyangbo does *not* have translations.


## Phase 2 (`new_set`)
This set covers the 5 new languages of this shared task:
- Amis (`ami`, `amis1246`)
- Even (`eve`, `even1260`)
- Japhug (`jya`, `japh1234`)
- Mukri Kurdish (`ckb`, `mukr1239`)
- Tsou (`tsu`, `tsou1248`)

The dev data can be seen in the [`phase_2`](phase_2/) folder.  
We report the number of sentences and words (based on whitespaces) below.

| Language      | Split | Sentences |     Words |
|---------------|-------|----------:|----------:|
| Amis          | dev   |        10 |        81 |
| Even          | dev   |         2 |        14 |
| Japhug        | train |     2,859 |    22,805 |
| Japhug        | dev   |       720 |     5,801 |
| Mukri Kurdish | dev   |         2 |        10 |
| Tsou          | dev   |        18 |       270 |

### File format
We follow the same formatting as in the Phase 1 dataset, but each language will have its own CSV file. 

We note that:
- All five languages are present in the GlossLM/PolyGloss corpus to some extent (Kurdish languages for Mukri Kurdish).
- Amis and Tsou have a dev set made of one short story.
- Even and Mukri Kurdish only feature *two* fully analysed sentences.
- Japhug has a training and development set, which may largely overlap with existing datasets.

## Phase 3 (test set)
All ten languages of both tracks have test sets in the [`phase_3`](phase_3/) folder.  
Below, we report the number of sentences per language.

We recall the following points:
- The test sets for the `existing_set` are available online; please do **not** use them for training (or copying results).
- The two dev sentences for Even and Mukri Kurdish come from the same corpus as the released test set.
- The Japhug test set is one corpus. 
- The Amis and Tsou test sets are a concatenation of several stories.

| Existing set | | New set | |
|---|--:|---|--:|
| **Language** | **Sentences** | **Language** | **Sentences** |
| Gitxsan | 37 | Amis | 174 |
| Hokkaido Ainu | 588 | Even | 102 |
| Lezgian | 53 | Japhug | 271 |
| Natügu | 99 | Mukri Kurdish | 40 |
| Nyangbo | 248 | Tsou | 194 |
| **Total** | **1,025** | **Total** | **781** |

## Citations
All dataset citations are in the main README file.
