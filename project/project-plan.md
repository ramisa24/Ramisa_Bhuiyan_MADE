# Project Plan

## Title

A Data-Driven Investigation of Crime and Arrest Disparities

## Main Question

Which neighborhoods or regions have the highest disparities between crime reports and arrests?

## Description

This project will focus on locations and types of crime where crime is reported often but arrests are few, hence possible under policing or lack of adequate resources. The eventual use of the maps is to help the policymaker gain informed insights of disparities that exist in the policies implemented by the police.

## Datasources

### Datasource1: Crime Data
- Metadata URL: https://catalog.data.gov/dataset/crime-data-from-2020-to-present
- URL: https://data.lacity.org/api/views/2nrs-mtv8/rows.csv?accessType=DOWNLOAD
- Content: This dataset contains records of reported crimes in Los Angeles, including descriptions, locations, dates, and areas.
- Columns: Crime description, report date, victim's gender, location, area name, and a unique identifier.
- Initial Observations: Contains missing values in critical columns like crime description and area name.
- License Information: Open licensed CC0 1.0 Universal
     - Obligation: Any use of the crime data must include proper attribution to the Los Angeles Open Data Portal as the source.
     - Link: https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8/about_data

### Datasource2: Arrest Data
- Metadata URL: https://catalog.data.gov/dataset/arrest-data-from-2020-to-present
- URL: https://data.lacity.org/api/views/amvf-fr72/rows.csv?accessType=DOWNLOAD
- Content: This dataset includes records of arrests made in Los Angeles, providing details like arrest types, charges, locations, and dates.
- Columns: Crime description, report date, victim's gender, location, area name, and aunique identifier.
- Initial Observations: Contains missing values in critical columns like crime description andarea name.
- License Information: Open licensed CC0 1.0 Universal
     - Obligation: Similar to the crime data, proper attribution to the Los Angeles Open DataPortal is required.
     - Link: https://data.lacity.org/Public-Safety/Arrest-Data-from-2020-to-Present/amvf-fr72/about_data


## Work Packages

Here’s the breakdown of work packages for my project:

1. Research and Data collection
   - Collecting crime and arrest data from specified datasets covering relevant regions.

2. Data Preprocessing
   - Clean and standardize the data for consistency in analysis

3. Data Preliminary Inspection
   - Conduct exploratory analysis to identify initial patterns in crime reports and arrests.
4. Disparity Analysis:
   - Calculate and identify regions with the highest disparities between crime reports and arrests.

5. Statistical Analysis
   - Perform statistical tests to understand the relationship between crime reports and arrests.

6. Data Pipelining
   - Transform these datasets using ETL (Extract, Transform, Load) approaches in order to get a single dataset for evaluation.

7. Results Interpretation and Visualization
   - Create visualizations to illustrate disparities and key findings.
     
8. Policy Recommendations:
   - Develop recommendations to address the identified disparities.

9. Report Writing and Presentation
   - Transform the results into a straightforward report that includes graphs/ charts and recommendations.
   – Develop a presentation that is to be delivered to discuss overall results for the particular field of study and possible policies.

