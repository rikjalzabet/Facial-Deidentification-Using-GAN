import glob
import random
import os
import numpy as np

from torch.utils.data import Dataset
from PIL import Image
import torchvision.transforms as transforms


class ImageDataset(Dataset):
    def __init__(self, input_folder, output_folder, transforms_=None, mode="train", ):
        self.transform = transforms.Compose(transforms_)

        self.files_A = sorted(glob.glob(os.path.join(input_folder, "*.*")))
        self.files_B = sorted(glob.glob(os.path.join(output_folder, "*.*")))
        
        # self.files = sorted(glob.glob(os.path.join(root, mode) + "/*.*"))
        # if mode == "train":
        #     self.files.extend(sorted(glob.glob(os.path.join(root, "test") + "/*.*")))
        
        assert len(self.files_A) == len(self.files_B), "Folders must have the same number of files."
    
    def __getitem__(self, index):

        # img = Image.open(self.files[index % len(self.files)])
        # w, h = img.size
        # img_A = img.crop((0, 0, w / 2, h))
        # img_B = img.crop((w / 2, 0, w, h))

        # if np.random.random() < 0.5:
        #     img_A = Image.fromarray(np.array(img_A)[:, ::-1, :], "RGB")
        #     img_B = Image.fromarray(np.array(img_B)[:, ::-1, :], "RGB")

        # img_A = self.transform(img_A)
        # img_B = self.transform(img_B)
        
        img_A_path = self.files_A[index % len(self.files_A)]
        img_B_path = self.files_B[index % len(self.files_B)]
        
        img_A = Image.open(img_A_path).convert("RGB")
        img_B = Image.open(img_B_path).convert("RGB")
        
        img_A = self.transform(img_A)
        img_B = self.transform(img_B)

        return {"A": img_A, "B": img_B}

    def __len__(self):
        return len(self.files_A)
