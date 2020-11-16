import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from PIL import ImageFile
from numpy import expand_dims
from werkzeug.utils import secure_filename
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50

ImageFile.LOAD_TRUNCATED_IMAGES = True
model = ResNet50(weights='imagenet')

def classifyImage(file):
    baseFilePath = os.path.dirname(__file__)
    savedFilePath = os.path.join(baseFilePath, r'uploads', secure_filename(file.filename))
    file.save(savedFilePath)
    
    preds = getPrediction(savedFilePath, model)
    prediction = decode_predictions(preds, top=1)
    result = str(prediction[0][0][1])
    return result

def getPrediction(path, model):
    original = image.load_img(path, target_size=(224, 224))
    numpy_image = image.img_to_array(original)
    image_batch = expand_dims(numpy_image, axis=0)

    processed_image = preprocess_input(image_batch, mode='caffe')
    preds = model.predict(processed_image)
    
    return preds