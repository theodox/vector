vector
======

A simple vector math module, suitable for use in Maya python for those who want to avoid Pymel.  

Vectors are derived from `namedtuples` so they are immutable.  There are 3 base vector classes:

**Vector2** is a 2-d XY vector
**Vector3** is a 3-d XYZ vector
**Vector4** is a 4-d XYZW vector

They all provide the follwing operations:

####addition:

    Vector2(1,0) + Vector2(0, 1)
    # Vector2(1,1)
    
####subtraction:

    Vector2(1,1) - Vector2(0, 1)
    # Vector2(1,0)
    
####multiplication:

if the second argument is a vector, do a piecewise vector multiplication: 

    Vector2(1,1) * Vector2(2, 3)
    # Vector2(2,3)

If the second argument is a single number, do a scalar multiplication:

    Vector2(1,1) * 3
    # Vector2(3,3)

####multiplication:

if the second argument is a vector, do a piecewise vector division: 

    Vector2(2,4) / Vector2(4, 2)
    # Vector2(.5,2)

If the second argument is a single number, do a scalar division:

    Vector2(4, 4)  / 2
    # Vector2(2,2)

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
   
 




  
  
