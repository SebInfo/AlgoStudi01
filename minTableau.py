from array import array

# Algo faux prit dans un ouvrage
def minTab(tab):
    minIndex = 0
    longueurTab = len(tab)-1
    for j in range(0,longueurTab):
        if(tab[minIndex]>tab[j]):
            minIndex = j
    return tab[minIndex]

scores = array('i',[4,12,2,8,80,70,1,88])
print (minTab(scores))