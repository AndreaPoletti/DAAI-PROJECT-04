# Functions for evaluating/visualizing the network's output

## evalAnomaly.py

This code can be used to produce anomaly segmentation results on various anomaly metrics.

**Examples:**
```
python evalAnomaly.py --input '/home/shyam/ViT-Adapter/segmentation/unk-dataset/RoadAnomaly21/images/*.png' --method 'Max_logits'
```

## test_methods.py

This code can be used to run the evalAnomaly.py script with different methods and test datasets at once. 


## evalAnomaly_T.py

This code can be used to produce anomaly segmentation results with the Temperature calibrated Maximum Softmax Probability method. 


**Examples:**
```
python evalAnomaly_T.py --input '/home/shyam/ViT-Adapter/segmentation/unk-dataset/RoadAnomaly21/images/*.png' --temperature 1
```

## test_T.py

This code can be used to run the evalAnomaly_T.py script with different methods and test datasets at once. 

## eval_iou.py 

This code can be used to calculate the IoU (mean and per-class) in a subset of images with labels available, like Cityscapes val/train sets.

**Options:** Specify the Cityscapes folder path with '--datadir' option. Select the cityscapes subset with '--subset' ('val' or 'train'). For other options check the bottom side of the file.

**Examples:**
```
python eval_iou.py --datadir /home/datasets/cityscapes/ --subset val
```

## eval_forwardTime.py
This function loads a model specified by '-m' and enters a loop to continuously estimate forward pass time (fwt) in the specified resolution. 

**Options:** Option '--width' specifies the width (default: 1024). Option '--height' specifies the height (default: 512). For other options check the bottom side of the file.

**Examples:**
```
python eval_forwardTime.py
```




