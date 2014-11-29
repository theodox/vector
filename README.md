vector
======

A simple vector math module, suitable for use in Maya python for those who want to avoid Pymel.  Technically it will work for any vector math but I'd recommend using a C-based alternative (such as [numpy](http://www.numpy.org/) for any application with hard-core performance constraints.

installation
===========
The module is a single python file (`vector.py`)  which depends only on the standard library. Just drop it into any folder on your python path (either site-packages or another  and import it:

    from Vector import Vector2, Vector3


functionality
=============
There are 3 base vector classes:

- **Vector2** is a 2-d XY vector.
- **Vector3** is a 3-d XYZ vector.
- **Vector4** is a 4-d XYZW vector.

Typical usage would be:

    v = Vector2 ( 1.0, 0.0)

or using *args on existting iterable:

    example = [1.0., 0.0] # any iterable with 2 items
    v = Vector2(*example)

or assigning explicitly.

    example = Vector2(x = 1.0, y=2.0)

You can create integer or float versions by providing integers or floats at start (the math will follow the usual python float/vector rules).  `VectorN` classes are _tuples_, so they are immutable - you cannot assign to their values after they are created.

####addition:

    Vector2(1,0) + Vector2(0, 1)
    # Vector2(x=1,y=1)
    
####subtraction:

    Vector2(1,1) - Vector2(0, 1)
    # Vector2(x=1, y=0)
    
####multiplication:

if the second argument is a vector, do a piecewise vector multiplication: 

    Vector2(1,1) * Vector2(2, 3)
    # Vector2(x=2, y=3)

If the second argument is a single number, do a scalar multiplication:

    Vector2(1,1) * 3
    # Vector2(x=3 ,y=3)

####multiplication:

if the second argument is a vector, do a piecewise vector division: 

    Vector2(2.0, 4.0) / Vector2(4, 2)
    # Vector2(x = .5, y=2.0)

If the second argument is a single number, do a scalar division:

    Vector2(4.0, 4.0)  / 2
    # Vector2(x=2.0, y=2.0)

####length():

Returns the length of a vector:

    Vector2(3, 4).length()
    # 5

####normalized():

Returns a normalized copy of the vector.

    Vector2(3, 4).normalized()
    # Vector2(.8, .6)
  
####dot():
Returns the [dot product](http://techartsurvival.blogspot.com/2014/11/bagels-and-coffee-or-vector-dot-product.html) of two vectors:

    Vector2(1,0).dot(Vector2(.707, .707))
    # .707
   
 




  
  
