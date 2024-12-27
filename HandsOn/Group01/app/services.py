from rdflib.plugins.sparql import prepareQuery
from rdflib import Graph


g = Graph()
g.parse("../rdf/output-with-links.ttl", format="turtle")

def main_query(request):
    distrito = request.form.get("distrito", "None")
    fecha_desde = request.form.get("fecha-desde", "")
    fecha_hasta = request.form.get("fecha-hasta", "")
    tipo_accidente = request.form.get("tipo-accidente", "None")
    tipo_vehiculo = request.form.get("vehiculo", "None")
    edad_min = request.form.get("edad-min", "")
    edad_max = request.form.get("edad-max", "")
    lesividad = request.form.get("lesividad", "None")
    estado_metereologico = request.form.get("estado-meteorologico", "None")
    alcohol = request.form.get("alcohol", "None")
    droga = request.form.get("droga", "None")

    query = """
        SELECT ?x ?y ?num_expediente ?tipo_accidente ?fecha ?estado ?distrito_nombre ?distrito_url
        WHERE {
            ?accident a <http://smartcity.linkeddata.es/accidentes/ontologia/Accidente> ;
                    <http://smartcity.linkeddata.es/accidentes/ontologia/num_expediente> ?num_expediente ;
                    <http://smartcity.linkeddata.es/accidentes/ontologia/coordenada_x_utm> ?x ;
                    <http://smartcity.linkeddata.es/accidentes/ontologia/coordenada_y_utm> ?y .
            
            ?accident <http://smartcity.linkeddata.es/accidentes/ontologia/estaEnDistrito> ?distrito .
            ?distrito <http://smartcity.linkeddata.es/accidentes/ontologia/distrito> ?distrito_nombre .
            ?distrito <http://www.w3.org/2002/07/owl#sameAs> ?distrito_url .

            OPTIONAL { ?accident <http://smartcity.linkeddata.es/accidentes/ontologia/tipo_accidente> ?tipo_accidente }
            OPTIONAL { ?accident <http://smartcity.linkeddata.es/accidentes/ontologia/fecha> ?fecha }
            OPTIONAL { ?accident <http://smartcity.linkeddata.es/accidentes/ontologia/estado_meteorologico> ?estado }
    """

    filters = []

    # Add distrito-related clauses if needed
    if distrito != "None":
        filters.append(f'?distrito_nombre = "{distrito}"')

    # Add fecha if date filters exist
    if fecha_desde != "":
        filters.append(f'?fecha >= "{fecha_desde}"^^xsd:date')
    if fecha_hasta != "":
        filters.append(f'?fecha <= "{fecha_hasta}"^^xsd:date')

    # Add tipo_accidente if needed
    if tipo_accidente != "None":
        filters.append(f'?tipo_accidente = "{tipo_accidente}"')

    # Add estado_meteorologico if needed
    if estado_metereologico != "None":
        filters.append(f'?estado = "{estado_metereologico}"')

    # Add persona-related clauses only if any persona filter is active
    if any(x != "None" and x != "" for x in 
           [tipo_vehiculo, edad_min, edad_max, lesividad, alcohol, droga]):

        query += """
            ?accident <http://smartcity.linkeddata.es/accidentes/ontologia/personaInvolucrada> ?persona .
        """

        if tipo_vehiculo != "None":
            query += """
                ?persona <http://smartcity.linkeddata.es/accidentes/ontologia/tipo_vehiculo> ?tipo_vehiculo .
            """
            filters.append(f'?tipo_vehiculo = "{tipo_vehiculo}"')

        if edad_min != "" or edad_max != "":
            if edad_min != "":
                query += """
                    ?persona <http://smartcity.linkeddata.es/accidentes/ontologia/min_edad> ?min_edad .
                """
                filters.append(f"?min_edad >= {edad_min}")
            if edad_max != "":
                query += """
                    ?persona <http://smartcity.linkeddata.es/accidentes/ontologia/max_edad> ?max_edad .
                """
                filters.append(f"?max_edad <= {edad_max}")

        if lesividad != "None":
            query += """
                ?persona <http://smartcity.linkeddata.es/accidentes/ontologia/tieneLesion> ?lesion .
                ?lesion <http://smartcity.linkeddata.es/accidentes/ontologia/lesividad> ?lesividad_nombre .
            """
            filters.append(f'?lesividad_nombre = "{lesividad}"')

        if alcohol != "None":
            query += """
                ?persona <http://smartcity.linkeddata.es/accidentes/ontologia/positiva_alcohol> ?alcohol .
            """
            filters.append(f"?alcohol = {alcohol}")

        if droga != "None":
            query += """
                ?persona <http://smartcity.linkeddata.es/accidentes/ontologia/positiva_droga> ?droga .
            """
            filters.append(f"?droga = {droga}")

    # Add filters if any exist
    if filters:
        query += "FILTER(" + " && ".join(filters) + ")"

    query += "}"

    # Prepare and execute the query
    q = prepareQuery(query)

    return query, g.query(q)

def get_distritos():
    get_districts_query = prepareQuery(
        """
            SELECT DISTINCT ?distrito
            WHERE {
                ?district a <http://smartcity.linkeddata.es/accidentes/ontologia/Distrito> ;
                        <http://smartcity.linkeddata.es/accidentes/ontologia/distrito> ?distrito .
            }
            ORDER BY ?distrito
            """
    )
    return [row.distrito for row in g.query(get_districts_query)]


def get_type_accident():
    get_type_accident = prepareQuery(
        """
        SELECT DISTINCT ?tipo_accidente
        WHERE {
            ?accident a <http://smartcity.linkeddata.es/accidentes/ontologia/Accidente> ;
                    <http://smartcity.linkeddata.es/accidentes/ontologia/tipo_accidente> ?tipo_accidente .
        }
        ORDER BY ?tipo_accidente
        """
    )
    return [row.tipo_accidente for row in g.query(get_type_accident)]


def get_tipo_vehiculo():
    get_tipo_vehiculo = prepareQuery(
        """
        SELECT DISTINCT ?tipo_vehiculo
        WHERE {
            ?persona a <http://smartcity.linkeddata.es/accidentes/ontologia/Persona> ;
                    <http://smartcity.linkeddata.es/accidentes/ontologia/tipo_vehiculo> ?tipo_vehiculo .
        }
        ORDER BY ?tipo_vehiculo
        """
    )
    return [row.tipo_vehiculo for row in g.query(get_tipo_vehiculo)]


def get_lesividad():
    get_lesividad = prepareQuery(
        """
        SELECT DISTINCT ?lesividades
        WHERE {
            ?Lesividad a <http://smartcity.linkeddata.es/accidentes/ontologia/Lesividad> ;
                    <http://smartcity.linkeddata.es/accidentes/ontologia/lesividad> ?lesividades .
        }
        ORDER BY ?lesividades
        """
    )
    return [row.lesividades for row in g.query(get_lesividad)]


def get_estado_meteorologico():
    get_estado_meteorologico = prepareQuery(
        """
        SELECT DISTINCT ?estado_meteorologico
        WHERE {
            ?accident a <http://smartcity.linkeddata.es/accidentes/ontologia/Accidente> ;
                    <http://smartcity.linkeddata.es/accidentes/ontologia/estado_meteorologico> ?estado_meteorologico .
        }
        ORDER BY ?estado_meteorologico
        """
    )
    return [row.estado_meteorologico for row in g.query(get_estado_meteorologico)]
