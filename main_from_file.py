from plotter import Plotter
from category import Categorize


def main():
    plotter = Plotter()
    categorize = Categorize()
    
    print('read polygon.csv')
    
    (x_p,y_p,num_p)= categorize.csv_r('polygon.csv')
        
    
    plotter.add_polygon(x_p,y_p)
    
    print('Finished')
    
    print('read input.csv')

    (x_pt,y_pt,num_pt)= categorize.csv_r('input.csv')

    print('Finished')

    print('categorize points')
    kinds=[]
    
    for i in range (len(x_pt)):
        kind=(categorize.pip(x_p,y_p,x_pt[i],y_pt[i]))
        plotter.add_point(x_pt[i],y_pt[i],kind)
        kinds.append(kind)
    
    
    print('Finished')
    
    print('write output.csv')
    
    with open ('output.csv','w') as f:
        
        #write the information line which is not icluded in data
        f.write('id,category\n')
        
        for i in range(len(x_pt)):
            output=str(i+1)+','+kinds[i]+'\n'
            f.write(output)
    
    print('Finished')
    
    print('plot polygon and points')
    plotter.show()
    
    print('Finished')


if __name__ == '__main__':
    main()
