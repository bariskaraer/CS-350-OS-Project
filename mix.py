# -*- coding: utf-8 -*-
import os
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

def main():
    
    
    hdd_drive = "C:\\Users\\baris\\Desktop\\hdd\\"

    directory = "C:\\Users\\baris\\Desktop\\Text Files 15 11 2019"

    files = []
    sizes = []
    size_categories = []
    
    for root, dir, file in os.walk(directory):
        for i in file:
            newfile = os.path.join(root, i)
            size = os.path.getsize(str(newfile))
            files.append(newfile)
            sizes.append(float(size))
            size_categories.append(compareSize(size))
            #print(f"{newfile} {size} B")

            size_megabytes = size / 1000000
            #IF size of the file is bigger than 1 mb or is 1 mb than move the file
            if (size_megabytes >= 1) :
                if newfile.startswith(hdd_drive):
                    continue

                total, used, free = shutil.disk_usage(hdd_drive)
                
                if size_megabytes > free * 1000000:
                    print(f"{newfile} {size} B - Not enough space on HDD !")
                    continue

                file_path = newfile.replace(ssd_drive, hdd_drive, 1)
                file_dir = root.replace(ssd_drive, hdd_drive, 1)

                if not os.path.exists(file_dir):
                    os.makedirs(file_dir)

                shutil.move(newfile, file_path)
    
    df = pd.DataFrame({
            'file_name':files,
            'file_size':sizes,
            'size_category':size_categories
            })
    df = df.sort_values(by=['file_size'])
    
    
    
    intervals = ['0K','1K','10K','100K','1M','10M','100M','1GB','∞']
    count_files,fbins = np.histogram(df['size_category'],bins=8)
    plt.hist(df['size_category'],fbins)
    plt.xticks(fbins, intervals)
    plt.xlabel('File Size')
    plt.ylabel('Number of Files')
    plt.title('File Size Distribution Histogram')
    plt.show()
    
    for num, count in enumerate(count_files):
        print("There are {} files with size {} - {}.".format(str(count),intervals[num], intervals[num+1]))

# =============================================================================
#  compareSize returns a number between 0-7 which represents 
#  <1K, <10K, <100K, <1M, <10M, <100M, <1GB, >=1GB, respectively
# =============================================================================
    
def compareSize(sizeB):
    if(sizeB == 0):
        return 0
    else:
        return min(7, max(0, int(math.log10(sizeB))-2))
    
   
    

if __name__ == "__main__":
    main()


