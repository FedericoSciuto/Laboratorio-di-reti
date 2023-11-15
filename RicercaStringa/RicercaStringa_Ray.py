from Bio import SeqIO
from time import perf_counter
from functools import reduce
import multiprocessing
from multiprocessing import cpu_count
import ray

# Funzione di mapping che conta le occorrenze della stringa target in una sottosequenza
def mapping(sequenza, stringa_target):
    lunghezza_target = len(stringa_target)
    sottosequenze = [sequenza[i:i + lunghezza_target] for i in range(len(sequenza) - lunghezza_target + 1)]
    return sottosequenze

# Funzione di reduce che somma i conteggi intermedi per sequenza
def reducing(sottosequenze, stringa_target):
    conteggio = sottosequenze.count(stringa_target)
    return conteggio
    
def conteggio_finale(count1, count2):  
    return count1 + count2

# Funzione che elabora una porzione dei dati e restituisce il conteggio
@ray.remote  # Indica che questa funzione è gestita da Ray
def process_chunk(chunk, stringa_target):
    conteggi_intermedi = map(lambda sequenza: reducing(mapping(sequenza.seq, stringa_target), stringa_target), chunk)
    conteggio = reduce(conteggio_finale, conteggi_intermedi)
    return conteggio

# Funzione principale che esegue le funzioni di mapping, reducing, conteggio_finale e process_chunk
def MapReduce(data, stringa_target, num_process):
    start_time = perf_counter()

    # Dividi i dati in porzioni per la parallelizzazione
    chunk_size = len(data) // num_process
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    
    # Creazione di un elenco di riferimenti a risultati futuri
    future_results = [process_chunk.remote(chunk, stringa_target) for chunk in chunks]
    
    # Attendere i risultati dai processi paralleli
    conteggi_intermedi = ray.get(future_results)

    # Utilizza reduce() per sommare i conteggi intermedi
    conteggio_totale = reduce(conteggio_finale, conteggi_intermedi)

    end_time = perf_counter()

    print(f"\nLa stringa '{stringa_target}' appare {conteggio_totale} volte nel file.")
    print(f"Tempo di esecuzione: {end_time - start_time:0.3f} secondi.\n")

def main():
    ray.init()  # Inizializza Ray

    global filename

    # Scelta del file da analizzare
    genome_files = input("\nSeleziona il file da analizzare:\n1 -> GRCh37_42MB_protein.faa\n2 -> GRCh38_105MB_protein.faa\n3 -> GRCh37_302MB_rna.fna\n4 -> GRCh38_742MB_rna.fna\n")

    file_mapping = {
        "1": "GRCh37_42MB_protein.faa",
        "2": "GRCh38_105MB_protein.faa",
        "3": "GRCh37_302MB_rna.fna",
        "4": "GRCh38_742MB_rna.fna"
    }

    filename = file_mapping.get(genome_files)

    if not filename:
        print("\nOpzione non valida\n")
    else:
        stringa_target = input("\nStringa da ricercare: ")
        
        # Ottiene il numero totale di core disponibili sul cluster
        cluster_resources = ray.cluster_resources()
        num_process_max = int(cluster_resources.get("CPU", 1)) # Numero di core disponibili
        num_process = int(input(f"\nNumero di processi da utilizzare (max = {num_process_max}): "))
        
        if num_process < 1 or num_process > num_process_max:
        	print(f"\nNumero di processi inserito non valido (deve essere compreso tra 1 e {num_process_max})\n")
        else:
        	# Fase di Splitting (Splitting Phase)
        	sequenze = list(SeqIO.parse(filename, 'fasta'))
        	
        	# Chiamata alla funzione MapReduce con parallelismo
        	MapReduce(sequenze, stringa_target, num_process)

if __name__ == "__main__":
    main()

