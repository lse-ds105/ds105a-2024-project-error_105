[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_SwzfpU1)

# Pokemon in the Real World

## Description
The goal of our project is to analyse the data of Pokemon, and map it to locations in the real world by referencing weather data. Due to time constraints, we have focused on 3 primary types: fire, ice and water. The final product of our project is a map where one can see the locations of the Pokemon. 

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

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
### **Running the Python Script**

To run the `process_biomes.py` script, open your terminal and navigate to the directory where the `proess_biomes.py` script is located. Then, use the following command:

```bash
python your_script_name.py
```

## Data Sources 

## Project Structure 
```bash
/project-root
├── data/                 
│   ├── biomes_data/           # Biomes data files
│   ├── pokemon_data/          # Pokémon data files
│   ├── weather_data/          # Weather data files
│   └── main.db                # SQL Tables
├── code/              
│   ├── data_collection/       # Code for data collection
│   ├── data_processing/       # Code for data processing
│   └── Data Visualisation/    # Code for generating visualizations
│
├── map/                       # Maps and visualizations
├── docs/                      # GitHub Pages entry point, assorted diagrams and media files
├── README.md                  # Project documentation
└── requirements.txt           # Dependencies
```




