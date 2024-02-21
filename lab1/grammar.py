#Variant 23:
#VN={S, B, C},
#VT={a, b, c}, 
#P={ 
#    S → aB     
#    B → aC    
#    C → bB   
#    C → c 
#   C → aS
#    B → bB
#}

def __init__ (self):
    self.VN = {'S', 'B', 'C'}
    self.VT = {'a', 'b', 'c'}
    self.P = {
        'S': ['aB'],
        'B': ['aC', 'bB'],
        'C': ['bB', 'c', 'aS'],
    }