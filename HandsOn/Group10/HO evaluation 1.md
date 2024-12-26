10
    Analysis
        - The analysis.html file does not contain the license of the dataset to be generated.
    Ontology
        - The XML schema datatypes must be written in lowercase.
        - Some XML schema datatypes have a wrong namespace.
        - In OWL, there are object properties (where value of the property is a resource) and datatype properties (where the value of the property is a string literal, usually typed). 
        - The domain and/or range of some property is not defined.
        - In OWL, having multiple domains (or ranges) means that the domain (or range) is the intersection of all the classes.  The current definitions of properties with multiple domains are wrong.
        - Parking is defined as a class and as a property.
    RDF data
    Take into account that the review has been performed over a previous version of the hands-on. Some of the defects found may have been already fixed.
