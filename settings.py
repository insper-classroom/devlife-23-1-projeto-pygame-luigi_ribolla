from csv import reader 

def import_csv_layout(path):
    terreno = []
    with open(path) as level_map:
        layout = reader (level_map, delimiter = ',')
        for row in layout:
            terreno.append(list(row))
        return terreno
    

print(import_csv_layout('docs/csv-map/parede.csv'))
