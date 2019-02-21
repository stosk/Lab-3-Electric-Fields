
# coding: utf-8

# In[2]:


#Physics 216
#Plotting code to use the whole year!
#Jaylene Naylor
#September 2015, modified Sept 2017, August 2018
#-------------------------------------------#
get_ipython().run_line_magic('matplotlib', 'inline')
#Import packages and libraries needed and give them shortcut names
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#-------------------------------------------#
#Data Section - Create Arrays for data. Perform necessary calculations
#CHANGE THE VARIABLE NAMES and numbers to match your data
xvariable_rmid = np.array([1.75,2.25,2.75,3.25,3.75,4.25,4.75,5.25,5.75,6.25,6.75,7.25]) #what are units?
yvariable_Vavg = np.array([32,66,60,52,31,34,77,52.5,97.5,90.4,111.5,195.1]) #what are units?
ln_rmid = np.log(xvariable_rmid)
ln_Vavg = -np.log(yvariable_Vavg)

#--------------------------------------------#
#Create arrays for uncertainties
#CHANGE THE VARIABLE NAME and numbers to match your data 
err_E = np.array([0.3432,0.3432,0.3432,0.3432,0.3432,0.3432,0.3432,0.3432,0.3432,0.3432,0.3432,0.3432])


#--------------------------------------------#
#Re-assign variables as x, y, dy so that the following code may remain generic

x = ln_rmid   #this should be the array you want to plot on the x axis
y = ln_Vavg
dy = err_E  #this should be your error in y array

#----------------------------------------------#
#Don't need to change anything in this section!
 
#Find the intercept and slope, b and m, from Python's polynomial fitting function
b,m=np.polynomial.polynomial.polyfit(x,y,1,w=dy)

#Write the equation for the best fit line based on the slope and intercept
fit = b+m*x

#Calculate the error in slope and intercept 
#def Delta(x, dy) is a function, and we will learn how to write our own at a later date. They are very useful!
def Delta(x, dy):
    D = (sum(1/dy**2))*(sum(x**2/dy**2))-(sum(x/dy**2))**2
    return D
 
D=Delta(x, dy)
 
dm = np.sqrt(1/D*sum(1/dy**2)) #error in slope
db = np.sqrt(1/D*sum(x**2/dy**2)) #error in intercept

#Calculate the "goodness of fit" from the linear least squares fitting document
def LLSFD2(x,y,dy):
    N = sum(((y-b-m*x)/dy)**2)
    return N
                      
N = LLSFD2(x,y,dy)

#-----------------------------------------------------------------------#
#Plot data on graph. Plot error bars and place values for slope, error in slope and goodness of fit on the plot using "annotate"
plt.figure(figsize=(15,10))
 
plt.plot(x, fit, color='green', linestyle='--')
plt.scatter(x, y, color='blue', marker='o')
 
 
#create labels  YOU NEED TO CHANGE THESE!!!
plt.xlabel('ln rmid (m)')
plt.ylabel('ln Vavg (Volts)')
plt.title('ln rmid (m) vs ln Vavg (V)')
 
plt.errorbar(x, y, yerr=dy, xerr=None, fmt="none") #don't need to plot x error bars
 
plt.annotate('Slope (V/m) = {value:.{digits}E}'.format(value=m, digits=2),
             (0.65, 0.9), xycoords='axes fraction')
 
plt.annotate('Error in Slope (V/m) = {value:.{digits}E}'.format(value=dm, digits=1),
             (0.65, 0.85), xycoords='axes fraction')
 
plt.annotate('Goodness of fit = {value:.{digits}E}'.format(value=N, digits=2),
             (0.65, 0.80), xycoords='axes fraction')

plt.show()

