# Chicago Crime Pattern Analytics with MapReduce  
## University of Ruhuna - Faculty of Engineering 
### Module Name: Cloud Computing (EC7205)  
### Assignment Title: Large-Scale Data Analysis Using MapReduce

---

### Team Members
- EG/2020/3943
- EG/2020/3978
- EG/2020/4181 Samaraweera S.A.D.C.K.
---

## 1. Chosen Dataset

This project uses the [Chicago Crimes - 90 Days (2024)](https://www.kaggle.com/datasets/carolinaaaaaaa/chicago-crimes-90-days-2024) dataset from Kaggle, which has been expanded to include one year's worth of police reports, covering the period from **2023-05-05 to 2024-05-03**. The data contains detailed records of reported crimes in the city of Chicago over this time frame.

- **Time Period:** One year, from 2023-05-05 to 2024-05-03.
- **Rows:** 258535 records.
- **Format:** CSV file with columns:

  - `CASE#`
  - `DATE  OF OCCURRENCE`
  - `BLOCK`
  - `IUCR`
  - `PRIMARY DESCRIPTION`
  - `SECONDARY DESCRIPTION`
  - `LOCATION DESCRIPTION`
  - `ARREST`
  - `DOMESTIC`
  - `BEAT`
  - `WARD`
  - `FBI CD`
  - `X COORDINATE`
  - `Y COORDINATE`
  - `LATITUDE`
  - `LONGITUDE`
  - `LOCATION`
- **Reason for choice:** The dataset is sufficiently large, real-world, and complex, enabling meaningful crime analytics at scale.

#### Example row

| CASE#    | DATE  OF OCCURRENCE | BLOCK             | IUCR | PRIMARY DESCRIPTION | SECONDARY DESCRIPTION | LOCATION DESCRIPTION | ARREST | DOMESTIC | BEAT | WARD | FBI CD | X COORDINATE | Y COORDINATE | LATITUDE     | LONGITUDE     | LOCATION              |
|----------|---------------------|-------------------|------|--------------------|----------------------|---------------------|--------|----------|------|------|--------|--------------|--------------|--------------|---------------|-----------------------|
| JG497095 | 11/8/2023 20:50     | 025XX N KEDZIE BLVD| 810  | THEFT              | OVER $500            | STREET              | N      | N        | 1414 | 35   | 6      | 1154609      | 1916759      | 41.92740733  | -87.70729439 | (41.927407329, -87.70729439) |


---

## 2. Implemented MapReduce Job

**Task Chosen:**  
Analyze and summarize Chicago crime patterns by:
- Counting the number of crimes per combination of "Primary Description" (crime category) and location.
- Identifying the most common locations for each crime type.

**MapReduce Approach:**

- **Mapper (`src/mapper.py`):**  
  Reads CSV rows, extracts the primary crime description and location, and emits key-value pairs of the form:  
  `<crime_type> <TAB> <location> <TAB> 1`

- **Reducer (`src/reducer.py`):**  
  Receives sorted key-value pairs, aggregates the counts for each (crime_type, location) pair, and outputs the total count for each unique combination.

- **Interpretation Script (`src/interpret_results.py`):**  
  Reads the reducer's output and:
    - Computes and prints the total number of crimes per crime type (sorted by count).
    - For each crime type, identifies the top 3 locations where that crime most frequently occurs.

**Example Output:**  
- List of crime types sorted by total reports.
- For each crime type, a list of the three most common locations and the number of reports at each.

This approach provides insights into which types of crimes are most frequent overall and where they are most likely to occur within Chicago.

**Programming Language:** Python (for both mapper and reducer scripts).

---

## 3. Environment Setup

- **Platform:** Hadoop 3.4.1 (local single-node setup)
- **Java Version:** JDK 11
- **HDFS:** Configured for input/output storage.
- **Scripts:** Bash scripts automate upload, execution, and result fetching.
- **Evidence of installation:**  
  ![Hadoop Installation Screenshot](screenshot_hadoop_installation.png)  

---

## 4. Test and Run on Real Data

- **Input:** Full Kaggle dataset (~1 year of Chicago police reports)
- **Execution:**  
  ```bash
  bash scripts/upload_to_hdfs.sh
  bash scripts/run_mapreduce.sh
  bash scripts/fetch_and_interpret_results.sh
  ```
- **Sample Output (from output/output.txt):**
  ```
  THEFT    14235
  BATTERY   9911
  CRIMINAL DAMAGE  6721
  ASSAULT  3542
  ...
  ```
- **Execution Log:**  
  See `output/execution_log.txt` or attached screenshot(s).

---

## 5. Result Interpretation


---

## 6. Documentation and Submission

- **README.md:** Provided with clear setup and execution steps.
- **Source Code:** See `src/` and `scripts/` directories.
- **Dataset:** Kaggle dataset referenced; not redistributed due to licensing.
- **Results & Logs:** Included in `output/` directory.
- **Evidence:** Screenshots of Hadoop installation and job execution included.
