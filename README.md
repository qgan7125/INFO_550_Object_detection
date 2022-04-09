# INFO 550 Final Project A

## Setup
Please install required dependencies and git repos
```
Python >= 3.7
```

### Setup Virtual Environment
```
# Create virtual environment
python -m venv ODenv
.\ODenv\Scripts\activate # For windows
source ODenv/bin/activate # For mac

# Update pip
python -m pip install --upgrade pip
```

### Download yolov5 and install required packages for yolo5
```
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```
yolov5 has several pretrained models. Review [yolov5](https://github.com/ultralytics/yolov5) for more information.

### Install PyTorch
Please review the [PyTorch Website](https://pytorch.org/) to find the best version for your computer. 

(Note: If you have GPU, download GPU version which will train your model quicker)

My setup for Mac and Windows. There is a new version Pytorch released so some old version could be installed by pip.
```
# For windows
pip3 install torch torchvision torchaudio

# For Mac
pip3 install torch torchvision torchaudio
```

## Train Custom Data 
[yolov tutorial](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data)
```
# inside the yolov5 folder to train model
cd yolov5
python train.py --img 640 --batch 16 --epochs 200 --data data_pokemon.yaml --weights yolov5s.pt    
```


## Jupyter Notebook or Python Program
This project provide Jupyter Notebook version and Python version

If you want to use Jupyter Notebook, Please install Jupyter in your virtual environment
```
pip install ipykernel
python -m ipykernel install --user --name=ODenv
```


## Reference
This project learnt from [Deep Drowsiness Detection using YOLO, Pytorch and Python](https://www.youtube.com/watch?v=tFNJGim3FXw) and [Git repo](https://github.com/nicknochnack/YOLO-Drowsiness-Detection)

Thank Nicholas Renotte for providing tutorial. [Git](https://github.com/nicknochnack) and [Youtube](https://www.youtube.com/channel/UCHXa4OpASJEwrHrLeIzw7Yg)
