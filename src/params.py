DATA_FOLDER = '/src/data'
RESULTS_FOLDER = '/src/results'
TENSORBOARD_BASE_FOLDER = 'tensorboard'
INDICES_FILE = 'Data_Entry_2017.csv'

WEIGHT_FILE_NAME = "{val_loss:.2f}_weights.best.hdf5"

MIN_CASES = 1000

# Pretrained network image sizes
IMG_SIZE = (512, 512)
VGG19_IMG_SIZE = (224,224)
MOBILENET_IMG_SIZE = (224,224)
INCEPTIONRESNETV2_IMG_SIZE= (299,299)
INCEPTIONV3_IMG_SIZE= (299,299)
MOBILENETV2_IMG_SIZE = (224,224)
NASNETLARGE_IMG_SIZE = (224,224)


LEARNING_RATE = 0.0005
SYNTHETIC_BATCH_SIZE = 256
BATCH_SIZE = 32
ACCUMULATION_STEPS = int(SYNTHETIC_BATCH_SIZE / BATCH_SIZE)
VALIDATION_BATCH_SIZE = BATCH_SIZE*4
EPOCHS = 100
EARLY_STOPPING_PATIENCE = 5
RL_PLATEAU_PATIENCE = 2
WORKERS = 8
