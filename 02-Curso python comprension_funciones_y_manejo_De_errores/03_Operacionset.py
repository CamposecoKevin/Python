# Operaciones en conjuntos
set_contries_america = {"Guatemala", "Salvador", "Honduras", "Argentina"}

set_contries_suramerica = {"Argentina", "Chile", "Brisil"}
# Union de conjuntos, une todos.
set_both = set_contries_america.union(set_contries_suramerica)
print(set_both)
set_both = (set_contries_america | set_contries_suramerica)
print(set_both)
# intersección, solo toma los que se comparten.
set_both_intersecion = set_contries_america.intersection(
    set_contries_suramerica)
print(set_both_intersecion)
set_both_intersecion = (set_contries_america &
                        set_contries_suramerica)
print(set_both_intersecion)


# Diferencia: toma todos de la primera, menos los que comparte.
set_both_dif = set_contries_america.difference(
    set_contries_suramerica)
print(set_both_dif)
set_both_dif = (set_contries_america -
                set_contries_suramerica)
print(set_both_dif)

# diferencia simitrica: une todos, menos el que se repite.
set_both_dif_sim = set_contries_america.symmetric_difference(
    set_contries_suramerica)
print(set_both_dif_sim)
set_both_dif_sim = (set_contries_america ^
                    set_contries_suramerica)
print(set_both_dif_sim)


countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set()
new_set = countries.union(northAm, centralAm, southAm)

print(new_set)
