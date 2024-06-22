<h1>Datathon Solution for challenge 3</h1> 

 This is our team's solution for a datathon held for the bread cancer cause. The challenge 3 was about classifying breast cancer with Hispatology Images.

 <br>

 **About Dataset**
 <br>

Invasive Ductal Carcinoma (IDC) is the most common subtype of all breast cancers. To assign an aggressiveness grade to a whole mount sample, pathologists typically focus on the regions which contain the IDC. As a result, one of the common pre-processing steps for automatic aggressiveness grading is to delineate the exact regions of IDC inside of a whole mount slide.

The original dataset consisted of 162 whole mount slide images of Breast Cancer (BCa) specimens scanned at 40x. From that, 277,524 patches of size 50 x 50 were extracted (198,738 IDC negative and 78,786 IDC positive). Each patch’s file name is of the format: u_xX_yY_classC.png — > example 10253_idx5_x1351_y1101_class0.png . Where u is the patient ID (10253_idx5), X is the x-coordinate of where this patch was cropped from, Y is the y-coordinate of where this patch was cropped from, and C indicates the class where 0 is non-IDC and 1 is IDC.

**Our Solution**

it consists of a model of classifying benign or malign, we did some data visualisations and then we classified with a Simple CNN with EfficientNetB0 pre entrained as a base that achieved an accuracy of 0.71233
 
