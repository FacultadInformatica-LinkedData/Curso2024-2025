# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kruGN2O8GBMzSSEPT_FFaduPyAhCF6Hn

**Task 07: Querying RDF(s)**
"""

!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

"""First let's read the RDF file"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")
for s, p, o in g:
  print(s,p,o)

"""**TASK 7.1: List all subclasses of "LivingThing" with RDFLib and SPARQL**"""

# TO DO
from rdflib.plugins.sparql import prepareQuery
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
q1 = prepareQuery("""
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ns: <http://somewhere#>

SELECT ?subclass
WHERE {
  ?subclass rdfs:subClassOf ns:LivingThing .
}
""",
  initNs = { "vcard": vcard}
)

# Visualize the results
for r in g.query(q1):
  print(r)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO
q2 = prepareQuery("""
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ns: <http://somewhere#>

SELECT ?individual
WHERE {
  ?individual a ns:Person .
}
""",
  initNs = { "vcard": vcard}
)

# Visualize the results
for r in g.query(q2):
  print(r)

"""**TASK 7.3: List all individuals of just "Person" or "Animal". You do not need to list the individuals of the subclasses of person (in SPARQL only)**

"""

# TO DO
q3 = prepareQuery("""
PREFIX ns: <http://somewhere#>

SELECT ?individual1 ?individual2
WHERE {
  ?individual1 a ns:Person .
  ?individual2 a ns:Animal .
}
""",
  initNs = { "vcard": vcard}
)

# Visualize the results
for r in g.query(q3):
  print(r)

"""**TASK 7.4:  List the name of the persons who know Rocky (in SPARQL only)**"""

# TO DO
from rdflib import FOAF
q4 = prepareQuery("""
PREFIX vcard: <http://www.w3.org/2001/vcard-rdf/3.0#>
PREFIX ns: <http://somewhere#>

SELECT ?person
WHERE {
  ?person a ns:Person .
  ?person foaf:knows ?Rocky .
}
""", initNs={"vcard": vcard, "foaf": FOAF})

# Visualize the results
for r in g.query(q4):
  print(r)

"""**Task 7.5: List the name of those animals who know at least another animal in the graph (in SPARQL only)**"""

# TO DO
q5 = prepareQuery("""
PREFIX vcard: <http://www.w3.org/2001/vcard-rdf/3.0#>
PREFIX ns: <http://somewhere#>

SELECT ?animal
WHERE {
  ?animal a ns:Animal .
  ?animal foaf:knows ?otherAnimal .
  ?otherAnimal a ns:Animal .
}
""", initNs={"vcard": vcard, "foaf": FOAF})

# Visualize the results
for r in g.query(q5):
    print(r)

"""**Task 7.6: List the age of all living things in descending order (in SPARQL only)**"""

# TO DO
q6 = prepareQuery("""
PREFIX ns: <http://somewhere#>

SELECT ?living ?age
WHERE {
  ?living a ns:LivingThing .
  ?LivingThing foaf:age ?age .
}
ORDER BY DESC(?age)
""", initNs={"foaf": FOAF})

# Visualize the results
for r in g.query(q6):
    print(r)