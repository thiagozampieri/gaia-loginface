import cv2
import sys
import os
import numpy as np
from PIL import Image
import gaia.utils as cfg
import gaia.recognition as recognition

recognizer = recognition.face_recognizer()

def prepare_training_data(data_folder_path):
    dirs = os.listdir(data_folder_path)
    dirs.sort(key=cfg.natural_sort_key)
    images = []
    faces = []
    labels = []
    names = []
    for dir_name in dirs:
        if not dir_name.startswith("s"):
            continue;

        split = dir_name.split('-')
        label = int(split[0].replace("s", ""))
        subject_dir_path = data_folder_path + "/" + dir_name
        subject_images_names = os.listdir(subject_dir_path)

        for image_name in subject_images_names:
            if image_name.startswith("."):
                continue;

            image_path = subject_dir_path + "/" + image_name
            image = cv2.imread(image_path)
            images.append(image)

            cv2.imshow("Training on image...", image)
            cv2.waitKey(100)

            face, rect = recognition.detect_face(image)            

            if face is not None:    
                cv2.imshow("Training on face...", face)
                cv2.waitKey(100)

                faces.append(face)
                labels.append(label)
                name = split[1]
                if (names.count(name) <= 0):
                    names.append(name)


    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    cv2.waitKey(0)
 
    return images, faces, labels, names

def train():
    global recognizer

    print("Preparing data...")
    (images, faces, labels, names) = prepare_training_data("data/subjects")
    recognizer.train(faces, np.array(labels))
    recognizer.write('data/trainer.yml')

    print("Data prepared")
    print("Total images: ", len(images))
    print("Total faces: ", len(faces))
    print("Total labels: ", len(labels))  
    print("Total names: ", len(names))  