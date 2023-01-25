#!/usr/bin/env python
# coding: utf-8

# # Plotting lines with a Color Map Gradient

# If you find yourself drawing lots of lines with different colors corresponding to a changing variable, you might want to give this idea a try.

# In[1]:


import numpy as np
import matplotlib.pylab as plt
import matplotlib as mpl
import mpl_toolkits.axes_grid1 as axgrid
from mpl_toolkits.axes_grid1 import make_axes_locatable

plt.style.use('dark_background')
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'
plt.rcParams['font.size'] = 22

"""
How to plot several lines on a 
standard plot with a color gradient.
"""

#--------------------------#
#       Data Stuff         #
#--------------------------#
x = np.linspace(0, 2*np.pi, 500)
y = np.cos(2*x) 

#--------------------------#
#     Colormap Stuff       #
#--------------------------#
#note a colormap has RGB values mapped to a value between 0 and 1

cmap = plt.cm.inferno #choose cmap
n = 200 #number of colormap sample points to choose from
colors = cmap(np.linspace(0,1,n)) # sampling n different colors from the colormap

#--------------------------#
#     Plotting Stuff       #
#--------------------------#
fig, ax = plt.subplots(1,1,figsize=(12,8)) # initialize a figure and axis object
# ax.set_facecolor('#430085')
# fig.patch.set_facecolor('#430085')

for i in range(n): #iterate through each line you want to plot with a different color
    ax.plot(x, i*y, color=colors[i])
    
ax.set_title("TITLE")
ax.set_xlabel("X - LABEL")
ax.set_ylabel("Y - LABEL")
    
#--------------------------#
#     Colorbar Stuff       #
#--------------------------#
norm_scaling = mpl.colors.Normalize(vmin=0, vmax=1) #set the max and min y value for your cmap
divider = axgrid.make_axes_locatable(ax)
cax = divider.append_axes("right", size='5%', pad=0.05)
cbar = plt.colorbar(mpl.cm.ScalarMappable(norm=norm_scaling, cmap=cmap), cax=cax)
# cbar = fig.colorbar(mpl.cm.ScalarMappable(norm=norm_scaling, cmap=cmap), ax=ax) #create color bar object
cbar.set_label("TESTING",rotation=270,labelpad=30) #give cbar a label and rotate it 

fig.tight_layout() #tidy up the figure

plt.show()
    
    


# ## Load into Cycler
# 
# If you want to get some hexidecimal values to load into a cycler in a .mplstyle file, just use this:

# In[2]:


cmap = plt.cm.prism #choose cmap
n = 10 #number of colormap sample points to choose from
colors = cmap(np.linspace(0,1,n)) # sampling n different colors from the colormap
print([mpl.colors.to_hex(colors[i])[1:] for i in range(n)])


# In[ ]:




