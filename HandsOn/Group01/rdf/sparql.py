from rdflib import Graph
from rdflib.plugins.sparql import prepareQuery

g = Graph()

g.parse("./output.ttl", format="turtle")

# # q1: obtenemos los 10 primeros accidentes
# q1 = prepareQuery(
#     """
#     SELECT ?accident
#     WHERE {
#         ?accident a <http://smartcity.linkeddata.es/accidentes/ontologia/Accidente> .
#     }
#     LIMIT 10
#   """,
# )

# for r in g.query(q1):
#     print(r)


# q3: buscamos los 10 primeros accidentes que ocurrieron en el distrito 
q3 = prepareQuery(
    """
    SELECT ?accident
    WHERE {
        ?accident a <http://smartcity.linkeddata.es/accidentes/ontologia/Accidente> ;
                <http://smartcity.linkeddata.es/accidentes/ontologia/estaEnDistrito> ?district .
        ?district <http://smartcity.linkeddata.es/accidentes/ontologia/cod_distrito> ?cod_distrito .
        FILTER(?cod_distrito = 5)
    }
    LIMIT 10
  """,
)

for r in g.query(q3):
    print(r)


# q2 = prepareQuery(
#     """
#     SELECT ?accident
#     WHERE {
#         ?accident a <http://smartcity.linkeddata.es/accidentes/ontologia/Accidente> ;
#                 <http://smartcity.linkeddata.es/accidentes/ontologia/tipo_accidente> ?type .
#         FILTER(?type = "Colisión fronto-lateral")
#     }
#     LIMIT 10
#   """,
# )

# for r in g.query(q2):
#     print(r)
