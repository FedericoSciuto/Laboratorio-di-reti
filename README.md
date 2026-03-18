# 🧬 Genome Sequence Research: Parallel & Distributed Computing

Questo progetto esplora l'ottimizzazione dell'analisi di sequenze genomiche attraverso diverse strategie di parallelismo. L'obiettivo è la ricerca di sottostringhe specifiche all'interno di grandi volumi di dati genetici (file `.faa` e `.fna`) confrontando l'efficienza di architetture a thread singolo, multi-core e cluster distribuiti.

## 🎯 Obiettivi del Progetto
* [cite_start]**Bioinformatica:** Analisi di sequenze di DNA, RNA e proteine utilizzando la libreria `Biopython`[cite: 98, 99].
* [cite_start]**Big Data Processing:** Implementazione del modello di programmazione **MapReduce** (fasi di Mapping, Shuffle e Reducing)[cite: 14, 15].
* **Performance Benchmarking:** Confronto prestazionale tra tre approcci:
    1.  [cite_start]**Monothread:** Esecuzione sequenziale standard[cite: 114].
    2.  [cite_start]**Multithread:** Parallelismo su singola macchina tramite il modulo `multiprocessing` di Python[cite: 229, 230].
    3.  [cite_start]**Distributed Computing:** Elaborazione su cluster (10 nodi, 48 thread) utilizzando il framework **Ray**[cite: 67, 113].

## 🛠️ Tech Stack
* [cite_start]**Linguaggio:** Python 3.10+ (Ubuntu 22.04 LTS)[cite: 95, 96].
* [cite_start]**Librerie Core:** `Ray` (calcolo distribuito), `Biopython` (parsing genomico), `Multiprocessing`[cite: 97, 110, 111].
* [cite_start]**Dataset:** Sequenze genomiche umane (GRCh37/GRCh38) con dimensioni da 42MB a 742MB[cite: 198, 211].

## 📊 Risultati e Considerazioni
I test hanno dimostrato un miglioramento drastico delle prestazioni con l'aumentare del parallelismo:
* [cite_start]**Monothread:** Risultato il metodo più lento, con tempi che crescono proporzionalmente alla dimensione del file (fino a ~683s per 742MB)[cite: 452, 449].
* [cite_start]**Multithread:** Notevole incremento di velocità sfruttando tutti i core della CPU locale[cite: 454, 455].
* [cite_start]**Ray (Distributed):** L'approccio più efficiente e scalabile, capace di gestire grandi volumi di dati sfruttando la potenza di calcolo di più macchine contemporaneamente[cite: 456, 458].

## 🚀 Struttura del Codice
Il progetto è suddiviso in tre varianti principali:
1.  `monothread.py`: Logica MapReduce sequenziale.
2.  [cite_start]`multithread.py`: Utilizza `Pool.starmap` per suddividere il lavoro in chunk sui core disponibili[cite: 238].
3.  [cite_start]`ray_distributed.py`: Utilizza l'annotazione `@ray.remote` per distribuire i task sui nodi del cluster[cite: 358].

---
[cite_start]*Progetto realizzato da: Federico Sciuto e Carmelo Santamaria (Novembre 2023)*[cite: 2, 3].
