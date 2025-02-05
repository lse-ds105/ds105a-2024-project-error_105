import os
import json
import ee
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def authenticate_earth_engine():
    """
    Authenticate with Google Earth Engine using a service account stored in .env.
    """
    try:
        # Retrieve credentials from environment variables
        service_account = os.getenv("GEE_SERVICE_ACCOUNT")
        key_path = os.getenv("GEE_PRIVATE_KEY_PATH")

        if not service_account or not key_path:
            raise ValueError("Missing Earth Engine credentials. Check your .env file.")

        # Authenticate with Earth Engine
        credentials = ee.ServiceAccountCredentials(service_account, key_path)
        ee.Initialize(credentials)
        print("Successfully authenticated with Google Earth Engine.")
    except Exception as e:
        print(f"Error during authentication: {e}")

def process_biome_batch(ecoregions, biome_names, combined_data, batch_num, total_batches):
    """
    Process a batch of biomes and extract centroids for each ecoregion.
    """
    print(f"\n[Batch {batch_num}/{total_batches}] Processing biomes: {', '.join(biome_names)}")

    # Filter the dataset to include only the specified biomes
    selected_biomes = ecoregions.filter(ee.Filter.inList("BIOME_NAME", biome_names))
    
    # Map through each feature and extract necessary data
    def extract_centroid_data(feature):
        biome_name = feature.get("BIOME_NAME")
        ecoregion_name = feature.get("ECO_NAME")
        centroid = feature.geometry().centroid().coordinates()
        return ee.Feature(None, {
            "BIOME_NAME": biome_name,
            "ECO_NAME": ecoregion_name,
            "centroid": centroid
        })

    # Compute centroids and extract data
    processed_features = selected_biomes.map(extract_centroid_data).getInfo()

    # Store the processed data in the combined dataset
    biome_counts = {}
    for feature in processed_features["features"]:
        properties = feature["properties"]
        biome_name = properties["BIOME_NAME"]
        ecoregion_name = properties["ECO_NAME"]
        centroid = properties["centroid"]
        
        if biome_name not in combined_data:
            combined_data[biome_name] = {}
        combined_data[biome_name][ecoregion_name] = {"centroid": centroid[::-1]}  # Reverse to [lat, lon]

        # Track counts for print summary
        biome_counts[biome_name] = biome_counts.get(biome_name, 0) + 1

    # Print summary for this batch
    for biome_name, count in biome_counts.items():
        print(f"  - {biome_name}: {count} ecoregions processed.")

def main():
    # Default output directory and filename
    output_dir = "data/biomes_data"
    output_filename = "Ecoregions_Coordinates.json"

    # Build the full output file path
    output_file = os.path.join(output_dir, output_filename)

    # Ensure the directory exists
    os.makedirs(output_dir, exist_ok=True)

    print(f"Output will be saved to: {output_file}")

    # Authenticate with Earth Engine
    authenticate_earth_engine()

    # Load the RESOLVE Ecoregions 2017 dataset
    ecoregions = ee.FeatureCollection("RESOLVE/ECOREGIONS/2017")
    
    # Initialize combined dataset
    combined_biome_data = {}

    # Get a list of unique biome names, excluding N/A values
    biomes = ecoregions.aggregate_array("BIOME_NAME").distinct().getInfo()
    valid_biomes = [biome for biome in biomes if biome not in [None, "N/A"]]  # Skip invalid entries

    # Process biomes in batches
    batch_size = 5  # Default batch size
    total_batches = (len(valid_biomes) + batch_size - 1) // batch_size  # Calculate total number of batches
    total_biomes_processed = 0

    for i in range(0, len(valid_biomes), batch_size):
        biome_batch = valid_biomes[i:i + batch_size]
        try:
            process_biome_batch(ecoregions, biome_batch, combined_biome_data, i // batch_size + 1, total_batches)
            total_biomes_processed += len(biome_batch)
        except Exception as e:
            print(f"Error processing batch {i // batch_size + 1}: {e}")

    # Save the combined data to a JSON file
    with open(output_file, "w") as json_file:
        json.dump(combined_biome_data, json_file, indent=4)

    # Final summary
    print(f"\n=== Processing Completed ===")
    print(f"Total biomes processed: {total_biomes_processed}")
    print(f"Output saved to: {output_file}")

if __name__ == "__main__":
    main()
