#python 2.7

def test_hash_function(func,keys,size):
  result=[0]*size
  keys_used=[]
  for w in keys:
    if w not in keys_used   
      hv=func(w,size)
      result[hv]=result[hv]+1
      keys_used.append(w)
  return result   
