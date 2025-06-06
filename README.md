# Chicago Crime Pattern Analytics with MapReduce

This repository implements a scalable data processing pipeline to analyze crime patterns in Chicago using Hadoop MapReduce with Python. It uses big data technologies to efficiently process large volumes of crime data, extract meaningful insights, and automate the workflow from data ingestion to result interpretation.

## About the Dataset

This project uses the [Chicago Crimes - 90 Days (2024)](https://www.kaggle.com/datasets/carolinaaaaaaa/chicago-crimes-90-days-2024) dataset from Kaggle, containing one year's worth of police reports, covering the period from **2023-05-05 to 2024-05-03**. The data contains detailed records of reported crimes in the city of Chicago over this time frame.

## Directory Structure

- `src/`: Python source code for the mapper, reducer, and result interpretation.
  - `mapper.py`: Mapper script for Hadoop streaming.
  - `reducer.py`: Reducer script for Hadoop streaming.
  - `interpret_results.py`: Post-processing/ result interpretation script.
- `scripts/`: Bash scripts to automate HDFS upload, running MapReduce jobs, interpreting results, and viewing output.
- `input/`: Contains the input CSV data file(s).
- `output/`: Output directory for processed results.

## Prerequisites

- Java JDK 11 or higher
- Hadoop 3.4.1 installed and configured (with HDFS setup)
- Python 3.x

**Note:** Ensure that all `scripts/*.sh` files have execute permissions.  
You can grant permission with:

```bash
chmod +x scripts/*.sh
```

## Steps to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/chanmini-kavinya/chicago-crime-mapreduce.git
   cd chicago-crime-mapreduce
   ```

2. **Upload data to HDFS**
   - Use the provided script to upload your input data to HDFS:
     ```bash
     bash scripts/upload_to_hdfs.sh
     ```

3. **Run the MapReduce Job**
   - Execute the MapReduce job using:
     ```bash
     bash scripts/run_mapreduce.sh
     ```
   - This will use `src/mapper.py` and `src/reducer.py` for the Hadoop streaming job.

4. **View MapReduce Output on HDFS (Optional)**
   - To quickly view the MapReduce output stored on HDFS:
     ```bash
     bash scripts/view_hdfs_output.sh
     ```

5. **Interpret Results from HDFS**
   - After the job completes, fetch the output to your local `output/` directory and interpret the results:
     ```bash
     bash scripts/interpret_results.sh
     ```
