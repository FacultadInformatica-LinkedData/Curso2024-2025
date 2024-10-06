# %% [markdown]
# **Task 09: Data linking**

# %%
!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials/"

# %%
from rdflib import Graph, Namespace, Literal, URIRef
g1 = Graph()
g2 = Graph()
g3 = Graph()
g1.parse(github_storage+"rdf/data03.rdf", format="xml")
g2.parse(github_storage+"rdf/data04.rdf", format="xml")

# %% [markdown]
# Busca individuos en los dos grafos y enlázalos mediante la propiedad OWL:sameAs, inserta estas coincidencias en g3. Consideramos dos individuos iguales si tienen el mismo apodo y nombre de familia. Ten en cuenta que las URI no tienen por qué ser iguales para un mismo individuo en los dos grafos.

# %% [markdown]
# **Importamos las librerias**

# %%
from rdflib.namespace import OWL,RDF
from rdflib.plugins.sparql import prepareQuery
nameSpace3 = Namespace("http://data.three.org#")
nameSpace4 = Namespace("http://data.four.org#")
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

# %% [markdown]
# *Seleccionamos los individuos de los grafos 1 y 2 en listas, para comparar sus nombres de familias y apodos.*

# %%
primQuery = prepareQuery("""
    SELECT ?s ?given ?family WHERE { 
        ?s rdf:type nameSpace3:Person. 
        ?s vcard:given-name ?given.
        ?s vcard:family-name ?family.
    }
""", initNs={"rdf": RDF, "vcard": vcard, "nameSpace3": nameSpace3})

segQuery = prepareQuery("""
    SELECT ?s ?given ?family WHERE { 
        ?s rdf:type nameSpace4:Person. 
        ?s vcard:given-name ?given.
        ?s vcard:family-name ?family.
    }
""", initNs={"rdf": RDF, "vcard": vcard, "nameSpace4": nameSpace4})

# Almacenar URI, Given Name y Family Name
primUri = []
primGN = []
primFN = []
segUri = []
segGN = []
segFN = []

for i in g1.query(primQuery):
    primUri.append(i.get(0))
    primGN.append(i.get(1))
    primFN.append(i.get(2))

for j in g2.query(segQuery):
    segUri.append(j.get(0))
    segGN.append(j.get(1))
    segFN.append(j.get(2))

# %% [markdown]
# *Comparamos cada persona de un grafo con las del otro usando las listas generadas*

# %%
for i in primUri:
    for j in segUri:   
        if(primGN[i] == segGN[j] and primFN[i] == segFN[j]):
            g3.add((primUri[i], OWL.sameAs, segUri[j]))

# %% [markdown]
# *Finalmente imprimimos el resultado*

# %%
for s, p, o in g3:
    print(s, p ,o)


