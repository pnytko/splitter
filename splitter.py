import os
from PIL import Image
from itertools import product
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, required=True)
parser.add_argument('--dir_in', type=str, required=True)
parser.add_argument('--t_size', type=int, required=True)
args = parser.parse_args()

def split(filename, dir_in, t_size):

    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(dir_in, filename))
    width, height =  img.size

    grid  = product(range(0, height - height % t_size, t_size), range(0, width - width % t_size, t_size))
    t_qty_in_x = int((height - height % t_size)/t_size)
    t_qty_in_y = int((width - width % t_size)/t_size)

    print(f"\nW osi x będzie {t_qty_in_x} tile'i.")
    print(f"W osi y będzie {t_qty_in_y} tile'i.")
    print(f"Łącznie otrzymano {t_qty_in_x * t_qty_in_y} tile'i. ")

    out_folder_name= (f'{name}_tiled')
    out_folder_path = dir_in + '\\' + out_folder_name
    os.makedirs(out_folder_name, exist_ok=True)
    
    for i, j in grid:
        box = (j, i, j + t_size, i + t_size)
        out = os.path.join(out_folder_path, f'{name}_{i}_{j}{ext}')
        img.crop(box).save(out)

    print('\nWygenerowano tile.')

split(args.name, args.dir_in, args.t_size)