import argparse
import numpy as np
import os
parser = argparse.ArgumentParser()
parser.add_argument("-in","--path_input", type=str, help="the path of input file")
parser.add_argument("-label","--label_path", type=str, help="the path of label file")
parser.add_argument("-out","--path_output", type=str, help="the path of output file")
parser.add_argument("-w","--window_size", type=int, help="the window_size of feature")
parser.add_argument("-dt","--data_type", type=str, help="the data type of feature")


def loadData(path):
    print(path)
    if path.endswith(".npy"):
        Data = np.load(path)  # 使用 np.load 来加载 .npy 文件
        Data = np.squeeze(Data, axis=0) 
        print(Data.shape)
    else:
        Data = np.loadtxt(path)  # 使用 np.loadtxt 来加载其他文本文件
        print(Data.shape)
    return Data
    
def loadlabel(path):
    f=open(path,'r')
    lines = f.readlines()
    y_data = np.array([int(x) for x in lines[0].strip()])
    return(y_data.astype('float16'))

def saveData(path, data,label):
    #data= data[:, np.newaxis, :, :]
    
    #print(data.shape)
    #print(label.shape)
    np.save(path+"/data.npy", data)
    np.save(path+"/label.npy",label)

def get_series_feature(data, window_size):
    new_dim = window_size * 2 + 1
    padded_data = np.pad(data, ((window_size, window_size), (0, 0)), mode='constant')
    result = np.zeros((data.shape[0], new_dim, data.shape[1]))
    for i in range(data.shape[0]):
        start_idx = i
        end_idx = i + new_dim
        for j in range(start_idx, end_idx):
            result[i][j - start_idx] = padded_data[j]
    print(result.shape)
    #print(result)
    return result

    

def main(path_input, path_output, window_size,data_type,label_path):
    result=[]
    label=[]
    input=os.listdir(path_input)
    print(input)
    for i in input:
        if i.endswith(data_type):
            file_name = i.split(".")[0]
            data = loadData(path_input + "/" + i)
            result.append(get_series_feature(data, window_size))
            
            label_file = label_path + "/" + file_name + ".label"
            if os.path.exists(label_file):
                label.append(loadlabel(label_file))
            else:
                print(f"Warning: {label_file} not found.")

    #label=np.array(label)
    print(len(label))
    labels=np.concatenate(label, axis=0)
    labels = np.expand_dims(labels, axis=1)
    data = np.concatenate(result, axis=0)
    data = np.expand_dims(data, axis=1)
    saveData(path_output, data,labels)
        

if __name__ == "__main__":
    args = parser.parse_args()
    path_input = args.path_input
    path_output = args.path_output
    window_size = args.window_size
    label_path=args.label_path
    data_type=args.data_type
    main(path_input, path_output, window_size,data_type,label_path)





