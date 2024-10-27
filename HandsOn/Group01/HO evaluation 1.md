1
    Analysis
    Ontology
        - The XML schema datatypes must be written in lowercase
    RDF data
        - You are using the same resources to represent all the involved people (personaInvolucrada). Check those instances (Conductor, etc.).
        - Something similar happens with the instances of Localizacion.
        - Accidents have more than one value for the tieneLesion property. Is this correct? How do you know who has which lesion? (if the dataset mentions it)
        - You don't need to create classes for everything. If some class just describes its instances with a string (or a date), you could directly put that string in a datatype property.
    Take into account that the review has been performed over a previous version of the hands-on. Some of the defects found may have been already fixed.
