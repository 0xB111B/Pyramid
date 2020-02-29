# Pyramid

**pyramid.py** is a python implementation of "Pyramid word".  
  
Request is: http://127.0.0.1:5000/api/v1/ispyramidword?string=  
  
For example:  
* request is: http://127.0.0.1:5000/api/v1/ispyramidword?string=banana  

* request is: http://127.0.0.1:5000/api/v1/ispyramidword?string=bandana  

* request is: http://127.0.0.1:5000/api/v1/ispyramidword?string=b1a1n1d1a1n1a 

Reponse is either: 
**True**  - if string parameter contains a "Pyramid" word  
or  
**False** - if string parameter is not a "Pyramid" word,  
or contains not only [A-Za-z]  characters  
        or an empty string.  
  
To run the web service, install flask:  
`pip install flask`  


**pyramid.cpp** - is a standalone C++ implementation. 

**Description of the algorithm:**
- check the edge case (i.e. 0-length)
- store the total count of each letter in the array
- check the array for the presence of the arithmetic progression with d = 1.
