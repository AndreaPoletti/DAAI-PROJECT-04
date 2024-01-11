import os

# List of Temperatures you want to test
#temperatures = [0.5, 0.75, 1, 1.1]
temperatures = [10]

# List of datasets you want to test your Temperature method on
datasets = ["../Testing_Images/RoadAnomaly/images/*.jpg", "../Testing_Images/RoadAnomaly21/images/*.png", 
           "../Testing_Images/RoadObsticle21/images/*.webp", "../Testing_Images/fs_static/images/*.jpg",
           "../Testing_Images/FS_LostFound_full/images/*.png"]

#datasets = ["../Testing_Images/RoadObsticle21/images/*.webp"]

for t in temperatures:
    for dat in datasets:
        print("evalAnomaly_T.py --temperature " + str(t) + " --input " + dat)
        os.system("evalAnomaly_T.py --temperature " + str(t) + " --input " + dat)