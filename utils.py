import pickle
import numpy as np
import config
class HeartData():
    def __init__(self,age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
        print("*****************INIT FUNCTION******************")
        self.age=age
        self.sex=sex
        self.cp=cp
        self.trestbps=trestbps
        self.chol=chol
        self.fbs=fbs
        self.restecg=restecg
        self.thalach=thalach
        self.exang=exang
        self.oldpeak=oldpeak
        self.slope=slope
        self.ca=ca
        self.thal=thal
    
    def __load_saved_data(self):
        model_file_name=config.MODEL_FILE_PATH
        with open(model_file_name,'rb') as f:
            self.model=pickle.load(f)

    def get_predicted_class(self):
        self.__load_saved_data()
        test_array=np.zeros([1,self.model.n_features_in_])
        test_array[0,0]=self.age
        test_array[0,1]=self.sex
        test_array[0,2]=self.cp
        test_array[0,3]=self.trestbps
        test_array[0,4]=self.chol
        test_array[0,5]=self.fbs
        test_array[0,6]=self.restecg
        test_array[0,7]=self.thalach
        test_array[0,8]=self.exang
        test_array[0,9]=self.oldpeak
        test_array[0,10]=self.slope
        test_array[0,11]=self.ca
        test_array[0,12]=self.thal

        predict_class=self.model.predict(test_array)[0]
        return predict_class
