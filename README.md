### CMIP5 P50 Analysis


Request spatial data for range areas from IUCN Red List of Threatened Species:  
[http://www.iucnredlist.org](http://www.iucnredlist.org)

**Transform IUCN spatial data from shape file to a mask:**  

Install the GDAL Geospatial Data Abstraction Library:   
[https://trac.osgeo.org/gdal/wiki/BuildHints](https://trac.osgeo.org/gdal/wiki/BuildHints)

Type in bash shell:  

    ogr2ogr -f "GMT" -dim 3 species.gmt species.shp

Install GMT5:    
[http://gmt.soest.hawaii.edu/projects/gmt/wiki/Download](http://gmt.soest.hawaii.edu/projects/gmt/wiki/Download)

Type in GMT5 bash shell (grid the same as World Ocean Atlas 1° grid):  

    gmt grdmask -R-179.5/179.5/-89.5/89.5 -I1 -f0x -f1y -NNaN/1/1 species.gmt -Gspecies.nc  