

class Categorize:
    
    def pip(self, xs, ys, x, y):

        x_min = min(xs)
        x_max = max(xs)
        y_min = min(ys)
        y_max = max(ys)
        kind=[]
        is_in = False
        if x >= x_min and x <= x_max and y <= y_max and y >= y_min:
            
            for i in range(len(xs)):
                if i==0:
                    j = len(xs)-1
                else:
                     j=i-1
                     
                if ys[i] == ys[j]:
                    if ys[i] == y and abs(xs[i]-x)+abs(xs[j]-x) == abs(xs[i]-xs[j]):
                        kind = 'boundary'
                        break
                else:
                    if ((ys[i] > y) != (ys[j] > y)) and (x == (xs[j] - xs[i]) * (y - ys[i]) / (ys[j] - ys[i]) + xs[i]):
                        kind = 'boundary'
                        break
                        
                    else:
                        if ((ys[i] > y) != (ys[j] > y)) and (x < (xs[j] - xs[i]) * (y - ys[i]) / (ys[j] - ys[i]) + xs[i]):
                            is_in = not is_in
                            
                if is_in == True:
                    kind = 'inside'
                else:
                    kind = 'outside'
                        
        
        else:
            
            kind = 'outside'  
        
        return(kind)
    
    
    



    



