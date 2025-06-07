# Chicago Crime Pattern Analytics with MapReduce  
## University of Ruhuna - Faculty of Engineering 
### Module Name: Cloud Computing (EC7205)  
### Assignment 1
### Group Number: 55

---

## Team Members
- EG/2020/3943 - Sundarasekara G.O.
- EG/2020/3978 - Jayakody J.A.T.K.
- EG/2020/4181 - Samaraweera S.A.D.C.K.
---

## Table of Contents

1. [Dataset](#1-dataset)
2. [MapReduce Job Implementation and Approach](#2-mapreduce-job-implementation-and-approach)
3. [Environment Setup](#3-environment-setup)
4. [Test and Run on Real Data](#4-test-and-run-on-real-data)
5. [Interpret the Result](#5-interpret-the-result)
6. [Source Code](#6-source-code)
---

## 1. Dataset

This project uses the [chicago crimes 2023-2024](https://www.kaggle.com/datasets/carolinaaaaaaa/chicago-crimes-90-days-2024) dataset from Kaggle, containing one year's worth of police reports, covering the period from **2023-05-05 to 2024-05-03**. The data contains detailed records of reported crimes in the city of Chicago over this time frame.

- **Time Period:** One year, from 2023-05-05 to 2024-05-03.
- **Rows:** 258535 records.
- **Format:** CSV file with columns:

  - `CASE#`: Unique identifier for the crime report
  - `DATE OF OCCURRENCE`: Date and time when the incident took place
  - `BLOCK`: Approximate address where the crime occurred
  - `IUCR`: Illinois Uniform Crime Reporting code (crime classification)
  - `PRIMARY DESCRIPTION`: Main category/type of the crime (e.g., THEFT, BATTERY)
  - `SECONDARY DESCRIPTION`: More specific sub-type of the crime
  - `LOCATION DESCRIPTION`: Type of location (e.g., STREET, APARTMENT)
  - `ARREST`: Indicates if an arrest was made (Y/N)
  - `DOMESTIC`: Indicates if the incident was domestic-related (Y/N)
  - `BEAT`: Police beat where the crime occurred
  - `WARD`: City council ward of the incident location
  - `FBI CD`: FBI crime classification code
  - `X COORDINATE`: X coordinate (projected map position, for mapping)
  - `Y COORDINATE`: Y coordinate (projected map position, for mapping)
  - `LATITUDE`: Latitude in decimal degrees
  - `LONGITUDE`: Longitude in decimal degrees
  - `LOCATION`: Combined latitude and longitude (tuple)
- **Reason for choice:** The dataset is sufficiently large, real-world, and complex, enabling meaningful crime analytics at scale.

#### Example row

---

| CASE#    | DATE OF OCCURRENCE | BLOCK               | IUCR | PRIMARY DESCRIPTION | SECONDARY DESCRIPTION | LOCATION DESCRIPTION | ARREST |
|----------|--------------------|---------------------|------|--------------------|----------------------|---------------------|--------|
| JG497095 | 11/8/2023 20:50    | 025XX N KEDZIE BLVD | 810  | THEFT              | OVER $500            | STREET              | N      |

---

| DOMESTIC | BEAT | WARD | FBI CD | X COORDINATE | Y COORDINATE | LATITUDE     | LONGITUDE     | LOCATION                    |
|----------|------|------|--------|--------------|--------------|--------------|---------------|-----------------------------|
| N        | 1414 | 35   | 6      | 1154609      | 1916759      | 41.92740733  | -87.70729439  | (41.927407329, -87.70729439) |

</br>

---

## 2. MapReduce Job Implementation and Approach

**Task Chosen:**  
Analyze and summarize Chicago crime patterns by:
- Counting the number of crimes per combination of crime category and location.
- Identifying the most common locations for each crime type.

**Dataset Preparation:**
- The original dataset was sourced from Kaggle and cleaned to retain only the relevant columns and mainly, two columns were used. 
  - PRIMARY DESCRIPTION (Crime type)
  - LOCATION DESCRIPTION (Location where the crime occurred)

- Then, the cleaned data was uploaded into HDFS (Hadoop Distributed File System) for distributed processing.

**Execution Environment:**
- The analysis was conducted on a pseudo-distributed Hadoop cluster, which simulates a multi-node environment on a single physical machine.

**MapReduce Workflow:**

- **Map Phase (`src/mapper.py`):**  
  Reads CSV rows, extracts the primary crime description and location, and emits key-value pairs of the form:  
  `<crime_type> <TAB> <location> <TAB> 1`

- **Shuffle and Sort Phase:**  
  The Hadoop framework internally grouped all values by the composite key (CrimeType:Location) and sorted them before sending them to the reducers for aggregation.

- **Reduce Phase (`src/reducer.py`):**  
  Aggregates counts for each unique (crime_type, location) pair and outputs the total number of reports for each.

- **Result Interpretation (`src/interpret_results.py`):**  
  Reads the reducer's output and:
    - Computes and prints the total number of crimes per crime type.
    - For each crime type, identifies the top 3 locations where that crime most frequently occurs.

**Example Output:**  
- List of crime types sorted by total reports.
- For each crime type, a list of the three most common locations and the number of reports at each.

This approach provides insights into which types of crimes are most frequent overall and where they are most likely to occur within Chicago.

**Programming Language:** Python (for both mapper and reducer scripts).

<div style="page-break-after: always;"></div>

---

## 3. Environment Setup

- **Platform:** Hadoop 3.4.1 (pseudo-distributed setup)
- **Java Version:** JDK 11
- **Python Version:** Python 3.x (used for mapper, reducer, and result interpretation scripts)
- **HDFS:** Configured for input/output storage.
- **Scripts:** Bash scripts automate upload, execution, and result interpretation. 

- **Evidence of installation:**  
  <br/>
  <b>Java Installation</b><br/>
  <img src="screenshots/java_installation.png" alt="Java Installation" width="800"/>
  <br/>

  <b>Hadoop Installation</b><br/>
  <img src="screenshots/hadoop_installation.png" alt="Hadoop Installation" width="800"/>
  <br/>

  <b>Environment Variables Configuration</b><br/>
  <img src="screenshots/environment_variables.png" alt="Environment Variables" width="800"/>
  <br/>

  <b>Hadoop Configuration</b><br/>
    
    The Hadoop configuration files used for this project are available in the [hadoop-config](https://github.com/chanmini-kavinya/chicago-crime-mapreduce/tree/master/hadoop-config) 
    directory of the GitHub repository:
    
  - [core-site.xml](https://github.com/chanmini-kavinya/chicago-crime-mapreduce/blob/master/hadoop-config/core-site.xml)
  - [hdfs-site.xml](https://github.com/chanmini-kavinya/chicago-crime-mapreduce/blob/master/hadoop-config/hdfs-site.xml)
  - [mapred-site.xml](https://github.com/chanmini-kavinya/chicago-crime-mapreduce/blob/master/hadoop-config/mapred-site.xml)
  - [yarn-site.xml](https://github.com/chanmini-kavinya/chicago-crime-mapreduce/blob/master/hadoop-config/yarn-site.xml) 

  <br/>

  <div style="page-break-after: always;"></div>

  <b>SSH Configuration</b><br/>
  <img src="screenshots/ssh_configuration1.png" alt="SSH Configuration" width="800"/>
  <img src="screenshots/ssh_configuration2.png" alt="SSH Configuration" width="800"/>
  <img src="screenshots/ssh_configuration3.png" alt="SSH Configuration" width="800"/>
  <br/>

  <b>Start Hadoop Services</b><br/>
  <img src="screenshots/start_hadoop_services.png" alt="Start Hadoop Services" width="800"/>

<div style="page-break-after: always;"></div>

---

## 4. Test and Run on Real Data

The MapReduce job was executed on the full Kaggle dataset (approximately one year of Chicago police reports).

- **Input:**  
  Full Kaggle Chicago crime dataset ([Kaggle Dataset Link](https://www.kaggle.com/datasets/carolinaaaaaaa/chicago-crimes-90-days-2024)).

- **Sample MapReduce Output ([output.txt](https://github.com/chanmini-kavinya/chicago-crime-mapreduce/blob/master/output/output.txt)):**
  ```
  ARSON	ABANDONED BUILDING	6
  ARSON	AIRPORT BUILDING NON-TERMINAL - NON-SECURE AREA	1
  ARSON	ALLEY	54
  ARSON	APARTMENT	78
  ARSON	BAR OR TAVERN	2
  ARSON	CHA APARTMENT	2
  ARSON	CHA HALLWAY / STAIRWELL / ELEVATOR	1
  ARSON	CHA PARKING LOT / GROUNDS	1
  ARSON	CHURCH / SYNAGOGUE / PLACE OF WORSHIP	1
  ARSON	COMMERCIAL / BUSINESS OFFICE	4
  ...
  ```

- **Sample Interpretation ([summary.txt](https://github.com/chanmini-kavinya/chicago-crime-mapreduce/blob/master/output/summary.txt)):**
  ```
  ==================================================
  Total Crime Types (Sorted by Count)
  ==================================================
  THEFT                               57531 crimes
  BATTERY                             44881 crimes
  CRIMINAL DAMAGE                     29816 crimes
  MOTOR VEHICLE THEFT                 26560 crimes
  ASSAULT                             22992 crimes
  ...

  ==================================================
  Top 3 Locations per Crime Type
  ===================================================

  🔹 THEFT (Top 3 Locations):
     1. STREET                    15215 reports
     2. APARTMENT                  7303 reports
     3. SMALL RETAIL STORE         4968 reports

  🔹 BATTERY (Top 3 Locations):
     1. APARTMENT                 14779 reports
     2. RESIDENCE                  6883 reports
     3. STREET                     6575 reports

  🔹 CRIMINAL DAMAGE (Top 3 Locations):
     1. STREET                    12079 reports
     2. APARTMENT                  5304 reports
     3. RESIDENCE                  3642 reports
  ```

<div style="page-break-after: always;"></div>

You can refer to the following files for the complete output and interpretation:
- [Raw MapReduce Output (output.txt)](https://github.com/chanmini-kavinya/chicago-crime-mapreduce/blob/master/output/output.txt)
- [Interpretation & Summary (summary.txt)](https://github.com/chanmini-kavinya/chicago-crime-mapreduce/blob/master/output/summary.txt)
---

## 5. Interpret the Result

### Result Summary

The dataset included 258535 crime records. Initially, the total number of incidents for each crime type and location combination is found. Then , the most frequent types of crimes reported in Chicago, as well as the top locations where each crime most often occurred were identified. Theft was the most common crime type, followed by Battery and Criminal Damage. For each crime category, the top three locations were extracted and ranked by report count.
The output reveals that Streets, Apartments, and Residences are the most common crime scenes across a wide range of offenses. For example, Theft incidents mostly happened on streets and in apartments, while Battery was frequently reported in apartments and residences.

### Crime Type Proportion

<img src="output/crime_type_proportion.png" width="500">

This pie chart illustrates the overall distribution of crime types within the dataset. Theft is the most prevalent crime, accounting for 22.4% of total reports, followed by Battery (17.4%), Criminal Damage (11.6%), and Motor Vehicle Theft (10.3%). These top four categories alone represent over 60% of all reported incidents. The chart also includes less frequent crime types, such as Narcotics, Weapons Violations, and Burglary, each contributing a smaller proportion. This visualization provides a clear overview of crime trends and reported offenses in the city of Chicago during 2023–2024.

### Top 3 Locations per Crime Type

<img src="output/summary_top3_locations_per_crime_type.png" width="800">

This bar chart presents the top three most common locations where each crime type occurs. It shows key location-based trends in criminal activity. For example, Theft and Criminal Damage most often happen on Streets and in Apartments, while Motor Vehicle Theft is frequently reported at Streets and Parking Garages. Crimes like Assault and Deceptive Practices also show high occurrences in Residences, Apartments and Streets. Each group of bars corresponds to a specific crime type, with stacked colors representing the top three locations.

### Patterns and Insights
- Several interesting patterns emerged from the analysis of the Chicago crime dataset
- Theft was the most reported crime, with over 57,000 instances, followed by Battery and Criminal Damage, where these three types made up a significant portion of total crime reports.
- Street, Apartment, and Residence emerge as the most common settings for the majority of crimes. This pattern suggests a strong correlation between densely populated or publicly accessible areas and crime frequency.
- Motor Vehicle Theft incidents predominantly occur on Streets and in Parking Lots, indicating the need for better surveillance in outdoor public areas.
- Less frequent but serious crimes such as Homicide and Criminal Sexual Assault also occurred commonly in Apartments and Streets,  raising concerns about safety in both private and public environments.

### Performance or Accuracy Observations

- The MapReduce was successfully executed on a single-node Hadoop system.
- While this setup was sufficient for processing the dataset, the performance can be improved more by using a multi-node Hadoop cluster for parallelism.
- The term “accuracy” is not applicable for this dataset since we are not dealing with a predictive or classification model.
- The output is the result of deterministic aggregation, i.e., counting crime types and their top locations. However, data quality issues can still affect result reliability:
  - Some location names are inconsistently labeled (e.g., "RESIDENCE" vs "APARTMENT").
  - Certain location fields may be missing, potentially skewing the "top 3 locations" per crime type.
  - These inconsistencies don't introduce inaccuracy in the code execution but reduce the interpretability and trustworthiness of raw insights.

### Suggestions for Expansion

- Multi-node Deployment by running the job on a full Hadoop cluster to handle larger datasets and improve processing speed.
- Future analysis can use temporal data (e.g., by year or season) to detect trends in crime frequency over time.
- Geospatial Insights: Integrate latitude and longitude data to map hotspots visually.
- Normalize similar location labels for better grouping (e.g., unify "RESIDENCE", "APARTMENT", "HOUSE").
- Machine learning techniques like clustering or classification algorithms can be used to find the hidden relationships within data.


---

## 6. Source Code

The full source code is available at:  
[https://github.com/chanmini-kavinya/chicago-crime-mapreduce](https://github.com/chanmini-kavinya/chicago-crime-mapreduce)
