# **Task 07: Querying RDF(s)**

github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

# First let's read the RDF file
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

g = Graph()
g.namespace_manager.bind("ns", Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind(
    "vcard", Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False
)
g.parse(github_storage + "/rdf/example6.rdf", format="xml")

# **TASK 7.1: List all subclasses of "LivingThing" with RDFLib and SPARQL**
ns = Namespace("http://somewhere#")
for s, p, o in g.triples((None, RDFS.subClassOf, ns.LivingThing)):
    print(s)

print("----")

q1 = """
SELECT ?subclass
WHERE {
    ?subclass rdfs:subClassOf ns:LivingThing .
}
"""
for r in g.query(q1):
    print(r.subclass)

# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
q2 = """
SELECT ?individual WHERE {
	?individual rdf:type ?a .
    ?a rdfs:subClassOf* ns:Person
}
"""

for r in g.query(q2):
    print(r.individual)

# **TASK 7.3: List all individuals of just "Person" or "Animal". You do not need to list the individuals of the subclasses of person (in SPARQL only)**
q3 = """
SELECT DISTINCT ?individual WHERE {
    { ?individual rdf:type ns:Person . }
    UNION
    { ?individual rdf:type ns:Animal . }
}
"""
for r in g.query(q3):
    print(r.individual)

# **TASK 7.4:  List the name of the persons who know Rocky (in SPARQL only)**

from rdflib.namespace import FOAF
from rdflib.plugins.sparql import prepareQuery

VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")

q4 = prepareQuery(
    """
    SELECT ?name WHERE {
        ?person rdf:type ns:Person .
        ?person foaf:knows ns:RockySmith .
        ?person vcard:FN ?name.
    }
	""",
    initNs={"rdf": RDF, "foaf": FOAF, "vcard": VCARD, "ns": ns},
)

for r in g.query(q4):
    print(r.name)

# **Task 7.5: List the name of those animals who know at least another animal in the graph (in SPARQL only)**

q5 = prepareQuery(
    """
    SELECT ?name WHERE {
      	?animal rdf:type ns:Animal .
        ?animal foaf:knows ?animal2 .
        ?animal2 rdf:type ns:Animal .
        ?animal vcard:FN ?name .
    }
	""",
    initNs={"rdf": RDF, "foaf": FOAF, "vcard": VCARD, "ns": ns},
)

for r in g.query(q5):
    print(r.name)

# **Task 7.6: List the age of all living things in descending order (in SPARQL only)**

q6 = prepareQuery(
    """
	SELECT ?name ?age WHERE {
		?thing rdf:type/rdfs:subClassOf* ns:LivingThing .
		?thing vcard:FN ?name .
		?thing foaf:age ?age .
	}
	ORDER BY DESC(?age)
	""",
    initNs={"rdf": RDF, "foaf": FOAF, "vcard": VCARD, "ns": ns},
)

for r in g.query(q6):
    print(r.name, r.age)
