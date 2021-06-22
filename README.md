Open up terminal and navigate to the folder containing these scripts.

### Setting the Environment

This only needs to be done once.
To set up the environment, type the following command:
```
./setup.sh
```
Also, change the variable 'default_download_directory' in the script.py file. Set the variable to the path of the default download folder.

### Running the Code

To obtain the analysis for Structural MRI Pediatric Bipolar and Schizophrenia Lab Tutorial, create a .csv file, such that the first column consists of the path to the input file and the second column consists of the path the the output directory. For example,
```
/Users/preksha/Desktop/anat_brain.nii.gz,/Users/preksha/Desktop/output/anat_brain
/Users/preksha/Desktop/anat_brain_2.nii.gz,/Users/preksha/Desktop/output/anat_brain_2
```

NOTE
- Any file which has less than or more than two columns will be ignored
- If the output directory does not exist, it will be created
- If a file named 'voidata.csv' or 'snapshot.png' is present in the output directory, it will be overwritten

Once the .csv file is ready, run the script by the following command (replace input.csv by the path to the .csv folder created):
```
python3 script.py input.csv
```

NOTE
- To check the results, please examine the log.txt file that was created after running the program

### References
The script pertain to the course material taught in NS 101L at UCLA by Dr. Grisham