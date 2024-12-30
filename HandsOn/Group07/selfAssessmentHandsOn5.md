# Group Assessment – Hands-on Assignment 5

## 1. RDF Files
- **Requirement**: Each RDF file contains at least one `owl:sameAs` property.
  - **Self-Assessment**: ✔️ Met
  - **Comments**: Each RDF file in the dataset successfully includes at least one `owl:sameAs` property, linking internal resources to resources in external datasets to ensure semantic integration.

## 2. owl:sameAs Property Usage
- **Requirement**: Every `owl:sameAs` property links a resource in our dataset with another resource in an external dataset.
  - **Self-Assessment**: ✔️ Met
  - **Comments**: All `owl:sameAs` properties have been used to establish connections between our RDF resources and relevant external datasets, improving data enrichment and interoperability with external ontologies.

## 3. SPARQL File Requirements
- **Requirement**: The SPARQL file includes at least one query that retrieves necessary application data.
  - **Self-Assessment**: ✔️ Met
  - **Comments**: The SPARQL file contains multiple queries, each designed to retrieve data that is essential for the application. These queries cover data required for different functionalities within the application, ensuring the dataset’s applicability.

## 4. SPARQL Query Requirements
- **Requirement**: Each SPARQL query:
  - Utilizes the ontology.
  - Returns a non-empty result.
  - Makes use of the `owl:sameAs` links.
  - **Self-Assessment**: ✔️ Met
  - **Comments**: Each SPARQL query integrates the ontology effectively, returning relevant, non-empty results. The queries also leverage `owl:sameAs` links to retrieve enriched data from both internal and external datasets, ensuring comprehensive data retrieval and alignment with the ontology.

## Overall Summary
- **Assessment Summary**: All requirements for the assignment are met. Each RDF and SPARQL component is designed according to the specifications, ensuring proper linkage, ontology use, and data retrieval aligned with the `owl:sameAs` integrations.
- **Improvements**: Consider adding additional `owl:sameAs` properties to extend connections with a broader range of external datasets, further enhancing data enrichment potential.
- **Observations**: Despite our efforts to increase data alignment, we encountered limitations in further reconciliation with external datasets. We attempted multiple columns for matching criteria, but were unable to establish additional `owl:sameAs` links.