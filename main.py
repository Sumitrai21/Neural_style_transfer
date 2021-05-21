import os
import torch
import torch.nn as nn
import argparse


if __name__ == '__main__':
    #fixed args

    default_resource_dir = os.oath.join(os.path.dirname(__file__),'data')
    content_images_dir = os.path.join(default_resource_dir,'content-image')
    style_images_dir = os.path.join(defalt_resource_dir,'style-images')
    output_img_dir = os.path.join(default_resource_dir,'output-images')
    img_format = (4,'.jpg')


    #modifiable args

    parser = argparse.ArgumentPareser()
    parser.add_argument('--should_reconstruct_content',type=bool,help='pick between content os style image reconstruction',default=False)
    parser.add_argument('--should_visualize_representation',type=bool,help='visualize feature maps or Gram matrics', default=False)

    parser.add_argument('--content_image_name', type=str,help='content image name',default='lion.jpg')
    parser.add_argument('--style_image_name',type=str,help='style image name', default='ben_giles.jpg')
    parser.add_argument('--height',type=int,help='width of the content and style image(-1 to keep original)',default = 500)

    parser.add_argument('--saving_freq',type=int,help='saving frequency for intermediate images(-1 for final image',default=1)
    parser.add_argument('--model',type=str,choices=['vgg16','vgg19'], default='vgg19')
    parser.add_argument('--optimizer',type=str,choices=['lbfgs','adam'],default='lbfgs')
    args = parser.parse_args()

    #wrapping settings into a dictionary

    optimizer_config = dict()
    for arg in vars(args):
        optimizer_config[arg] = getattr(args,arg)

    optimizer_config['content_images_dir'] = content_images_dir
    optimizer_config['style_images_dir'] = style_images_dir
    optimizer_config['output_img_dir'] = output_img_dir
    optmizer_config['img_format'] = img_format


    reconstruct_image_from_representation(optimizer_config)