def check (arr,  brr, n) :   
   mset_arr = set(arr)
   mset_brr = set(brr)
   for item  in mset_arr:
       if arr.count(item) != brr.count(item):
           return 0
   return 1
