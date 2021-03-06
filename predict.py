import keras
from dilated_unet import UNet
from keras.models import load_model
from dilated_unet import bce_dice_loss
from dilated_unet import dice_coef
import tifffile as tiff
keras.losses.bce_dice_loss = bce_dice_loss
keras.metrics.dice_coef = dice_coef
import numpy as np
import mahotas as mh
from tifffile import imsave

model = load_model('weights/normal_unet_20M.weights')

normalize = lambda x: (x - mean) / (std_dev + 1e-10)

test = tiff.imread('test/test-volume.tif')
#test.shape() (30,512,512)
mean, std_dev = np.mean(test), np.std(test)
normalize = lambda x: (x - mean) / (std_dev + 1e-10)

test = normalize(test)

#test_preds = model.predict(test)

out = model.predict(test,batch_size=10)
imsave('test/test_predictions/test_preds.tif',out)
