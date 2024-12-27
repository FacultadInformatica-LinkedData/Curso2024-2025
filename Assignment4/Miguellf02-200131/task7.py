# -*- coding: utf-8 -*-


!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

# TASK 7.1: 
q1 = """
    SELECT ?subclass WHERE {
        ?subclass rdfs:subClassOf ns:LivingThing .
    }
"""
for r in g.query(q1):
    print(f"Subclass: {r.subclass}")

# TASK 7.2: 
q2 = """
    SELECT ?individual WHERE {
        ?individual rdf:type ns:Person .
        ?subclass rdfs:subClassOf ns:Person .
    }
"""
for r in g.query(q2):
    print(f"Individual of Person or Subclass: {r.individual}")

# TASK 7.3: 
q3 = """
    SELECT ?individual WHERE {
        ?individual rdf:type ns:Person .
        UNION
        ?individual rdf:type ns:Animal .
    }
"""
for r in g.query(q3):
    print(f"Individual of Person or Animal: {r.individual}")

# TASK 7.4: 
q4 = """
    SELECT ?name WHERE {
        ?person rdf:type ns:Person .
        ?person ns:knows ns:Rocky .
        ?person vcard:FN ?name .
    }
"""
for r in g.query(q4):
    print(f"Person who knows Rocky: {r.name}")

# TASK 7.5: 
q5 = """
    SELECT ?animalName WHERE {
        ?animal rdf:type ns:Animal .
        ?animal ns:knows ?anotherAnimal .
        ?anotherAnimal rdf:type ns:Animal .
        ?animal vcard:FN ?animalName .
    }
"""
for r in g.query(q5):
    print(f"Animal who knows another animal: {r.animalName}")

# TASK 7.6: 
q6 = """
    SELECT ?livingThing ?age WHERE {
        ?livingThing rdf:type ns:LivingThing .
        ?livingThing ns:age ?age .
    }
    ORDER BY DESC(?age)
"""
for r in g.query(q6):
    print(f"LivingThing: {r.livingThing}, Age: {r.age}")
