import xlwt
import sys
import json
import argparse
from xlwt import Workbook
from usps import USPSApi


usps_instance = USPSApi('')  # API Key Here

packages = []


def returnPackage(tracking, desc):
    packageStatus = usps_instance.track(tracking).result.get(
        'TrackResponse').get('TrackInfo').get('TrackSummary')
    return {'tracking': tracking,
            'desc': desc,
            'time': packageStatus.get('EventTime'),
            'date': packageStatus.get('EventDate'),
            'state': packageStatus.get('EventState'),
            'city': packageStatus.get('EventCity'),
            'status': packageStatus.get('Event')
            }


def standardizeInput(string):
    if "-" in string:
        x = string.split("-")
        trackingNum = x[0].strip()
        desc = x[1].strip()
        return {'tracking': trackingNum,
                'desc': desc}
    else:
        return {'tracking': string,
                'desc': ""}


def addToSpread(package, row, sheet):
    sheet.write(row, 0, package.get('tracking'))
    sheet.write(row, 1, package.get('desc'))
    sheet.write(row, 2, package.get('time'))
    sheet.write(row, 3, package.get('date'))
    sheet.write(row, 4, package.get('city'))
    sheet.write(row, 5, package.get('state'))
    sheet.write(row, 6, package.get('status'))


def loadFile(path):
    with open(path, 'r') as f:
        for line in f:
            packages.append(returnPackage(standardizeInput(line).get(
                'tracking'), standardizeInput(line).get('desc')))

def main(argv):
    inputHelp = "Full path of the file containing tracking info and descriptions. File should be formatted as follows: Tracking # - Description"
    outputHelp = "Full path of where you would like to save your .xls sheet (be sure to include the .xls extention)."
    


    parser = argparse.ArgumentParser()
    parser.add_argument("--trackingFile", "-i", action='store', dest='inputFile', help=inputHelp,required=True)
    parser.add_argument("--outputFile", "-o", action='store', dest='outputFile', help=outputHelp,required=True)
    args = parser.parse_args()
    trackingFile = args.inputFile
    outputFile = args.outputFile

    loadFile(trackingFile)
    wb = Workbook()
    sheet1 = wb.add_sheet('sheet 1')
    for package in packages:
        addToSpread(package, packages.index(package), sheet1)
    wb.save(outputFile)


if __name__ == "__main__":
    main(sys.argv[1::])
