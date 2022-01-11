#input=../dataset/Occluded_Duke/bounding_box_train
#output=../test_pose_storage/train
#CUDA_VISIBLE_DEVICES=0 python3 demo.py --indir $input --outdir $output --format open --vis_fast
#python generate_heatmap.py $input ../heatmaps/18heatmap_train $output
#
#input=../dataset/Occluded_Duke/bounding_box_test
#output=../test_pose_storage/gallery
#CUDA_VISIBLE_DEVICES=0 python3 demo.py --indir $input --outdir $output --format open --vis_fast
#python generate_heatmap.py $input  ../heatmaps/18heatmap_gallery $output
#
#
input=/home/eini/QHB/Pose_Guided_Occluded_Person_ReID-master/AlphaPose/examples/demo
output=/home/eini/QHB/Pose_Guided_Occluded_Person_ReID-master/AlphaPose/examples/res
#CUDA_VISIBLE_DEVICES=0 python3 demo.py --indir $input --outdir $output --format open --vis_fast
python generate_heatmap.py $input  /home/eini/QHB/Pose_Guided_Occluded_Person_ReID-master/AlphaPose/examples/res/heatmap $output

