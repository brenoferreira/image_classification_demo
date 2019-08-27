import os
import glob
from click.testing import CliRunner
from luminoth.predict import predict

PATH = os.getcwd()
runner = CliRunner()

def get_files():
    return glob.glob(PATH + "/images/*.jpg")

def classify_image(image_file_path):
    image_file_name = image_file_path.split('/')[-1]
    metadata_file_path = "{}/images/{}.metadata.json".format(PATH, image_file_name)
    try:
        result = runner.invoke(predict, [image_file_path])
        print(result)
    except Exception as e:
        print("Error in predicting image {}".format(image_file_path))
        print(e)

def predict_images():
    files = get_files()

    for file in files:
        classify_image(file)

if __name__ == "__main__":
    print("Classifying images")
    predict_images()
    print("Done")

