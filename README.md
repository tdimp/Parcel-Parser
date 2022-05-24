### INTRODUCTION
This program utilizes publicly available data and is meant to aid in the comparison of city parcels' zoning and future land use designations 
to find parcels whose current zoning does not roughly align with the future land use designation envisioned in the Comprehensive Plan. This 
will help the planning department focus their efforts on the parcels in need of a change in future land use designation. 


### GOALS
The primary goal is to compare each parcel's zoning with its future land use designation to find mismatches.
Because PDs are essentially customized, site-specific districts, it is necessary to separate them from the main parcel list.

The secondary goal is to create a list of unique PDs which will enable more efficient analysis. PD names generally coincide
with their subdivision names, so this program generates a list of unique subdivision names for all parcels zoned PD.


### HOW TO USE
You must have Python 3 installed (specifically 3.8.10). This program can be used by running 'python3 main.py' in the terminal.
All of the helper modules are imported to main.py and run within it. Because this program was written for a very specific task,
it requires 'parcels.csv' to be present and organized with certain header names and cell values.


### EXPECTED RESULTS
The program and its helper modules will output the following CSV files:
 
  1. A CSV list of all parcels zoned PD
  2. A CSV list of unique subdivision names derived from the PD parcel list
  3. A CSV list of all parcels (minus those zoned PD) currently in the city limits
  4. A CSV list of all parcels within the city (minus those zoned PD) whose zoning does not roughly correspond to its future land use designation.

### LICENSE

Copyright 2022 TDIMP

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.