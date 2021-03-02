import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from PIL import ImageFile, Image
from numpy import expand_dims
from werkzeug.utils import secure_filename
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50

ImageFile.LOAD_TRUNCATED_IMAGES = True
model = ResNet50(weights='imagenet')

def classifyImage(file):
    preds = getPrediction(file, model)
    prediction = decode_predictions(preds, top=1)
    result = str(prediction[0][0][1])
    return result

def getPrediction(img_bytes, model):
    original_image = Image.open(img_bytes)
    original_image = original_image.convert('RGB')
    original_image = original_image.resize((224, 224), Image.NEAREST)
    
    numpy_image = image.img_to_array(original_image)
    image_batch = expand_dims(numpy_image, axis=0)

    processed_image = preprocess_input(image_batch, mode='caffe')
    preds = model.predict(processed_image)
    
    return preds