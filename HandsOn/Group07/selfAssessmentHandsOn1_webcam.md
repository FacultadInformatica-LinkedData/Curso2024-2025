
## Dataset Selection
The selected dataset is the [Webcam Dataset](https://datos.gob.es/es/catalogo/l03380010-webcam). We chose this dataset because it fits within the smart city domain by providing real-time webcam data that can be used for monitoring traffic, weather, and tourism hotspots in urban environments.

### Dataset Requirements Satisfaction
1. **R1 (Smart city domain)**: The dataset provides webcam data which can be applied to domains such as traffic monitoring, weather observation, and tourism insights. It is highly relevant to smart city applications.
2. **R2 (CSV format)**: The dataset is available in CSV format, making it easy to process and integrate into various systems.
3. **R3 (Open license)**: The dataset is openly licensed, ensuring it can be reused and republished freely.
4. **R4 (Linkable to real-world entities)**: The data includes webcam locations, allowing it to be linked with geographic entities such as streets, regions, or cities.

### Optional Requirements
- **R5 (Documentation)**: The dataset includes limited documentation, but it provides sufficient metadata to understand its structure and potential uses. Therefore, it partially satisfies this requirement.
- **R6 (Multiple data sources)**: The dataset comes from a single source (Spanish government open data portal), and thus does not satisfy the optional requirement of incorporating data from multiple sources.

## Application Design
We plan to build an interactive application that provides real-time access to webcam feeds, displayed on an interactive map. The application will include:
- A map showing the locations of webcams.
- Clicking on a webcam marker will display real-time video or recorded footage.
- Filters will be available to categorize the webcams by region, type (e.g., traffic, weather), or other attributes.

The application will also integrate additional information such as weather or traffic APIs to provide a richer user experience.

## Self-Evaluation
We believe we have met the core requirements of this assignment:
- We selected a dataset that fits the course objectives and meets the primary requirements (R1 to R4).
- We designed an application that leverages the dataset to build a practical, real-world solution for monitoring smart cities.
- The optional requirements (R5 and R6) were discussed and evaluated, and although R6 is not fully met, we acknowledge this and will explore ways to address it in future tasks.

Overall, this hands-on has provided us with valuable insights into dataset selection and application design using open data in smart city contexts.
