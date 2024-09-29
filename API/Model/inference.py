from Model.utilities import extract_mfcc,load_model
import numpy as np



def Inference(audio_url:str):
    model=load_model()
    test_mfcc = extract_mfcc(audio_url)
    test_mfcc = np.expand_dims(test_mfcc, axis=0) 
    predicted_class = np.argmax(model.predict(test_mfcc))
    class_labels = ['German', 'English', 'Spanish']
    predicted_label = class_labels[predicted_class]
    return predicted_label
