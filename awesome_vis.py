import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt	# plot the distribution
import seaborn as sns			# for pretty plots
import pprint

flags = tf.app.flags
pp = pprint.PrettyPrinter().pprint

# Assume the operation is type "output = tf.xxxx(input)"
tf.app.flags.DEFINE_string('op', 'tf.identity', 'define the tf operation')
tf.app.flags.DEFINE_integer('dim', 1000, 'defien the input tensor shape')
tf.app.flags.DEFINE_integer('max', 1, 'the max value of the input tensor')
tf.app.flags.DEFINE_integer('min', -1, 'the min value of the input tensor')
conf = flags.FLAGS


def main(_):

	attrs = conf.__dict__['__flags']
	pp(attrs)
	with tf.Session() as sess:
		op = eval(conf.op)
		# assume the input vector is 1D tensor
		input_var = np.linspace(conf.min, conf.max, conf.dim)
		input = tf.placeholder('float32', [conf.dim])
		tf.initialize_all_variables().run()
		output = op(input)
		grad = tf.gradients(output, input)
		result = sess.run([output, grad], feed_dict={
					input:input_var
					})
		plt.plot(input_var, result[0], input_var, result[1][0])
		plt.xlabel('Input')
		plt.title(conf.op)
		plt.legend(['f(x)', 'df(x)/dx'], loc='upper left')
		plt.savefig('img/'+conf.op+'.png')


if __name__ == '__main__':
	tf.app.run()

