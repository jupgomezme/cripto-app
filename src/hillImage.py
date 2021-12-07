import os.path
import pickle
import numpy as np
from numpy.linalg import inv, det
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import sys
import pickle
import scipy.misc
import numpy as np
import imageio
from skimage import io

def transform(np_array, shape):
    return np_array.reshape(shape).astype('uint8')

def read_image(image_path):
    """ Read an image and return a one hot vector of the image"""
    img = imageio.imread(image_path)
    reshape_value = 1

    for i in img.shape:
        reshape_value *= i

    return img.reshape((1, reshape_value)), img.shape


def show_image(image):
    """ Show a single image"""
    plt.imshow(image)
    plt.show()


def show_images(a, b):
    """ Show two images side by side"""
    plot_image = np.concatenate((a, b), axis=1)
    plt.imshow(plot_image)
    plt.show()

class Hill:
    def __init__(self, data, file_name, key_path=None):

        self.data = data

        # Computet the chunk
        self.chunk = self.computer_chunk()

        if key_path:
            print('here')
            # Load the key if she exist in the current dir
            print(key_path)
            self._key = pickle.load(open( key_path, "rb" ))
            print('Usigng the args -k ' + key_path)
        else:
            file_name = file_name + '.key'
            print(file_name)
            if os.path.isfile(file_name):
                print('or here')
                # Load the key if she exist in the current dir
                self._key = pickle.load(open( file_name, "rb" ))
                print('Using the ' + file_name)
            else:
                # Generate a random key
                self._key = np.random.random_integers(0, 100, (self.chunk, self.chunk))
                
                # If determinat is equal to zero regenrate another key
                if det(self._key) == 0:
                    self._key = np.random.random_integers(0, 100, (self.chunk, self.chunk))

                # Save the key in a pickle
                pickle.dump( self._key, open( file_name, "wb" ) )


        # Get the inverse of the key
        self.reversed_key = np.matrix(self._key).I.A


    def computer_chunk(self):
        max_chunk = 100
        data_shape = self.data.shape[1]

        for i in range(max_chunk, 0, -1):
            if data_shape % i == 0:
                return i


    @property
    def key(self):
        return self._key

    def encode(self, data):
        """ Encode function """
        crypted = []
        chunk = self.chunk
        key = self._key

        for i in range(0, len(data), chunk):

            temp = list(np.dot(key, data[i:i + chunk]))
            crypted.append(temp)

        crypted = (np.array(crypted)).reshape((1, len(data)))
        return crypted[0]


    def decode(self, data):
        """ Decode function """
        uncrypted = []
        chunk = self.chunk
        reversed_key = self.reversed_key

        for i in range(0, len(data), chunk):
            temp = list(np.dot(reversed_key, data[i:i + chunk]))
            uncrypted.append(temp)

        uncrypted = (np.array(uncrypted)).reshape((1, len(data)))

        return uncrypted[0]

def hillImageEncryption(image):   
    
    # -----------------------------------------------------------------
    # ------------------------- Encoding part -------------------------
    # -----------------------------------------------------------------
    
    # Get the encdoed vector image
    encoded_image_vector = hill.encode(image)
    
    # Reshape to the original shape of the image
    encoded_image = encoded_image_vector.reshape(original_shape)
    
    # Show the decoded image
    # show_image(encoded_image.astype('uint8'))
    
    # Setup the encdoed file name to be used when saving the encdoed image
    img_name = image_file_name.split('.')[0]
    img_extension = image_file_name.split('.')[1]
    encoded_img_name = '{0}-encoded.{1}'.format(img_name, img_extension)
    
     # Convert to uint8
    encoded_image = encoded_image.astype('uint8')
    
    # Save the image
    io.imsave(encoded_img_name, encoded_image)
    pickle.dump(encoded_image_vector, open( encoded_img_name + '.pk', "wb" ))
    
    return encoded_image,encoded_img_name


# # -----------------------------------------------------------------
# # ------------------------- Decoding part -------------------------
# # -----------------------------------------------------------------

def hillImageDecryption(image):
    
    img_vector = pickle.load(open(image + '.pk', 'rb'))

    # Get the decoded vector image
    decoded_image_vector = hill.decode(img_vector)
    
    # Reshape to the original shape of the image
    decoded_image = decoded_image_vector.reshape(original_shape)
    
    decoded_img_name = '{0}-decoded.{1}'.format(img_name, img_extension)

    # Save the image
    io.imsave(decoded_img_name, decoded_image)
    
    return decoded_image

image_file_name = 'lena.jpg'
img, original_shape = read_image(image_file_name)
hill = Hill(data=img, file_name=image_file_name)
lena = hillImageEncryption(img[0])
lena_2 = hillImageDecryption(lena[1])