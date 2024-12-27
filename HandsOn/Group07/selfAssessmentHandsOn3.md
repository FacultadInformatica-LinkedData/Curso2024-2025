# Self-Assessment for Hands-on 3

## Group Information
- **Group Name**: Group06
- **Members**: Juan Sebastian Torres Alvarez, Alberto Aragon Calvo, Rodrigo Allende Rial, Miguel Carrallo


---

## Objective
The goal of this task was to become familiar with cleaning and preparing CSV data using OpenRefine. We selected our dataset, imported it into OpenRefine, analyzed it to identify errors, and then applied several transformations to prepare it for RDF generation.

---

## Process Overview

### 1. **Data Import**
We imported the selected CSV dataset into OpenRefine. The dataset contained information about [describe dataset, e.g., "city infrastructure data related to street lighting"]. The import process was smooth, and OpenRefine correctly identified all columns and data types.

### 2. **Data Analysis and Cleaning**
In this stage, we performed an analysis of the dataset to find inconsistencies, errors, and opportunities for improvement. The initial analysis had already been done in a previous class, but we updated it based on the following findings:
- **Missing values**: Several rows were missing critical data (e.g., geographic coordinates for street lights).
- **Inconsistent formats**: Date fields and numerical values were not standardized, requiring uniform transformation.
- **Duplicate entries**: We identified and removed duplicate rows.

Using OpenRefine’s functions, we fixed these issues. The key transformations applied include:
- Normalizing date formats to YYYY-MM-DD.
- Standardizing numerical values (e.g., converting all power consumption data to watts).
- Cleaning text fields to ensure consistent casing (e.g., all street names are capitalized).
- Removing duplicates based on specific identifiers.

### 3. **Data Transformation**
We transformed the dataset to be more RDF-friendly, preparing it for future integration. This included:
- Reformatting the structure of the CSV to ensure ease of conversion to RDF triples.
- Ensuring that key columns (such as streetlight ID and location) could be easily linked to external datasets using URIs.

### 4. **Exporting Results**
After completing the data cleaning and transformation, we exported the updated dataset as a CSV file and saved the transformation operations as a JSON file. These files are included in the GitHub repository as part of the final deliverables.

---

## Challenges Encountered

- **Handling missing values**: We initially faced difficulties deciding how to handle missing data, especially in crucial fields like geographic coordinates. Ultimately, we chose to omit rows where data was incomplete.
- **Normalizing data formats**: Ensuring consistency across date formats and numerical values required us to experiment with different OpenRefine functions before achieving the desired result.
- **Version control**: Ensuring that everyone in the group applied the same transformations and kept up with the versioning in GitHub was a challenge. We overcame this by documenting our steps carefully in the JSON file.

---

## Team Collaboration

The team worked together effectively throughout the project:
- **Juan Sebastian Torres Alvarez** focused on importing the data and managing the transformation process.
- **Juan Sebastian Torres Alvarez** was responsible for analyzing and identifying errors in the dataset.
- **Rodrigo Allende Rial** helped implement the cleaning functions in OpenRefine and reviewed the final output.

We collaborated using GitHub to track changes and ensure that the final deliverables were uploaded correctly.

---

## Conclusion

This task gave us valuable hands-on experience with OpenRefine and its data cleaning capabilities. The transformations we applied will significantly aid in the RDF generation process for our dataset, making it more interoperable with other datasets.

---

## Lessons Learned

- The importance of maintaining consistency in data formats across large datasets.
- How to leverage OpenRefine’s powerful functions to clean and transform data quickly.
- Effective collaboration and communication within the team to ensure the task was completed on time.

---

## Next Steps

- Integrate the cleaned dataset into RDF format.
- Explore potential links between our dataset and other external data sources to enhance interoperability.

---

