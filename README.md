# PyDMath Version - 0.1
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; This **PyDMath** is a mathematical module, with this you can able to perform a mathematical operations 
which includes mensuration, permutation and combination. We can use any use any type of measurement units but the output will return in SI standard units.
This makes differ from other Python modules.

## Math topics included till now
<ul>
  <li>Mensuration</li>
  <ul>
    <li>Area</li>
    <li>Perimeter</li>
    <li>Volume</li>
   </ul>
  <li>Permutation</li>
  <li>Combination</li>
</ul>

## Input format
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; Inputs must be a string seperated by "-" for value and the unit. Value on left side and unit on right side.

# Mensuration
### Sample code
```python
from PyDMath import perimeter

# Create object for the class
obj = perimeter()
print(obj.circle('2-cm'))
```

## Shapes includes
### Perimeter and Area
```Circle``` ```Square``` ```Rectangle``` ```Triangle``` ```Equilateral triangle``` ```Parallelogram``` ```Trapezium``` ```Isosceles triangle``` ```Rhombus```
### Volume
```Sphere``` ```Cylinder``` ```Cube``` ```Rectangular prism``` ```Cone``` ```Hemi sphere``` ```Right rectangular prism``` 
