import tensorflow as tf
from datasets import load_dataset
print("version", tf.__version__)

def resize_images(examples):
    examples["image"] = [tf.image.resize(image, (28, 28)).numpy() for image in examples["image"]]
    return examples

ds = resize_images(load_dataset("viola77data/recycling-dataset"))
split_ratio = 0.8
split_index = int(len(ds) * split_ratio)
train_ds = ds[split_index:]
test_ds = ds[:split_index]

x_train = train_ds["image"]
y_train = train_ds["label"]
x_test = test_ds["image"]
y_test = test_ds["label"]