from Bio import SeqIO
from time import perf_counter
from functools import reduce

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

# Funzione principale che esegue le funzioni di mapping, reducing e conteggio_finale
def MapReduce(data, stringa_target):
    start_time = perf_counter()

    # Utilizza map() per ottenere i conteggi intermedi per sequenza
    conteggi_intermedi = map(lambda sequenza: reducing(mapping(sequenza.seq, stringa_target), stringa_target), data)

    # Utilizza reduce() per sommare i conteggi intermedi
    conteggio_totale = reduce(conteggio_finale, conteggi_intermedi)

    end_time = perf_counter()

    print(f"\nLa stringa '{stringa_target}' è presente {conteggio_totale} volte nel file.")
    print(f"Tempo di esecuzione: {end_time - start_time:0.3f} secondi.\n")

def main():
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

        # Fase di Splitting (Splitting Phase)
        sequenze = list(SeqIO.parse(filename, 'fasta'))

        # Chiamata alla funzione MapReduce
        MapReduce(sequenze, stringa_target)

if __name__ == "__main__":
    main()
