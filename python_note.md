- a few techniques in python
  - use +=, not a = a+1 
  - In dictionary(Hash map), note the difference between get and   
    dict[key] to access value.
    dict.get(key,0) returns 0 if key is not in dictionary.
    So use dict.get(key,0).
  - if key in dict is faster than if key in dict.keys(). It seems like  
    the default search is based on key in dictionary.
    
