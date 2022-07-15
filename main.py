
#import matplotlib.pyplot as plt
#import numpy as np

'''#Plot1:
x = np.array([1,2,7,9])
y = np.array([3,8,1,10])

plt.subplot(3,2,1)
plt.plot(x,y, 'o-b')
plt.title("Example Plot")
plt.xlabel("Frequency")
plt.ylabel("Data")
plt.grid(color = 'g', linestyle = '--', linewidth = 0.5)

#Plot2:
x = np.array([0,1,2,3])
y = np.array([6,2,7,11])

plt.subplot(3,2,6)
plt.plot(x,y, 's-r')
plt.title("Example Plot")
plt.xlabel("Frequency")
plt.ylabel("Data")
plt.grid(color = 'g', linestyle = '--', linewidth = 0.5)'''


#######################
#Create Scatter Plot
'''x = np.array([5,7,3,5,8,9,3,10,15,11,12])
y = np.array([89,70,60,90,78,65,89,78,94,71,58])

plt.scatter(x,y, color='g')

x = np.array([4,9,4,10,1,2,3,10,15,11,12])
y = np.array([89,70,60,90,78,65,30,45,65,78,63])

plt.scatter(x,y, color='b')'''

#####################
##BAR PLOT

'''x = np.array(["Apple", "Banana", "Mango"])
y = np.array([5,7,10])

plt.barh(x,y,height=0.1 ,color='r')'''

###################
#Histogram
'''x = np.random.normal(150, 5, 300)
plt.hist(x)'''

########################
#Pie Charts
'''mylabels = ['A', 'B', 'C', 'D', 'E', 'F']
a = np.array([45,15,10,10,15,5])
myexp=[0.2, 0.1, 0.5, 0.2, 0.1, 0.1]
plt.pie(a, labels = mylabels, explode=myexp, shadow=True)
plt.legend(title = "Example Pie Plot")'''

#Show
#plt.show()

###############################################################################
input_dir = "E:/NOAMI/Python Course Materials/Module13"
import pandas as pd
import os

output_path = "E:/NOAMI/Python Course Materials/Module13"
output_dir = os.path.join(output_path, 'output')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

os.chdir(input_dir)
for filename in os.listdir():
    if filename.endswith('.csv'):
        print(filename)
        file_name, file_ext = os.path.splitext(filename)
        new_name = '{}{}{}'.format(file_name, '_daily', file_ext)
        df = pd.read_csv(filename, index_col=0, parse_dates=True)
        print(df)
        data_df = df.resample("D").mean()
        print(data_df)
        data_df.to_csv(os.path.join(output_dir, new_name), index=True)

print("conversion has been done successfully!")

