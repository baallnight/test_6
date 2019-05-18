import tensorflow as tf
class CalcModel:
    def __init__(self):
        self._w1 = tf.placeholder(tf.float32, name = 'w1')
        self._w2 = tf.placeholder(tf.float32, name = 'w2')
        self._feed_dict = {'w1': 8.0, 'w2' : 2.0}

    def create_comm_model(self, type):
        w1 = self._w1
        w2 = self._w2
        feed_dict = self._feed_dict

        if type == 'add': r = tf.add(w1, w2, name='op_add')
        elif type == 'sub': r = tf.subtract(w1, w2, name='op_sub')
        elif type == 'mul': r = tf.multiply(w1, w2, name='op_mul')
        elif type == 'div': r = tf.divide(w1, w2, name='op_div')

        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        result = sess.run(r, {w1: feed_dict['w1'], w2: feed_dict['w2']})
        print('TF {} 결과 {}'.format(type, result))

        saver.save(sess, './saved_'+type+'/model', global_step=1000)

    def create_add_model(self):
        self.create_comm_model('add')

    def create_sub_model(self):
        self.create_comm_model('sub')

    def create_mul_model(self):
        self.create_comm_model('mul')

    def create_div_model(self):
        self.create_comm_model('div')

