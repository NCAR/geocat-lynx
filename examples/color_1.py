import xarray as xr
import numpy as np
import cartopy.crs as ccrs
import netCDF4 as nc

import geocat.datafiles as gdf
from geocat.viz import cmaps as gvcmaps
import lynx

# Open a netCDF data file using xarray default engine and load the data into xarray
ds = xr.open_dataset(gdf.get("netcdf_files/uv300.nc")).isel(time=1)
# fn = gdf.get("netcdf_files/uv300.nc")
# ds = nc.Dataset(fn)

projection = ccrs.PlateCarree()
levels = np.arange(-16, 48, 4)

cplot = lynx.Contour(ds.U,
                     flevels=levels,
                     clevels=levels,
                     xlim=(-180, 180),
                     ylim=(-90, 90),
                     xticks=np.linspace(-180, 180, 13),
                     yticks=np.linspace(-90, 90, 7),
                     projection=projection,
                     cmap=gvcmaps.ncl_default,
                     maintitle="Default Color",
                     lefttitle=ds.U.long_name,
                     righttitle=ds.U.units)

cplot.show()
