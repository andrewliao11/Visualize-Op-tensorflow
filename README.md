# Visualize_Op
Visualize the tensorflow operation, including f(x), and df(x)/dx   
Just Support the 1D Tensor!
## Requirement 
- Python 2.7
- Tensorflow
- seaborn (for beatiful plot)

## Motivation


## Usage
The code is used to help you visualize some "**strange functions**", and you can further analyze its gradient   
Just run the ```awesome_vis.py``` file. And you can further define some spec of your input:   
Ex: ```python awesome_vis.py --op tf.sigmoid --max 10 --min -10 --dim 1000```   
```
dim = 100
max = 10
min = -10
```
| tf.identity | tf.sigmoid | tf.nn.relu | tf.tanh |
|---|---|---|---|
|   |   |   |   |

| tf.cos | tf.sin | tf.floor | tf.ceil |
|---|---|---|---|
|   |   |   |   |




