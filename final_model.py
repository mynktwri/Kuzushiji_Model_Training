from my_resnet import ResNet
import numpy as np
from keras.models import Sequential
from keras import metrics
import keras
from sklearn import model_selection
import matplotlib.pyplot as plt

with np.load("KKanji/kkanji-imgs.npz") as data:
        imgs = data['arr_0']
with np.load("KKanji/kkanji-labels.npz") as data:
        labels = data['arr_0']
with np.load("KKanji/kkanji-unique-labels.npz") as data:
        unique_labels = data['arr_0']
print("imgs and labels loaded.")

hist = np.histogram(labels, bins=range(0, len(unique_labels)), density=True)
class_weights = hist[0]
# this is to get the weights of each class in the overall 3.8
imgs = imgs.reshape(imgs.shape[0], 64, 64, 1).astype('float32')
imgs_train, imgs_test, labels_train, labels_test = model_selection.train_test_split(imgs, labels, test_size=0.1)
classes = len(unique_labels)

labels_train = keras.utils.to_categorical(labels_train, num_classes=classes)
labels_test = keras.utils.to_categorical(labels_test, num_classes=classes)


#
# '''
# now = datetime.datetime.now()
# logdir = f"logs/%d-%d-%d-%d" %(now.month, now.day, now.hour, now.minute)
# history = model.fit(x=train_imgs, y=train_labels, epochs=3, batch_size=128, verbose=1, validation_split=.1,
#         callbacks=[TBCallback(log_dir=logdir)])
# '''
#
# loss, accuracy = model.evaluate(imgs_test, labels_test)
# plt.plot(history.history['categorical_accuracy'])
# plt.plot(history.history['val_categorical_accuracy'])
# plt.title('model accuracy')
# plt.ylabel('categorical_accuracy')
# plt.xlabel('epoch')
# plt.legend(['training', 'validation'], loc='best')
# print("Test loss:", loss)
# print("Test accuracy:", accuracy)
# plt.show()
