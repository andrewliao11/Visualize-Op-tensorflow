# Visualize_Op
Visualize the tensorflow operation, including f(x), and df(x)/dx   
Just Support the 1D Tensor
## Requirement 
- Python 2.7
- Tensorflow
- seaborn (for beautiful plot)

## Motivation
The auto-grad properties make Tensorflow really mode approachable to a newbie in deep learning/machine learning. However, many people use the operation without knowing the characteristic of those function. So, I develop a simple project to show the ```f(x)``` and ```df(x)/dx```, which aims to help everyone to know those function well.

## Usage
The code is used to help you visualize some "**strange functions**", and you can further analyze its gradient   
Just run the ```awesome_vis.py``` file. And you can further define some spec of your input:   
Ex: ```python awesome_vis.py --op tf.sigmoid --max 10 --min -10 --dim 1000```   
```
dim = 100
max = 10
min = -10
```
## Example
| tf.identity | tf.sigmoid | tf.nn.relu | tf.tanh |
|---|---|---|---|
| ![](https://github.com/andrewliao11/Visualize_Op/blob/master/img/tf.identity.png?raw=true) | ![](https://github.com/andrewliao11/Visualize_Op/blob/master/img/tf.sigmoid.png?raw=true) | ![](https://github.com/andrewliao11/Visualize_Op/blob/master/img/tf.nn.relu.png?raw=true) | ![](https://github.com/andrewliao11/Visualize_Op/blob/master/img/tf.tanh.png?raw=true) |

| tf.cos | tf.sin | tf.exp | tf.sqrt |
|---|---|---|---|
| ![](https://github.com/andrewliao11/Visualize_Op/blob/master/img/tf.cos.png?raw=true) | ![](https://github.com/andrewliao11/Visualize_Op/blob/master/img/tf.sin.png?raw=true) | ![](https://github.com/andrewliao11/Visualize_Op/blob/master/img/tf.exp.png?raw=true) | ![](https://github.com/andrewliao11/Visualize_Op/blob/master/img/tf.sqrt.png?raw=true) |




