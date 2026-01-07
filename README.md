# US Wildlife Habitat Connectivity Analysis

This project analyzes wildlife habitat connectivity across the **U.S. portion of the Yellowstone-to-Yukon (Y2Y) corridor**.  
In the future, I plan on extending the analysis to the full Y2Y region (includes both U.S. and Canada).

## Study Region

The study region is the **intersection of the Yellowstone-to-Yukon (Y2Y) corridor and the United States national boundary**. This region includes parts of Montana, Idaho, Wyoming, Washington, and Oregon.

Raw boundary inputs are stored as GeoJSON files:
- Y2Y corridor boundary: `data/raw/boundaries/y2y_boundary.geojson`
- U.S. national boundary: `data/raw/boundaries/us_boundary.geojson`

The script `src/build_boundary.py` finds the intersection of these boundaries and then saves the study region to the `data/processed` directory. All datasets will be clipped to this boundary.