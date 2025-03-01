# OOP-Related-Bugs-Study-TSE-Artifacts
This is the project repository of our TSE research paper: A Comprehensive Study of OOP-Related Bugs in C++ Compilers.
The project is composed of the following 3 folders that record our empirical study result, proof-of-concept application, and bug-finding experiment result respectively.

### Project Layout Overview
***
Here are the main useful files:
```
|-- OOP-Related-Bugs-Study
    |-- dataset
        |-- dataset_TSE.xlsx    ## The analysis result summary of selected bug reports
    |-- scripts/
        |-- filter_by_keywords/    ## The corresponding scripts to  perform keyword filtering
        |-- extract_statistics/    ## The corresponding scripts to reproduce all the statistics in the paper
        |-- show_figures/  ## The corresponding scripts to draw the figures
    |-- OOPFuzz/
        |-- setup/    ## The entrance for running the application
            |-- startup.sh    ## The start script
            |-- config.json    ## The configuration file for the code mutation process
        |-- src/    ## The code implementation of mutation operators
        |-- README.md  ## The instructions for building and running the application
    |-- bug triggering inputs/    
        |-- code/    ## The input test code triggering bugs reported via OOPFuzz
        |-- record.xlsx    ## The detailed information summary of input tests 
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

### Bug Number Distribution by Year
***

The following table is the supplement to Table 1 that shows the bug distribution in each year:

|**Year**|**2014**|**2015**|**2016**|**2017**|**2018**|**2019**|**2020**|**2021**|**2022**|**2013**|
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
|**Reports_GCC**||||509|675|511|580|548|358|220|
|**Remain_GCC**||||201|254|185|225|196|129|78|
|**Bugs_GCC**||||64|118|102|93|91|45|73|
|**Reports_LLVM**|219|154|154|132|80|68|111|58|13|16|
|**Remain_LLVM**|78|51|55|49|25|24|39|16|5|11|
|**Bugs_LLVM**|49|29|31|19|15|25|14|9|4|7|








