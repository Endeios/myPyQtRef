'''
Created on 09/ott/2013

@author: bveronesi
'''


def test(greet,times):
    for i in range(0,times):
        print(greet)

def triggered():
    triggered = "imtriggered!!"
    print(triggered)
    
def register(register):
    register["test"].connect(triggered)