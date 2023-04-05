import numpy as np
import config
import pickle
import json

class TestModel():

    def __init__(self):

        self.model = pickle.load(open(config.MODEL_FILE_PATH,'rb'))
        self.scaler = pickle.load(open(config.SCALER_FILE_PATH,'rb'))
        self.model_data = json.load(open(config.MODEL_DATA_FILE,'r'))

    def result(self,age,bmi,children,smoker,region):

        test_array = np.zeros(self.model.n_features_in_)

        test_array[0] = age
        test_array[1] = bmi
        test_array[2] = children
        test_array[3] = self.model_data['smoker'][smoker]
        ind = self.model_data['feature'].index('region_'+region)
        test_array[ind] = 1

        scaled_array = self.scaler.transform([test_array])

        test = self.model.predict(scaled_array)

        print(f"Insurance amount : ",np.around(test[0],2))

        return np.around(test[0],2)