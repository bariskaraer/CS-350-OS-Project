import os
import numpy as np
import shutil

def main():
    ssd_drive = "C:\\"
    directory = ssd_drive + "Users\\baris\\Desktop\\ssd"
    hdd_drive = "C:\\Users\\baris\\Desktop\\hdd\\"
    files = []

    for root, dir, file in os.walk(directory):
        for i in file:
            newfile = os.path.join(root, i)
            files.append(newfile)
            size = os.path.getsize(str(newfile))
            print(f"{newfile} {size} B")
            size_megabytes = size / 1000000
            if (size_megabytes < 1) :
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


if __name__ == "__main__":
    main()
