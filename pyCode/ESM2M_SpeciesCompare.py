#ipython --pylab
import scipy
from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

Folder = '/Users/kasmith/Dropbox/Manuscripts/CMIP5_p50/Results/ESM2M/deltap50depth/'
species1 = ['Todarodes_sagittatus', 'Thunnus_thynnus', 'Thunnus_obesus', 'Thunnus_maccoyii', 'Thunnus_albacares', 'Systellaspis_debilis', 'Scomber_japonicus', 'Pagothenia_borchgrevinki']
species2 = ['Oplophorus_gracilirostris', 'Nautilus_pompilius', 'Meganyctiphanes_norvegica', 'Loligo_vulgaris', 'Katsuwonus_pelamis', 'Gnathphausia_ingens', 'Euphausia_superba', 'Dosidicus_gigas']
species3 = ['Doryteuthis_pealeii', 'Dissostichus_mawsoni', 'Clupea_harengus', 'Architeuthis_dux', 'Acipenser_medirostris', 'Acanthephyra_smithi', 'Acanthephyra_curtirostris', 'Acanthephyra_acutifrons']


leftlist = [0.02, 0.216, 0.412, 0.608, 0.804]
#bottomlist = [0.755, 0.51, 0.265, 0.02]
#bottomlist = [0.7525, 0.505, 0.2575, 0.01]
bottomlist = [0.76, 0.52, 0.27, 0.02]

width = 0.42
#height = 0.225
#height = 0.2575
height = 0.20

g = [[0.06, bottomlist[0], width, height], [0.56, bottomlist[0], width, height],
     [0.06, bottomlist[1], width, height], [0.56, bottomlist[1], width, height],
[0.06, bottomlist[2], width, height], [0.56, bottomlist[2], width, height],
[0.06, bottomlist[3], width, height], [0.56, bottomlist[3], width, height]]

i = 0
while i<len(species1):
  file = Folder + 'ESM2M.rcp85.deltap50depth.' + species1[i] + '.nc'
  nc = Dataset(file,'r')
  lats = nc.variables['YT_OCEAN'][:]
  lons = nc.variables['XT_OCEAN'][:]
  lons2 = lons+360
  depth = nc.variables['DELTA_P50DEPTH'][:]
  depth = depth.squeeze()
  fig = plt.figure(1, figsize(8,10))
  axg1 = plt.axes(g[i])
  m = Basemap(llcrnrlon=20.,llcrnrlat=-80.,urcrnrlon=380.,urcrnrlat=80.,projection='cyl',lon_0=180)
  x, y = m(*np.meshgrid(lons, lats))
  a, b = m(*np.meshgrid(lons2, lats))
  m.drawmapboundary(fill_color='0.7') #fill_color='0.5'
  m.drawcoastlines()
  m.fillcontinents(color='black', lake_color='0.5')
  if (i == 0) or (i == 2) or (i == 4) or (i == 6):
    m.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0])
  else:
    m.drawparallels(np.arange(-90.,120.,30.),labels=[0,0,0,0])
  m.drawmeridians(np.arange(0.,420.,60.),labels=[0,0,0,0])
  im1 = m.pcolor(x,y,depth,cmap=plt.cm.BrBG, vmin=-200, vmax=200)
  im2 = m.pcolor(a,b,depth,cmap=plt.cm.BrBG, vmin=-200, vmax=200)
  cb = m.colorbar(im1,"bottom", size="5%", pad="2%")
  cb.set_ticks([-200,-100,0,100,200])
  cb.set_ticklabels([-200,-100,0,100,200])
  plt.title(species1[i], fontsize=12)
  plt.suptitle("ESM2M P50 Depth Change")
  i=i+1

plt.show()

outfig = '/Users/kasmith/Dropbox/Manuscripts/CMIP5_p50/Graphs/ESM2M_species1.ps'
plt.savefig(outfig, dpi=72, bbox_inches=0)


i = 0
while i<len(species2):
  file = Folder + 'ESM2M.rcp85.deltap50depth.' + species2[i] + '.nc'
  nc = Dataset(file,'r')
  lats = nc.variables['YT_OCEAN'][:]
  lons = nc.variables['XT_OCEAN'][:]
  lons2 = lons+360
  depth = nc.variables['DELTA_P50DEPTH'][:]
  depth = depth.squeeze()
  fig = plt.figure(2, figsize(8,10))
  axg1 = plt.axes(g[i])
  m = Basemap(llcrnrlon=20.,llcrnrlat=-80.,urcrnrlon=390.,urcrnrlat=80.,projection='cyl',lon_0=180)
  x, y = m(*np.meshgrid(lons, lats))
  a, b = m(*np.meshgrid(lons2, lats))
  m.drawmapboundary(fill_color='0.7') #fill_color='0.5'
  m.drawcoastlines()
  m.fillcontinents(color='black', lake_color='0.5')
  if (i == 0) or (i == 2) or (i == 4) or (i == 6):
    m.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0])
  else:
    m.drawparallels(np.arange(-90.,120.,30.),labels=[0,0,0,0])
  m.drawmeridians(np.arange(0.,420.,60.),labels=[0,0,0,0])
  im1 = m.pcolor(x,y,depth,cmap=plt.cm.BrBG, vmin=-200, vmax=200)
  im2 = m.pcolor(a,b,depth,cmap=plt.cm.BrBG, vmin=-200, vmax=200)
  cb = m.colorbar(im1,"bottom", size="5%", pad="2%")
  cb.set_ticks([-200,-100,0,100,200])
  cb.set_ticklabels([-200,-100,0,100,200])
  plt.title(species2[i], fontsize=12)
  plt.suptitle("ESM2M P50 Depth Change")
  i=i+1

plt.show()

outfig = '/Users/kasmith/Dropbox/Manuscripts/CMIP5_p50/Graphs/ESM2M_species2.ps'
plt.savefig(outfig, dpi=72, bbox_inches=0)


i = 0
while i<len(species3):
  file = Folder + 'ESM2M.rcp85.deltap50depth.' + species3[i] + '.nc'
  nc = Dataset(file,'r')
  lats = nc.variables['YT_OCEAN'][:]
  lons = nc.variables['XT_OCEAN'][:]
  lons2 = lons+360
  depth = nc.variables['DELTA_P50DEPTH'][:]
  depth = depth.squeeze()
  fig = plt.figure(3, figsize(8,10))
  axg1 = plt.axes(g[i])
  m = Basemap(llcrnrlon=20.,llcrnrlat=-80.,urcrnrlon=390.,urcrnrlat=80.,projection='cyl',lon_0=180)
  x, y = m(*np.meshgrid(lons, lats))
  a, b = m(*np.meshgrid(lons2, lats))
  m.drawmapboundary(fill_color='0.7') #fill_color='0.5'
  m.drawcoastlines()
  m.fillcontinents(color='black', lake_color='0.5')
  if (i == 0) or (i == 2) or (i == 4) or (i == 6):
    m.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0])
  else:
    m.drawparallels(np.arange(-90.,120.,30.),labels=[0,0,0,0])
  m.drawmeridians(np.arange(0.,420.,60.),labels=[0,0,0,0])
  im1 = m.pcolor(x,y,depth,cmap=plt.cm.BrBG, vmin=-200, vmax=200)
  im2 = m.pcolor(a,b,depth,cmap=plt.cm.BrBG, vmin=-200, vmax=200)
  cb = m.colorbar(im1,"bottom", size="5%", pad="2%")
  cb.set_ticks([-200,-100,0,100,200])
  cb.set_ticklabels([-200,-100,0,100,200])
  plt.title(species3[i], fontsize=12)
  plt.suptitle("ESM2M P50 Depth Change")
  i=i+1

plt.show()

outfig = '/Users/kasmith/Dropbox/Manuscripts/CMIP5_p50/Graphs/ESM2M_species3.ps'
plt.savefig(outfig, dpi=72, bbox_inches=0)



