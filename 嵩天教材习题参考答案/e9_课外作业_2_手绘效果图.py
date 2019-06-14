from PIL import Image
import numpy as np

vec_e1 = np.pi/2.2
vec_az = np.pi/4
depth = 5
im = Image.open('lwz.jpg').convert('L')
a = np.asarray(im).astype('float')
grad = np.gradient(a)
grad_x, grad_y = grad
grad_x = grad_x * depth/100
grad_y = grad_y * depth/100
dx = np.cos(vec_e1) * np.cos(vec_az)
dy = np.cos(vec_e1) * np.sin(vec_az)
dz = np.sin(vec_e1)
A = np.sqrt(grad_x**2 + grad_y**2 + 1.)
uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A
a2 = 255*(dx * uni_x + dy * uni_y + dz * uni_z)
a2 = a2.clip(0,255)
im2 = Image.fromarray(a2.astype('uint8'))
im2.save('lwzhd.jpg')