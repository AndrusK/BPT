# Bulk Postage Tracker
Due to USPS's package tracking notifications being as seemingly random as they are, this project was made to avoid the 3am text notifications of the USPS telling me a package has once again been delayed due to their incompetence. I'm now able to avoid the sleepless nights of disappointment from the USPS by running this and having all my package updates in a convenient spreadsheet.

## Installation

This script has a couple dependencies. The first of which is an API key for the USPS API. Which you can register for [here](https://www.usps.com/business/web-tools-apis/).


You will also need the following python packages:

```text
argparse
json
sys
usps-api
xlwt
```
## Usage
Usage is pretty straight forward.
```text
bpt.py -i <file containing tracking numbers> -o <your output file (be sure to add the .xls extention)>
```
You input text file should be formatted like this:
```text
# - Package Description
# - Package Description
```

## License
[WTFPL](http://www.wtfpl.net/)
