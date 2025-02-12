[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_SwzfpU1)

# Pokémon in the Real World

## Description
The goal of our project is to analyse the data of Pokémon, and map it to locations in the real world by referencing weather data. Due to time constraints, we have focused on 3 primary types: fire, ice and water. The final product of our project is a map where one can see the locations of the Pokémon. 

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Project Structure](#project-structure)
- [Search Bar Bug](#search-bar-bug-in-map)

## Installation
Provide instructions on how to set up the project.
### Step 1: Cloning Repository
```bash
git clone git@github.com:lse-ds105/ds105a-2024-project-error_105.git
```

This will download the repository's content to a folder named ds105a-2024-project-error_105 in your current working directory.
### Step 2: Set Up a Virtual Environment
A virtual environment helps isolate project dependencies and avoid conflicts. This set of bash commands assumes that user is already operating from base folder of repository. If you are not already in directory is named 'ds105a-2024-project_105'(to be copy pasted to access directory!)
   ```bash
   cd /path/to/ds105a-2024-project_105
   ```
1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
(.venv) should appear in terminal prompt at this stage!

3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure same kernel (.venv) is used when running jupyter notebooks!

### Step 3: Set Up Your Service Account
To run the code, you will need to set up your own Google Cloud service account for authentication.

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or use an existing one.
3. Navigate to **IAM & Admin** > **Service Accounts**.
4. Create a new service account and grant it appropriate permissions for accessing your resources.
5. Download the JSON key for the service account.
6. Save the JSON file as `service-account.json` in the root directory of the project.

### Step 4: Set Up Your `.env` File
The `.env` file is used to store sensitive information like API credentials securely.

Set up your environment variables in a `.env` file at the root of the repository. The code below will copy the template file to a new `.env` file.

```bash
cp .env.template .env
```

## Usage
### Sequence of Running the Notebooks  

To ensure accurate results, the notebooks must be executed in the following order:  

```bash
NB1A → NB2A → NB3A → NB1B → NB1C → NB2C → NB3B → NB3C
```  

**Note:** Running the notebooks in a different order may lead to errors.

### **Running the Python Script (NB1B)**

To run the `NB1B - process_biomes.py` script, open your terminal and navigate to the directory where the `NB1B - proess_biomes.py` script is located. Then, use the following command:

```bash
python "NB1B - process_biomes.py"
```

Note! It is important to use **double quotes** to ensure that the script is run properly. 

## Data Sources 

We have three main data sources. 
1. [PokeAPI](https://pokeapi.co/docs/v2) - for Pokémon data. 
2. [RESOLVE Ecoregions 2017](https://developers.google.com/earth-engine/datasets/catalog/RESOLVE_ECOREGIONS_2017) - for biome and location data. 
3. [Open-Meteo](https://open-meteo.com/) - for various types of meteorological data. 


## Project Structure 
```bash
/project-root
├── code/              
│   ├── data_collection/       # Code for data collection
│   ├── data_processing/       # Code for data processing
│   └── data_visualisation/    # Code for generating visualizations
├── data/                 
│   ├── biomes_data/           # Biomes data files
│   ├── pokemon_data/          # Pokémon data files
│   ├── weather_data/          # Weather data files
│   └── main.db                # SQL Tables
├── docs/                      # GitHub Pages entry point, assorted diagrams and media files
├── reflections/    
├── visuals/
│   ├── biomes_data/           # Biomes data files
│   └── pokemon_data/          # Pokémon data files    
├── .env.template              # Sample .env file
├── .gitignore                 # Files for GitHub to not track
├── README.md                  # Project documentation
└── requirements.txt           # Dependencies
```

## Search bar bug in map

Our map, when initialised, shows many blue markers that have to be disabled manually via clicking the "Pokemon Locations" layer in the map. This is due to a bug in the Search plugin of Folium.

To implement a search bar, we have to create a GeoJson layer that contains all Pokemon locations for the search bar to browse through. This leads to default blue markers popping up in all these locations. Without a search bar, we can remove these marker prior to initialisation by passing the "Show = False" argument for layers.

However, this argument is overridden when the search bar is implemented, which leads to the default blue markers showing up. We've tried many solutions, including trying to make the blue markers transparent and injecting JavaScript to manually disable this layer, but to no avail.


