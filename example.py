
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.figure()
years = ['2000','2001','2002','2003','2004']
compounds = ['CO','O3','SOx','NOx','CO','O3','SOx','NOx','CO','O3','SOx','NOx','CO','O3','SOx','NOx','CO','O3','SOx','NOx']
im = plt.imread('map.png')
implot=plt.imshow(im,zorder=1,cmap=plt.cm.gray)
arr = np.load('toy_data.npy')
i = 0
for year in range(5):
    ys = []
    xs = []
    for x in arr[year,4]:
        x += 4.3
        x *= 25/2.
        xs.append(x)
    print(len(xs))
    for y in arr[year,5]:
        y += 5.9
        y *= 25/2.
        ys.append(y)
    print(len(ys))
    np.save('converted',[xs,ys])
    for point in range(4):
        size = arr[year,point]*50000
        plt.figure(i)
        im = plt.imread('map.png')
        implot=plt.imshow(im,zorder=1,cmap=plt.cm.gray)
        plt.title(str(years[year]) + ' [' + str(compounds[i] + ']'))
        plt.scatter(xs,ys,s=size,alpha=0.5,zorder=2)
        ticks = np.arange(40,700,120)
        labels=[0,1,2,3,4,5]
        plt.xticks(ticks,labels)
        plt.xlabel('km')
        yticks = np.arange(480,40,-120)
        ylabels=[0,1,2,3,4,5]
        plt.yticks(yticks,ylabels)
        plt.ylabel('km')
        plt.savefig('test_' + str(i) + '.png')
        i += 1 
