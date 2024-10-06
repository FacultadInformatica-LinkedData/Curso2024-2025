# %% [markdown]
# **Task 07: Querying RDF(s)**

# %%
!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

# %% [markdown]
# First let's read the RDF file

# %%
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

# Add the namespace and import the usage of SPARQL
ns = Namespace("http://somewhere#")
from rdflib.plugins.sparql import prepareQuery

# %% [markdown]
# **TASK 7.1: List all subclasses of "LivingThing" with RDFLib and SPARQL**

# %%
# TO DO
# Visualize the results
for s, p, o in g.triples((None, RDFS.subClassOf, ns.LivingThing)):  # Cambiar ns.Person a ns.LivingThing
    print(s)
print("\n")

#for r in g.query(q1):
#  print(r)
query = prepareQuery("""SELECT ?s WHERE { ?s rdfs:subClassOf ns:LivingThing }""", initNs={"rdfs": RDFS, "ns": ns})
for data in g.query(query):
    print(data)

# %% [markdown]
# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# %%
# TO DO
# Visualize the results

for s, p, o in g.triples((None, RDF.type, ns.Person)):
    print(s)
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    for s2, p2, o2 in g.triples((None, RDF.type, s)):
        print(s2)
print("\n")
q2 = prepareQuery("""select ?s where { {?s rdf:type ns:Person} union {?s2 rdfs:subClassOf ns:Person. ?s rdf:type ?s2} }""", initNs={"rdfs": RDFS, "ns": ns, "rdf": RDF})
for data in g.query(q2):
    print(data)

# %% [markdown]
# **TASK 7.3: List all individuals of just "Person" or "Animal". You do not need to list the individuals of the subclasses of person (in SPARQL only)**
# 

# %%
from rdflib.plugins.sparql import prepareQuery

# Define the query
q3 = prepareQuery("""
    SELECT ?s WHERE {
        { ?s rdf:type ns:Person }
        UNION
        { ?s rdf:type ns:Animal }
    }
""", initNs={"rdf": RDF, "ns": ns})

# Execute the query and visualize the results
for data in g.query(q3):
    print(data)


# %% [markdown]
# **TASK 7.4:  List the name of the persons who know Rocky (in SPARQL only)**

# %%
# Define the query
q4 = prepareQuery("""
    SELECT ?name WHERE {
        ?person rdf:type ns:Person .
        ?person ns:knows ns:Rocky .
        ?person vcard:FN ?name .
    }
""", initNs={"rdf": RDF, "ns": ns, "vcard": Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")})

# Execute the query and visualize the results
for data in g.query(q4):
    print(data)


# %% [markdown]
# **Task 7.5: List the name of those animals who know at least another animal in the graph (in SPARQL only)**

# %%
# Define the query
q5 = prepareQuery("""
    SELECT ?name WHERE {
        ?animal rdf:type ns:Animal .
        ?animal ns:knows ?otherAnimal .
        ?otherAnimal rdf:type ns:Animal .
        ?animal vcard:FN ?name .
    }
""", initNs={"rdf": RDF, "ns": ns, "vcard": Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")})

# Execute the query and visualize the results
for data in g.query(q5):
    print(data)

# %% [markdown]
# **Task 7.6: List the age of all living things in descending order (in SPARQL only)**

# %%
# Define the query
q6 = prepareQuery("""
    SELECT ?livingThing ?age WHERE {
        ?livingThing rdf:type ns:LivingThing .
        ?livingThing ns:age ?age .
    }
    ORDER BY DESC(?age)
""", initNs={"rdf": RDF, "ns": ns})

# Execute the query and visualize the results
for data in g.query(q6):
    print(data)


