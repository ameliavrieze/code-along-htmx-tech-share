# You may pretend this is a real database :)
import random

images = ["img/3dchungus.gif", "img/contentawarechungus.gif", "img/cubechungus.gif", 
          "img/explodechungus.gif", "img/spherechungus.gif", "img/spinchungus.gif", 
          "img/wavechungus.gif", "img/donutchungus.gif", "img/pyramidchungus.gif", 
          "img/triplechungus.gif",]
def get_images(limit=8):
    rand_images = []
    for i in range(limit):
        rand_images.append(random.choice(images))
    return rand_images


"""
If you're curious, an actual sql query might look like:

('''select * from table
limit %s offset %s;'''
(limit, offset,))

where limit = # of nodes to load at a time
and offset = limit * (current page #)
"""