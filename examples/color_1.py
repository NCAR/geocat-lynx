import xarray as xr
import numpy as np
import cartopy.crs as ccrs

import geocat.datafiles as gdf
from geocat.viz import cmaps as gvcmaps
import lynx

# Open a netCDF data file using xarray default engine and load the data into xarray
ds = xr.open_dataset(gdf.get("netcdf_files/uv300.nc")).isel(time=1)

projection = ccrs.PlateCarree()

# lynx.contourf(ds, projection,
#               title="Default Color",
#               lefttitle="Zonal Wind",
#               righttitle="m/s",
#               colormap=gvcmaps.ncl_default,
#               levels=levels)
