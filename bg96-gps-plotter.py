
# import gmplot package 
import gmplot 
import sys  

#######################
#settings
marker_size = 5

def latitude_converter(lat_string):

  	latitude = float(lat_string[:2])
	latitude += (float(lat_string[2:9])/60)

  	if lat_string[9] == 'S':
  		latitude = latitude * (-1)
  	
  	return latitude
    
def longitude_converter(lon_string):

  	longitude = float(lon_string[:3])
  	longitude += (float(lon_string[3:10])/60)

  	if lon_string[10] == 'W':
  		longitude = longitude * (-1)

  	return longitude


lat_list = list()
lon_list = list()

for line in sys.stdin:
    coord = line.split(',')
    if len(coord) == 11:
    	lat_list.append(latitude_converter(str(coord[1])))
    	lon_list.append(longitude_converter(str(coord[2])))
   



#print "{} {}".format(lat_list[0], lon_list[0]) 

# GoogleMapPlotter return Map object 
# Pass the center latitude and 
# center longitude 
gmap = gmplot.GoogleMapPlotter(lat_list[0], lon_list[0], 13 ) 
gmap.scatter( lat_list, lon_list, '# FF0000', 
                              size = marker_size, marker = False ) 
# Pass the absolute path 
gmap.draw( "map11.html" ) 
