from pybtex.database import parse_file, BibliographyData, Entry

old = input('input old "file-name.bib": ')
new = input('input new "file-name.bib": ')

old_bib = parse_file(old)
new_bib = parse_file(new)



old_entries = set(old_bib.entries.keys())
new_entries = set(new_bib.entries.keys())

new_unique_entries = new_entries - old_entries


unique_entries_bib = BibliographyData()

for entry in new_unique_entries:
    unique_entries_bib.entries[entry] = new_bib.entries[entry]

with open('unique_entries.bib', 'w') as bibfile:
    unique_entries_bib.to_file(bibfile)

print("Entradas únicas foram salvas em 'unique_entries.bib'")