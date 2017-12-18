# credit https://chenyuzuoo.github.io/posts/b9c48783/


import csv
import pandas as pd 

# Read in raw data from csv
def main():
  rawData = pd.read_csv('brussel_test.csv')
  #rawData = csv.reader(open('brussel_test.csv', 'rb'), dialect='excel')
  print (rawData)
  # the template. where data from the csv will be formatted to geojson
  template = \
      ''' \
      { "type" : "Feature",
        "properties" :{},
          "geometry" : [%s},
          },
      '''
  # the head of the geojson file
  output = \
      ''' \
  { "type" : "FeatureCollection",
      "features" : [
      '''
  # loop through the csv by row skipping the first
  iter = 0
  for index, row in rawData.iterrows():
      # iter += 1
      # if iter >= 2:
      #drop_off_addr = '"{}"'.format(row[0])
      geo_json = row[1]
      #unixTime = row[1]
      #msgtext = row[3]
      #userID = row[4]
      # output += template % (row[0], row[2], row[1], row[3], row[4])
      output += template % (geo_json)
      
  # the tail of the geojson file
  output += \
      ''' \
      ]
  }
      '''
      
  # opens an geoJSON file to write the output to
  outFileHandle = open("brussel_test.geo.json", "w")
  outFileHandle.write(output)
  outFileHandle.close()


if __name__ == '__main__':
  main()




