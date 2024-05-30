import bibtexparser
from bibtexparser.bibdatabase import BibDatabase

def carregar_bibtex(arquivo):
    with open(arquivo, 'r') as bibtex_file:
        return bibtexparser.load(bibtex_file)

def salvar_bibtex(bib_database, arquivo):
    with open(arquivo, 'w') as bibtex_file:
        bibtexparser.dump(bib_database, bibtex_file)

def diferenca_bibtex(bib1, bib2):
    ids_bib2 = {entry['ID'] for entry in bib2.entries}
    diferenca_entries = [entry for entry in bib1.entries if entry['ID'] not in ids_bib2]

    diferenca_db = BibDatabase()
    diferenca_db.entries = diferenca_entries
    return diferenca_db

def intersecao_bibtex(bib1, bib2):
    ids_bib2 = {entry['ID'] for entry in bib2.entries}
    intersecao_entries = [entry for entry in bib1.entries if entry['ID'] in ids_bib2]
    intersecao_db = BibDatabase()
    intersecao_db.entries = intersecao_entries
    return intersecao_db

def complemento_intersecao_bibtex(bib1, bib2):
    ids_bib1 = {entry['ID'] for entry in bib1.entries}
    ids_bib2 = {entry['ID'] for entry in bib2.entries}
    intersecao_ids = ids_bib1 & ids_bib2  

    complemento_entries = [
        entry for entry in bib1.entries if entry['ID'] not in intersecao_ids
    ] + [
        entry for entry in bib2.entries if entry['ID'] not in intersecao_ids
    ]
    
    complemento_db = BibDatabase()
    complemento_db.entries = complemento_entries
    return complemento_db

nome_bib1 = input('Add o nome bib 1: ') + '.bib'
nome_bib2 = input('Add o nome bib 2: ') + '.bib'
bib1 = carregar_bibtex( nome_bib1 ) 
bib2 = carregar_bibtex( nome_bib2) 


diferenca = diferenca_bibtex(bib1, bib2)


salvar_bibtex(diferenca, 'conjunto_diferenca_de_' + nome_bib1 + '_com_' + nome_bib2 + '.bib')

print('diferenca salva em diferenca.bib')
