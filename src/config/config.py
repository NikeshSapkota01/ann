"""
This config file should hold all static parameters - everything is changed here (except from the networks structure) 
"""
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
from datetime import datetime
from src.utils.file_operations import *

################### PARAMETER for Preprocessing ###########################
data = dict(
    # datalist = ['data2014','data2015','data2016'],
    datalist=['data'],
    filterbool=False,
    frequency=1,  # values per hour
    minmaxscale=True,
    sequencelength=24,  # 24 h
    num_of_samples=64,
)


windowing = dict(  # window characteristics
    windowlength=6,
    windowshift=1,
)


###################### data parameter #####################################
# these are the fields I am considering to use
fields = dict(
    allfields=['temperature', 'relativeHumidity', 'deltaP',  # 'p0',
               'cloudiness', 'windSpeed', 'windDirection_oneHot',
               'precipitation', 'month', 'hour per day'],  # allfields = ['temperature'],
)
label = 'temperature'

prediction = dict(
    pos=fields['allfields'].index(label),
    num_predictions=24,
    label=label,
)

fitler = dict(
    N=2,  # Filter order
    Wn=0.7,  # Cutoff frequency
)

datapaths = dict(
    data='data/weatherData.csv',
)


#####################################################################################
##################### Tensorflow parameters #########################################
####################################################################################

now = datetime.utcnow().strftime("%Y%m%d%H%M%S")

Tensorboard = dict(
    logdir=create_directory("_TEST1"),
    saverpath= create_directory("saver"),
    savetoTensorboard=True,
)

NN_input = dict(
    height=windowing['windowlength'],
    width=6,
    channels=1,
)

NN_CNN = dict(

    ### convlayer1###
    conv1_fmaps=8,  # 8, #32
    conv1_ksizex=3,
    conv1_ksizey=3,
    conv1_stride=1,
    conv1_pad="SAME",

    ### convlayer2###
    conv2_fmaps=8,  # 8, #64
    conv2_ksizex=2,
    conv2_ksizey=2,
    conv2_stride=1,
    conv2_pad="SAME",

    ### convlayer3###
    conv3_fmaps=16,  # 32
    conv3_ksizex=2,
    conv3_ksizey=2,
    conv3_stride=1,
    conv3_pad="SAME",

    ### convlayer4###
    conv4_fmaps=32,  # 64
    conv4_ksizex=3,
    conv4_ksizey=3,

    conv4_stride=1,
    conv4_pad="SAME",

    ### convlayer5###
    conv5_fmaps=64,  # 16, #32
    conv5_ksizex=3,
    conv5_ksizey=3,

    conv5_stride=1,
    conv5_pad="SAME",

    ### convlayer6###
    conv6_fmaps=128,  # 32, #64
    conv6_ksizex=2,
    conv6_ksizey=2,
    conv6_stride=1,
    conv6_pad="SAME",
)

NN_LSTM = dict(
    # data['sequencelength']-windowing['windowlength']+1,#64, #hidden LSTM units
    num_unitsLSTM=128,
    # data['sequencelength']-windowing['windowlength'],  # 14 size of batch
    batch_size=128,
    n_layersLSTM=2,
)

NN_Dense = dict(
    n_fc1=512,  # 1024
    n_fcout=64,  # 512,
    n_outputs=prediction['num_predictions'],
)


Modelparameter_highlevel = dict(
    dropout=0.2,  # 0.2,
    l2_reg_param=0.00001,
    learningrate=0.00005,
    # n_epochs = 25,
    n_inputs=NN_input['height'] * NN_input['width'],
    n_outputs=NN_Dense['n_outputs'],
    batchsize=128,  # int((data['sequencelength']-windowing['windowlength'])),
)
