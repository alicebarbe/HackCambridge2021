# ResNet50
This folder contains a ResNet model for Image Classification using CIFAR-10 dataset. 



## Requirments

In order to use MindSpore window operating system is required. Python 3.7.5 must be installed, you can find how to do so here (). For this project we have created a citual environment local to this repository.

### Create a Virtual Env  for Python 3.7 with virtualenv

- Install `pyenv`

- install  `pipenv` using `pip install  pipenv` or `pip install -user pipenv`
- navigate to the project directory, in this case ./mindSpore and use the following command:

```
pipenv install --python 3.7
```

now you may follow the instruction to actuvate your virtual environment. 

### Install MindSpore

To install MindSpore, follow the installation guide here(https://www.mindspore.cn/install/en). Make sure to select your machine specification to obtain the correct command. 
 
 # Usage

 ## Training

 ```
 python evalCIFAR10.py --device_target=CPU
 ```

 ## Evaluation

 ```
 python trainCIFAR10.py --device_target=CPU
 ```


