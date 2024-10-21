# Self-Assessment for Hands-on 2

## Group Information:
- **Group Name**: Group06
- **Members**: Juan Sebastian Torres Alvarez, Alberto Aragon Calvo, Rodrigo Allende Rial, Miguel Carrallo

## Evaluation Criteria:
### 1. Dataset Analysis:
We performed an in-depth analysis of the Alumbrado Público dataset, focusing on the structure, schema, and licensing. The data is well-structured, and the open license allows for its transformation into RDF and publication.

### 2. Resource Naming Strategy:
The URI structure and content negotiation strategy were defined clearly. The use of `/city/lighting/{id}` ensures a simple and understandable URI pattern for the resources.

### 3. Ontology Development:
We successfully created a lightweight ontology for the streetlight data, with classes such as `Streetlight`, `Location`, and `Type`. We encountered no significant issues during the ontology design.

### 4. RDF Example:
An RDF file was generated, showing how the streetlight data is transformed into RDF. The instances follow the defined ontology structure.

## Lessons Learned:
- The importance of a clear URI naming strategy to ensure resource discoverability.
- How to develop a lightweight ontology based on real-world data.
- The challenges of transforming a CSV dataset into RDF.

## Next Steps:
- Expand the ontology to include additional properties, such as maintenance schedules.
- Link the dataset with other city infrastructure datasets to provide a more comprehensive view of city services.
