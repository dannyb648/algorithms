def rookSees(pos,size):
    #Return a list of all squares "In view" of a queen in position pos on a board of size
    inView=[]
        #Row and column
    for i in range(size):
        #Row
        setAppend(inView,(pos[0],i))
        #Column
        setAppend(inView,(i,pos[1]))
    #Take out position of rook so he doesn't see himself...
    inView.remove(pos)
    return inView
