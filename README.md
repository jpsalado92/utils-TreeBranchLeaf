# TreeBranchLeaf
Given files containing indicators and headers at different levels, create a new `.csv` file in which every indicator is
groupped with its corresponding header(s). 

## Example
### Input
`ind_headers123.txt` file:
```text
header1
header1.1
header1.1.1
indicator1
header2
indicator2
header3
header3.1
indicator3
```
`headers-lvl1.txt` file:
```text
header1
header2
header3
```
`headers-lvl2.txt` file:
```text
header1.1
header3.1
```
`headers-lvl3.txt` file:
```text
header1.1.1
```
 
### Output
`result.txt`
```text
indicator, header_1, header_2, header_3
indicator1, header1, header1.1, header1.1.1 
indicator2, header2, -, -   
indicator3, header3, header3.1, -
```

## Data
All the data in this repo was obtained by manual extraction from [Garapen website](http://www.garapen.net/public_observatorio/ctrl_observatorio.php?lang=es)