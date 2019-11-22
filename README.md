# Antimicrobial
##Analysis_Script_API.py

Must have installed matplotlib and reqests libraries prior to running the script.
Version used during development were matplotlib (3.1.1) and reqests (2.22.0).

Purpose of script:
Access and analysise prescribing data from openprescribing.net

Functionality:
1. Enter name of CCG to investigate (type first few letters and select from drop-down list)
  program will look for population data for selected CCG using an API
2. Enter name of drug family to investigate (type first few letters and select from drop-down list)
  program will look for prescription data for selected drug family using an API
 
Practices with no population or no prescription data are filtered out and listed in the Zero_Population.txt or Zero_Prescription.txt files.
Population and prescription data with no missing values are merged on practices (practice IDs) 
