# OOP-Related-Bugs-Study-TSE-Artifacts
This is the project repository of our TSE research paper: A Comprehensive Study of OOP-Related Bugs in C++ Compilers.
The project is composed of the following 3 folders that record our empirical study result, proof-of-concept application, and bug-finding experiment result respectively.

### Project Layout Overview
***
Here are the main useful files:
```
|-- OOP-Related-Bugs-Study
    |-- OOPFuzz/
        |-- setup/    ## The entrance for running the application
            |-- startup.sh    ## The start script
            |-- config.json    ## The configuration file for the code mutation process
        |-- src/    ## The code implementation of mutation operators
        |-- README.md  ## The instructions for building and running the application
    |-- bug triggering inputs/    
        |-- code/    ## The input test code triggering bugs reported via OOPFuzz
        |-- record.xlsx    ## The detailed information summary of input tests 
    |-- dataset
        |-- dataset_TSE.xlsx    ## The analysis result summary of selected bug reports
```

### About Bug Type Labeling
***
As shown in the paper, to conduct the bug-type taxonomy, we have manually analyzed 788 bug reports with 100 for pilot analysis and 688 for classification. More specifically, for the remaining 688 reports, the labeling process involves 6 rounds successively, each followed by a meeting between the first 2 authors to discuss the process and solve conflicts.  As a supplement to our paper, we are going to show a detailed statistics form for each of the 6 rounds of labeling below:

|**Round**|**Analyzed Reports**|**Conflicts**|**Phased Kappa**|
| ----------- | ----------- | ----------- | ----------- |
|1|48|5|0.879|
|2|45|5|0.875|
|3|92|7|0.913|
|4|97|5|0.951|
|5|182|11|0.932|
|6|224|15|0.938|
|Total|688|48| |





