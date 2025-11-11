from sklearn.utils import shuffle
import os
from tqdm import tqdm
import numpy as np
import tensorflow as tf
import gc

datalabel="RTK_drop"

def data_label():
    return datalabel

#def MCNN_data_load(MAXSEQ):
def MCNN_data_load(WINDOW,DATA_TYPE,DATASET,MAXSEQ):

    #path_m_training = "../dataset/"+str(MAXSEQ)+"/mcarrier/train.npy"
    #path_s_training = "../dataset/"+str(MAXSEQ)+"/secondary/train.npy"
    
    #path_data_training = "../dataset/ATP_549/"+str(DATA_TYPE)+"/"+str(WINDOW)+"/train/data.npy"
    #path_label_training = "../dataset/ATP_549/"+str(DATA_TYPE)+"/"+str(WINDOW)+"/train//label.npy"
    
    path_data_training = "../dataset/"+str(DATA_TYPE)+"/"+str(WINDOW)+"/train/data.npy"
    path_label_training = "../dataset/"+str(DATA_TYPE)+"/"+str(WINDOW)+"/train/label.npy"
    
    #path_data_testing = "../dataset/RTK_69/"+str(DATA_TYPE)+"/"+str(WINDOW)+"/test/data.npy"
    #path_label_testing = "../dataset/RTK_69/"+str(DATA_TYPE)+"/"+str(WINDOW)+"/test/label.npy"
    
    #path_data_testing = "../dataset/RTK_people/prottrans/"+str(WINDOW)+"/test/data.npy"
    #path_label_testing = "../dataset/RTK_people/prottrans/"+str(WINDOW)+"/test/label.npy"
    
    path_data_testing = "../dataset/"+str(DATA_TYPE)+"/"+str(WINDOW)+"/test/data.npy"
    path_label_testing = "../dataset/"+str(DATA_TYPE)+"/"+str(WINDOW)+"/test/label.npy"
    
    x_train,y_train=data_load(path_data_training,path_label_training)
    x_test,y_test=data_load(path_data_testing,path_label_testing)

    
    return(x_train,y_train,x_test,y_test)

def data_load(DATA,LABEL):
    data=np.load(DATA)
    label=np.load(LABEL)
    
    #label1 = np.ones(f1.shape[0])
    #label2 = np.zeros(f2.shape[0])
   
    
    #print(data.shape)
    #print(label.shape)
    
    #print(label1)
    #print(label2)
  
    
    x=data
    y= tf.keras.utils.to_categorical(label,2)
    #y.dtype='float16'
    gc.collect()
    return x ,y