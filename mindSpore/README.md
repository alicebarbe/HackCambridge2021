# ResNet50

This folder contains a ResNet model for Image Classification using CIFAR-10 dataset. ResNet50 is convolutional neural network 50 layers deep.



## Requirments

In order to use MindSpore, Windows-x64 is required. Python 3.7.5 must be installed, you can find how to do so [here](https://www.python.org/downloads/release/python-375/). 
For this project we have created a virtual environment local to this repository. This code has been implemented for --divice_target=CPU.


## Folder Structure

Place your test and training files within the `CIFAR-10` folder, the path has been specified within the code therefore it is important to place the target files in the right location.

```
CIFAR-10
   ├─cifar-10-batches-bin
   │
   └─cifar-10-verify-bin

```

### Create a Virtual Env for Python 3.7 with virtualenv

- Install `pyenv`

- install  `pipenv` using `pip install  pipenv` or `pip install -user pipenv`
- navigate to the project directory, in this case ./mindSpore and use the following command:

```
pipenv install --python 3.7
```

now you may follow the instruction to activate your virtual environment. 

### Install MindSpore

To install MindSpore, follow the installation guide [here](https://www.mindspore.cn/install/en). Select your machine specifications to obtain the correct command. 
 
 # Usage

 ## Training
 
 
 ```
 python trainCIFAR10.py --device_target=CPU
 ```

 ## Evaluation


 ```
 python evalCIFAR10.py --device_target=CPU   
 ```
