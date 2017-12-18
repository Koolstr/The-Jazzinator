import urllib
import zipfile
import nottingham_util
import rnn

zip = zipfile.ZipFile(r'datas.zip')  
zip.extractall('data')  

# build the model
nottingham_util.create_model()

# train the model
rnn.train_model()
