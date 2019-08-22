import requests
from PIL import Image
from io import BytesIO

API_URL = 'https://api.creativecommons.engineering/image/search?q={}'

# Image scaled size
IMAGE_SIZE = 300, 300

test_queries = [
    "dog",
    "DNA",
    "F14",
    "cat",
    "WW2",
    "Monet",
    "Edvard Munch",
    "flamingo",
    "weather",
    "Andrew Jackson",
    "maps of the Atlantic",
    "wildlife",
    "reading",
    "Syrian women",
    "medicine",
    "health",
    "periodic table",
    "aardvark",
    "children playing",
    "nurse",
    "basketball team",
    "music",
    "computer",
    "technology",
    "car",
    "books",
    "video",
    "beach",
    "flower",
    "food",
    "tree",
    "people",
    "nature",
    "money",
    "house",
    "school"
]

def search(term):
    response = requests.get(API_URL.format(term))

    if response.status_code == 200:
        json = response.json()

        results = json["results"]

        return results

def get_image_file_data(image_json):
    image_file_url = image_json["url"]

    response = requests.get(image_file_url)

    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        return img

def save_scaled_image(image, name):
    image.thumbnail(IMAGE_SIZE)
    image.save("./images/{}.jpg".format(name), "JPEG")

def do_work():
    for term in test_queries:
        try:
            images_json = search(term)
        except:
            print("Failed to search {}".format(term))
        
        
        for img_json in images_json:
            try:
                img = get_image_file_data(img_json)
            except:
                print("Failed to get image data for {}".format(img_json["id"]))

            try:
                save_scaled_image(img, img_json["id"])
            except:
                print("Failed to save image {}".format(img_json["id"]))

if __name__ == "__main__":
    print("Loading and saving images to images/")
    do_work()
    print("Done")