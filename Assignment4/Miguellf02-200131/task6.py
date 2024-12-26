# -*- coding: utf-8 -*-


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"
g.parse(github_storage+"/rdf/example5.rdf", format="xml")

ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))

print("\n### After adding Researcher class ###\n")
for s, p, o in g:
    print(s, p, o)

# TASK 6.1: 
g.add((ns.School, RDF.type, RDFS.Class))
g.add((ns.School, RDFS.label, Literal("Escuela", lang="es")))

g.add((ns.University, RDF.type, RDFS.Class))
g.add((ns.University, RDFS.label, Literal("Universidad", lang="es")))

print("\n### After adding School and University classes ###\n")
for s, p, o in g:
    print(s, p, o)

# TASK 6.2: 
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))

print("\n### After adding Researcher as subclass of Person ###\n")
for s, p, o in g:
    print(s, p, o)

# TASK 6.3: 
g.add((ns.JaneSmithers, RDF.type, ns.Researcher))

print("\n### After adding individual Jane Smithers ###\n")
for s, p, o in g:
    print(s, p, o)

# TASK 6.4: 
schema = Namespace("https://schema.org/")
g.add((ns.JaneSmithers, schema.email, Literal("jane.smithers@example.org")))
g.add((ns.JaneSmithers, schema.fullName, Literal("Jane Smithers")))
g.add((ns.JaneSmithers, schema.givenName, Literal("Jane")))
g.add((ns.JaneSmithers, schema.familyName, Literal("Smithers")))

print("\n### After adding details to Jane Smithers ###\n")
for s, p, o in g:
    print(s, p, o)

# TASK 6.5: 
example = Namespace("https://example.org/")
g.add((ns.JohnSmith, example.worksAt, example.UPM))

print("\n### After adding John Smith's university ###\n")
for s, p, o in g:
    print(s, p, o)

# TASK 6.6: 
foaf = Namespace("http://xmlns.com/foaf/0.1/")
g.add((ns.JohnSmith, foaf.knows, ns.JaneSmithers))

print("\n### After adding that John knows Jane ###\n")
for s, p, o in g:
    print(s, p, o)

