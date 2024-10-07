# %% [markdown]
# **Task 08: Completing missing data**

# %%
#!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

# %%
from rdflib import Graph, Namespace, Literal, URIRef
g1 = Graph()
g2 = Graph()

# Definir el namespace correcto para VCARD y DATA
DATA = Namespace("http://data.org#")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")

g1.parse(github_storage + "/rdf/data01.rdf", format="xml")
g2.parse(github_storage + "/rdf/data02.rdf", format="xml")

print("Tripletas en g1:")
for s, p, o in g1:
    print(s, p, o)
    
print("Tripletas en g2:")
for s, p, o in g2:
    print(s, p, o)

# %% [markdown]
# Tarea: lista todos los elementos de la clase Person en el primer grafo (data01.rdf) y completa los campos (given name, family name y email) que puedan faltar con los datos del segundo grafo (data02.rdf). Puedes usar consultas SPARQL o iterar el grafo, o ambas cosas.

# %%
# ITERANDO EL GRAFO

# Supongamos que g1 y g2 ya están cargados correctamente como se hizo antes

# Iterar sobre todas las personas en el primer grafo
for person in g1.subjects(RDF.type, DATA.Person):
    print(f"Persona: {person}")

    # Inicializar los campos
    given_name = None
    family_name = None
    email = None

    # Buscar el nombre de pila, apellido y email en g1
    for gn in g1.objects(person, VCARD.Given):
        given_name = gn
    for fn in g1.objects(person, VCARD.Family):
        family_name = fn
    for em in g1.objects(person, VCARD.EMAIL):
        email = em

    # Si algún dato falta, buscarlo en g2
    if not given_name:
        for gn in g2.objects(person, VCARD.Given):
            given_name = gn
    if not family_name:
        for fn in g2.objects(person, VCARD.Family):
            family_name = fn
    if not email:
        for em in g2.objects(person, VCARD.EMAIL):
            email = em

    # Imprimir los resultados con los datos completados
    print(f"  Given: {given_name if given_name else 'No given name'}")
    print(f"  Family: {family_name if family_name else 'No family name'}")
    print(f"  Email: {email if email else 'No email'}")
    print()

# Iterar sobre todas las personas en el segundo grafo   
    





