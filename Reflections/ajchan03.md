# Individual Reflection

## Table of Contents
1. [Technical Contributions](#technical-contributions)
2. [Team Collaboration](#team-collaboration)
3. [Learning Journey](#learning-journey)

---

# Technical Contributions

## Specific Code/Features Developed
- **Data Visualisation**: Main contributor to the initial iterations of the interactive map. Implemented Vignesh' heatmap overlay, created code to show Pokemon as icons appearing on the map. Identiifed issues with typos appearing in API; fixed them using rudimentary autocorrect before replacing it with a more rigorous method.
  

  **Evidence**:  
  
  - [Link to feature branch of first iteration of map on GitHub](https://github.com/lse-ds105/ds105a-2024-project-error_105/tree/WorldMap)
  - [Link to feature branch of second iteration of map on GitHub](https://github.com/lse-ds105/ds105a-2024-project-error_105/tree/Data_Visualisation)

  
  - Map progression
    ![First iteration](../Reflections/supporting_evidence_adrian/first_iteration.png)
    ![Second iteration](../Reflections/supporting_evidence_adrian/second_iteration.png)

   

- **Search Bar Feature**: Used a GeoJson object containing all Pokemon locations and names to implement a search bar that identified and indicated where the searched Pokemon was with a flashing red dot. Encountered difficulties due to numerous bugs with the Search plugin; found workarounds for all but one.
  
  **Evidence**:  
  - [Link to `NB3B - Map.py` on GitHub](https://github.com/lse-ds105/ds105a-2024-project-error_105/blob/main/code/data_collection/process_biomes.py)  

  - Code snippet from search bar section; needed to transform original data into data format due to bug in the plugin:  
    ```python
    geojson_data = {
    "type": "FeatureCollection",
    "features": []
}
# Transform the original data into GeoJson data format
for item in pokemon_features:
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": item['geometry']['coordinates']
        },
        "properties": {
            "name": item['properties']['name']
        }
    }
    geojson_data["features"].append(feature)
    ```


- **Webpage Design**: Designed the 'Data Sources' section. Included descriptions of how we used each source along with API keys and limitations.

  **Evidence**:  
  - [Sources page](https://lse-ds105.github.io/ds105a-2024-project-error_105/sources.html)  


## Problems Solved
- 


## Technical Decisions Influenced
- Map design decisions such as using Icons in place of names
- Introduction of search bar
---

# Team Collaboration

## Role in Team Coordination
- Scheduled meetings, and helped with the assignation of tasks

  **Evidence**:
![Screenshot of meeting](../Reflections/supporting_evidence_adrian/meeting.png)

## How I Supported Team Members
- Assisted teammates with tasks, helping them realise their vision of the map
- Gave support in cases where clarity was required

## Conflict Resolution Examples
- Our team worked smoothly across these weeks.

---

## Learning Journey

### Skills Developed

- **Coding Conventions:** Developed correct coding conventions.

- **Python:** Developed skills regarding transforming data structures and wider data analysis, and learnt how to create interactive maps with Folium.

- **HTML/CSS & JavaScript:** Developed JavaScript skills due to bug with search bar, trying to inject Javascript into the map HTML to manually disable a layer that was not aestheticallly pleasing (ultimately unsucessfully). Also honed HTML Skills in creating a webpage.


### Challenges Overcome
- **Debugging**: Found workaround to Folium's Search plugin bug by reshaping data structure 


### Areas for Future Growth
- **Leadership**: Develop better leadership skills in guiding team members through technical challenges, decision-making, and feature implementation. Set clear goals and step up in project coordination to drive progress effectively.
- **Natural Language Processing Toolkit** Initially wanted use this to classify Pokemon, but abandoned due to unfamiliarity. Would like to advance my skill in this area.
---
