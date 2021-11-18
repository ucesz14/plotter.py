from plotter import Plotter
from category import Categorize


def main():
    plotter = Plotter()
    categorize = Categorize()
    print('read polygon.csv')
    
    
    num_p=[]
    x_p=[]
    y_p=[]
    
    with open ('polygon.csv') as f:
        rows= f.readlines()[1:]

  
    for row in rows:
        num_p_t, x_p_t, y_p_t=row.split(',')
        
        num_p.append (float(num_p_t))
        
        x_p.append (float(x_p_t))
        
        y_p.append (float(y_p_t.strip()))
        
    plotter.add_polygon(x_p,y_p)
    
    
    
    print('read input.csv')
    num_pt=[]
    x_pt=[]
    y_pt=[]
    
    with open ('input.csv') as f:
        rows= f.readlines()[1:]

  
    for row in rows:
        num_pt_t, x_pt_t, y_pt_t=row.split(',')
        
        num_pt.append (float(num_pt_t))
        
        x_pt.append (float(x_pt_t))
        
        y_pt.append (float(y_pt_t.strip()))
    
    print(x_pt)

    print('categorize points')
    kinds=[]
    
    for i in range (len(x_pt)):
        kind=(categorize.pip(x_p,y_p,x_pt[i],y_pt[i]))
        plotter.add_point(x_pt[i],y_pt[i],kind)
        kinds.append(kind)
    
    
    
    '''
    
    
    x_min = min(x_p)
    x_max = max(x_p)
    y_min = min(y_p)
    y_max = max(y_p)
    kind=[]
    for i in range(len(x_pt)):
        
        if x_pt[i] >= x_min and x_pt[i] <= x_max and y_pt[i] <= y_max and y_pt[i] >= y_min:
            
            kind.append('Unclassified')
        
        else:
            
            kind.append('outside')
    for i in range (len(x_pt)):    
        
    '''
    
    
    
        



    print('write output.csv')

    print('plot polygon and points')
    plotter.show()


if __name__ == '__main__':
    main()
