import os

# List of evalAnomaly methods you want to test
methods= ["Max_logits"]

# List of datasets you want to test  evalAnomaly methods on
datasets = ["../../Testing_Images/RoadAnomaly/images/*.jpg", "../../Testing_Images/RoadAnomaly21/images/*.png", 
           "../../Testing_Images/RoadObsticle21/images/*.webp", "../../Testing_Images/fs_static/images/*.jpg",
           "../../Testing_Images/FS_LostFound_full/images/*.png"]

for m in methods:
    for dat in datasets:
        print("evalAnomaly.py --method " + m + " --input " + dat)
        os.system("evalAnomaly.py --method " + m + " --input " + dat)