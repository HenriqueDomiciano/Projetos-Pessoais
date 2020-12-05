import numpy as np

global grid
grid=np.array([[1,3,4,0,0,0,0,0,0],[6,2,0,0,0,5,0,0,0],[0,0,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,9,0],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]])

def value():
    def is_possible(ent,y,x):
        for i in range(9): 
            if grid[y,i] == ent :
                return False 
        for j in range(9): 
            if grid[j,x]==ent:
                return False
        x0=(x//3)*3
        y0=(y//3)*3
        for k in range(3):
            for u in range(3): 
                if grid[y0+k,x0+u]==ent:
                    return False
        
        return True

    def solver(): 
        for i in range (9):
            for j in range (9):
                if grid[i,j]==0:
                    for n in range(1,10):
                        if is_possible(n,i,j):
                            grid[i,j]=n
                            solver()
                            grid[i,j]=0
                    return
            break
        return
    return grid
print(value())