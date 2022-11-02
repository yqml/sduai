## Graphial illustration of sequence.
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# print(matplotlib.__version__)


# # 折线图
# xpoints = np.array([1, 2, 6, 8])
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(xpoints, ypoints)
# plt.show()
#
# breakpoint()
#
# ## Default X-Points
# # ypoints = np.array([3, 8, 1, 10, 5, 7])
# # plt.plot(ypoints)# Default X-Points
# # plt.plot(ypoints, marker = 'D')# x,X,+,P,s,D,d,p,H,h,v,^,<,>,1,2,3,4,|,_
# # plt.show()
#
# ## Mark each point with a circle
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, 'o')
# # plt.plot(ypoints, 'o:m')# r red, g green, b blue, c cyan, m magenta, y yellow, k black, w white.
# plt.show()


## Many many mec,mfc
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'o', ms = 20)# Set the size of the markers to 20
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')# Set the EDGE color to red
# plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')# Set the face color to red
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')# Set both the EDGE and face color to red
# plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')# Use Hexadecimal color values
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')# Use 140 supported color names.
# plt.show()


### Linestyle
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, ls = 'dotted')
# plt.plot(ypoints + 1, ls = 'dashed')
# plt.plot(ypoints + 2, ls = 'solid')
# plt.plot(ypoints + 3, ls = 'dashdot')
# plt.plot(ypoints + 4, ls = 'None')
# plt.show()


## line color and line width
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, color = 'r')
# plt.plot(ypoints + 1, color = '#4CAF50')
# plt.plot(ypoints + 2, color = 'hotpink')
# plt.plot(ypoints + 3, linewidth = '10')
# plt.show()


### Labels for a plot
# x = np.array([80,  125])
# y = np.array([240, 330])

# plt.plot(x, y)
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# plt.title("Sports Watch Data")
# plt.grid()
# plt.show()


## Font properties for title and lables
# x = np.array([80,  125])
# y = np.array([240, 330])
#
# font1 = {'family':'serif','color':'blue','size':20}
# font2 = {'family':'serif','color':'darkred','size':15}
#
# plt.title("Sports Watch Data", fontdict = font1, loc = 'left')# location of title: left, right, center
# plt.xlabel("Average Pulse", fontdict = font2)
# plt.ylabel("Calorie Burnage", fontdict = font2)
#
# plt.plot(x, y)
#
# plt.show()

## Grid and grid options
# x = np.array([80,  125])
# y = np.array([240, 330])
# plt.grid()
# plt.plot(x, y)
# plt.show()

# only vertical grid
# x = np.array([80,  125])
# y = np.array([240, 330])
# plt.grid(axis = 'x')
# plt.plot(x, y)
# plt.show()

# only horizontal grid
# x = np.array([80,  125])
# y = np.array([240, 330])
# plt.grid(axis = 'y')
# plt.plot(x, y)
# plt.show()

# set line properties of grid
# x = np.array([80,  125])
# y = np.array([240, 330])
# plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
# plt.plot(x, y)
# plt.show()



### draw multiple plots in one figure

## The following is row1*col2
# # plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(1, 2, 1)
# plt.plot(x,y)
#
# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(1, 2, 2)
# plt.plot(x,y)
#
# plt.show()


## The following is row2*col1
# # plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(2, 1, 1)
# plt.plot(x,y)
#
# # plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(2, 1, 2)
# plt.plot(x,y)
#
# plt.show()


## The following is for titles in multiple plots
# # plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(1, 2, 1)
# plt.plot(x,y)
# plt.title("SALES")
#
# # plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(1, 2, 2)
# plt.subplots_adjust(wspace=0.8,hspace=1.8)
# plt.plot(x,y)
# plt.title("INCOME")
#
# plt.suptitle("MY SHOP")
# plt.show()
#
# breakpoint()


### Scatter plot
## day one, the age and speed of 13 cars, and two specified colors:
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y, color = 'hotpink')

# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y, color = '#88c999')
# plt.show()

## specify the color of each point
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
# plt.scatter(x, y, c=colors)
#
# plt.show()

## Color map
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
# plt.scatter(x, y, c=colors, cmap='viridis')
# plt.colorbar()
#
# plt.show()

## size and transparency of each point
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
# plt.scatter(x, y, s=sizes, alpha=0.5)
#
# plt.show()

## random arrays, colors, sizes and colormap as well as transparency
# x = np.random.randint(100, size=(100))
# y = np.random.randint(100, size=(100))
# colors = np.random.randint(100, size=(100))
# sizes = 10 * np.random.randint(100, size=(100))
# plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
# plt.colorbar()
#
# plt.show()

##### Bars
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x,y)
# plt.show()
#
# x = ["APPLES", "BANANAS"]
# y = [400, 350]
# plt.bar(x, y)
# plt.show()

## horizontal bar
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
#
# plt.barh(x, y)
# plt.show()

## Bar colors
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
#
# plt.bar(x, y, color = "red")# hotpink,"#4CAF50" etc...
# plt.show()

## vertical bar widths
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
#
# plt.bar(x, y, width = 0.1)
# plt.show()

## horizontal bar height
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
#
# plt.barh(x, y, height = 0.1)
# plt.show()


##### Histogram
# x = np.random.normal(170, 10, 250)
# plt.hist(x)
# plt.show()

##### pie chart
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# plt.pie(y, labels = mylabels)
# plt.show()

## start angle
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# plt.pie(y, labels = mylabels, startangle = 90)
# plt.show()

## 某一个扇形分离
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# myexplode = [0.2, 0, 0, 0]
#
# plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
# plt.show()

## colors for each part
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# mycolors = ["black", "hotpink", "b", "#4CAF50"]
#
# plt.pie(y, labels = mylabels, colors = mycolors)
# plt.show()

## add a legend
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
#
# plt.pie(y, labels = mylabels)
# plt.legend(title = "Four Fruits:")
# plt.show()
#
# breakpoint()




breakpoint()
