Open up terminal and navigate to the folder containing these scripts.

### Setting the Environment

This only needs to be done once.
To set up the environment, type the following command:
```
./setup.sh
```
Also, change the variable 'default_download_directory' in the script.py file. Set the variable to the path of the default download folder.

### Generating the Input File

To obtain the analysis for Structural MRI Pediatric Bipolar and Schizophrenia Lab Tutorial, create a .csv file, such that the first column consists of the path to the input file and the second column (optional) consists of the path to the output directory. If no second column is present, the data will be appended to the summary (output.csv), but the output files will not be saved. For example,
```csv
/Users/preksha/Desktop/anat_brain.nii.gz
/Users/preksha/Desktop/anat_brain_2.nii.gz,
/Users/preksha/Desktop/anat_brain_3.nii.gz,/Users/preksha/Desktop/output/anat_brain_3
```
A sample file is located in the folder (input.csv)

To generate a input.csv file by extracting all files with a particular extension from a directory, run the following command (change the value of the variables as required):
```bash
search_folder="/Users/prekshapatel/Desktop"   # please ensure this is the absolute path
extension="*.nii.gz"
find $search_folder -name $extension > input.csv
```

**NOTE**
- Any file which has less than one column or more than two columns will be ignored
- If the output directory does not exist, it will be created
- If a file named 'voidata.csv' or 'snapshot.png' is present in the output directory, it will be overwritten

### Running the Code

Once the .csv file is ready, run the script by the following command (replace input.csv by the path to the .csv folder created):
```
python3 script.py input.csv
```

**NOTE**
- To check the results, please examine the log.txt file that was created after running the program
- A summarized version of the results are saved in output.csv

### References
The scripts pertain to the course material taught in NS 101L at UCLA by Dr. Grisham
