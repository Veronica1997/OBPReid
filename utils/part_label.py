# import cv2 as cv
import numpy as np
import scipy
from PIL import Image
import os
import scipy
import json
def part_label_generate(path,imgname,part_num,imgh):
    global final_point
    if not os.path.isfile(os.path.join(path,imgname+'.json')): ##If there is no pose json file, part_label=1
        final_label=np.ones(part_num)
    else:
        with open(os.path.join(path,imgname+'.json'),'r') as f:
            a=json.load(f)
            person=a['people']
        p_count=0
        if len(person)==0:
            final_label=np.ones(part_num)
            print('no detected person')
            return final_label
        ####If there are more than one person, use the person with the largest number of landmarks 
        for i in range(len(person)):
            p_points=person[i]
            p_points=p_points['pose_keypoints_2d']
            p_points=np.array(p_points)
            p_points=p_points.reshape(18,3)
            p_points=p_points[p_points[:,2]>0.2]
            count=p_points.shape[0]
            if count>=p_count:
                final_point=p_points
                p_count=count
        ####
        if final_point.shape[0]<3:
            final_label=np.zeros(part_num)
        else:
            label = np.zeros(part_num)
            for j in range(len(final_point)):
                w,h = final_point[j][:2]
                for k in range(part_num):
                    mark = 0
                    if h > (float(k) / part_num) * imgh and h < (float(k + 1.) / part_num) * imgh:
                        label[k]=1
                        for i in range(len(person)):
                            p_point = person[i]
                            p_point = p_point['pose_keypoints_2d']
                            p_point = np.array(p_point)
                            p_point = p_point.reshape(18, 3)
                            p_point = p_point[p_point[:, 2] > 0.2]
                            counts = p_point.shape[0]
                            if counts != p_count:
                                for n in range(len(p_point)):
                                    w1, h1 = p_point[n][:2]
                                    if h1 > (float(k) / part_num) * imgh and h1 < (float(k + 1.) / part_num) * imgh:
                                        mark=mark+1
                        if mark > 2:
                            label[k] = 0
            final_label=label
    return final_label
