# -*- coding: utf-8 -*-
"""Task08.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LfCDubpIL2Q6xaIjLyFx1Dk-2QFWZhNb

**Task 08: Completing missing data**
"""

!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

from rdflib import Graph, Namespace, Literal, URIRef
g1 = Graph()
g2 = Graph()
g1.parse(github_storage+"/rdf/data01.rdf", format="xml")
g2.parse(github_storage+"/rdf/data02.rdf", format="xml")

"""Tarea: lista todos los elementos de la clase Person en el primer grafo (data01.rdf) y completa los campos (given name, family name y email) que puedan faltar con los datos del segundo grafo (data02.rdf). Puedes usar consultas SPARQL o iterar el grafo, o ambas cosas."""

from rdflib.namespace import RDF, RDFS
from rdflib import Namespace

VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
ns = Namespace("http://data.org#")

#we create list in which we will save information from graph g2
#the key will be the person's URI. Every person in g1 already has a definded URI
given_names = {}
family_names = {}
emails = {}

for s, p, o in g2:
    if p == VCARD.Given:
        given_names[s] = str(o)
    elif p == VCARD.Family:
        family_names[s] = str(o)
    elif p == VCARD.EMAIL:
        emails[s] = str(o)

for person in g1.subjects(RDF.type, ns.Person):
    if not (person, VCARD.Given, None) in g1:
        if person in given_names:
            g1.add((person, VCARD.Given, Literal(given_names[person])))

    if not (person, VCARD.Family, None) in g1:
        if person in family_names:
            g1.add((person, VCARD.Family, Literal(family_names[person])))

    if not (person, VCARD.EMAIL, None) in g1:
        if person in emails:
            g1.add((person, VCARD.EMAIL, Literal(emails[person])))

for s, p, o in g1:
    print(s, p, o)