from log import logger
from pathlib import Path
import json
import random
import shutil
from tqdm import tqdm

# A helper to do some independent works
# Trait it as a draft
# this runs alone


def merge_dir():
    for i in range(0, 60):
        p = Path("train/data/train", str(i))
        if not p.exists():
            p.mkdir()

    file_train = json.load(
        open(
            "train/data/temp/labels/AgriculturalDisease_train_annotations.json",
            "r",
            encoding="utf-8",
        )
    )
    file_val = json.load(
        open(
            "train/data/temp/labels/AgriculturalDisease_validation_annotations.json",
            "r",
            encoding="utf-8",
        )
    )

    file_list = file_train + file_val

    for file in tqdm(file_list):
        filename = file["image_id"]
        origin_path = Path("train/data/temp/images/", filename)
        ids = file["disease_class"]
        if ids == 44:
            continue
        if ids == 45:
            continue
        if ids > 45:
            ids = ids - 2
        save_path = Path("train/data/train/", str(ids))
        if origin_path.exists():
            shutil.copy(origin_path, save_path)


def sampling():
    #     image_dir = Path("train/data/temp/images")
    #     xxx_dir = Path("train/data/temp/unused")

    #     img_del = random.sample(list(image_dir.iterdir()), 5000)
    #     [shutil.move(x, xxx_dir) for x in img_del]

    img_num = len([])
    logger.debug(img_num)


sampling()
