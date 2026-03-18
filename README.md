# 🧬 Genome Sequence Research: Parallel & Distributed Computing

Questo progetto esplora l'ottimizzazione dell'analisi di sequenze genomiche attraverso diverse strategie di parallelismo. L'obiettivo è la ricerca di sottostringhe specifiche all'interno di grandi volumi di dati genetici (file `.faa` e `.fna`) confrontando l'efficienza di architetture a thread singolo, multi-core e cluster distribuiti.

## 🎯 Obiettivi del Progetto
* **Bioinformatica:** Analisi di sequenze di DNA, RNA e proteine utilizzando la libreria `Biopython`.
* **Big Data Processing:** Implementazione del modello di programmazione **MapReduce** (fasi di Mapping, Shuffle e Reducing).
* **Performance Benchmarking:** Confronto prestazionale tra tre approcci:
    1.  **Monothread:** Esecuzione sequenziale standard.
    2.  **Multithread:** Parallelismo su singola macchina tramite il modulo `multiprocessing` di Python.
    3.  **Distributed Computing:** Elaborazione su cluster (10 nodi, 48 thread) utilizzando il framework **Ray**.

## 🛠️ Tech Stack
* **Linguaggio:** Python 3.10+ (Ubuntu 22.04 LTS).
* **Librerie Core:** `Ray` (calcolo distribuito), `Biopython` (parsing genomico), `Multiprocessing`.
* **Dataset:** Sequenze genomiche umane (GRCh37/GRCh38) con dimensioni da 42MB a 742MB.

## 📊 Risultati e Considerazioni
I test hanno dimostrato un miglioramento drastico delle prestazioni con l'aumentare del parallelismo:
* **Monothread:** Risultato il metodo più lento, con tempi che crescono proporzionalmente alla dimensione del file (fino a ~683s per 742MB).
* **Multithread:** Notevole incremento di velocità sfruttando tutti i core della CPU locale.
* **Ray (Distributed):** L'approccio più efficiente e scalabile, capace di gestire grandi volumi di dati sfruttando la potenza di calcolo di più macchine contemporaneamente.

## 🚀 Struttura del Codice
Il progetto è suddiviso in tre varianti principali:
1.  `monothread.py`: Logica MapReduce sequenziale.
2.  `multithread.py`: Utilizza `Pool.starmap` per suddividere il lavoro in chunk sui core disponibili.
3.  `ray_distributed.py`: Utilizza l'annotazione `@ray.remote` per distribuire i task sui nodi del cluster.

---
*Progetto realizzato da: Federico Sciuto e Carmelo Santamaria (Novembre 2023)*.
