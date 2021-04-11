import numpy as np

labirent = 'WPPWWW\nWWPWPS\nWWPWPW\nPPPPPW\nFWPWWW\nWPPPPW'


def write_file(isim,labirent):
    
    f = open(isim,"w+")
    
    f.write(labirent)
    
    f.close()
   
    
    
    
def read_file(isim):
    
    liste = []
    
    
    f=open(isim, "r")
    if f.mode == 'r':
        liste = f.read()
        liste2 = liste.split('\n')
        return liste2
    
write_file('girdi.txt',labirent)
metin = read_file('girdi.txt') 
print(metin)



print("------------------------------")




def string2matris(labirent):
    
    matrix = []
    
    for row in labirent:
        #print('row:',row)
        matrix.append([])
        #print('matrix1: ',matrix)
        for col in row:
            #print('col:',col)
            #print('matrix2:',matrix)
            matrix[-1].append(col)
            #print('matrix3:',matrix)
    return matrix


labirent_matris = string2matris(metin)
print("mm",labirent_matris)



print("------------------------------")



def start_bul(labirent_matris):
    
    k_sat = 0
    k_sut = 0
    for sat in labirent_matris:
        k_sat+=1
        #print('sat:',k_sat)
        k_sut = 0
        for sut in sat:
            
            k_sut += 1
            #print('sut',k_sut)
            
            if sut == "S":
                return (k_sat-1,k_sut-1)
                
            
    
start_poz = start_bul(labirent_matris)
print(start_poz)


print("---------------------------------")


sayma = 0
yList = []


def YolBul(labirent_matris,start_poz):
    
    global sayma,yList
    
    
    sat,sut = start_poz
    print('Pozisyon: {},{}'.format(sat,sut))
    
    max_sat = len(labirent_matris)
    max_sut = len(labirent_matris[0])
    
    sayma += 1
    yList.append((sat,sut))
    print('Yeni Liste: ',yList)
    
    if labirent_matris[sat][sut] == "F":
        return True
    
    else:
        if sut+1 < max_sut and labirent_matris[sat][sut+1] != "W" and (sat,sut+1) not in yList:
            YolBul(labirent_matris,(sat,sut+1))
            
        elif sut-1 >= 0 and labirent_matris[sat][sut-1] != 'W' and (sat,sut-1) not in yList:
            YolBul(labirent_matris,(sat,sut-1))
        
        elif sat-1 >= 0 and labirent_matris[sat-1][sut] != 'W' and (sat-1,sut) not in yList:
            YolBul(labirent_matris,(sat-1,sut))
        
        elif sat+1 < max_sat and labirent_matris[sat+1][sut] != 'W' and (sat+1,sut) not in yList:
            YolBul(labirent_matris,(sat+1,sut))
        
        else:
            print('{},{}'.format(sat,sut))
        
    
        
    
YolBul(labirent_matris,start_poz)

print("Yeni Liste: " , yList)            
            
print("--------------------------------")           


labirent2 = '000000\n000000\n000000\n000000\n000000\n000000'
liste3 = labirent2.split("\n")

def string3matris(labirent):
    
    matrix = yList
    
    for row in labirent:
        #print('row:',row)
        matrix.append([])
        #print('matrix1: ',matrix)
        for col in row:
            #print('col:',col)
            #print('matrix2:',matrix)
            matrix[-1].append(col)
            #print('matrix3:',matrix)
            
                 
               
             
    return matrix

labmat2= string2matris(liste3)
labmat2

def ListeDonustur(labmat2,yList):
    
    
    
    for x,y in yList:
        
        if yList[0] == (x,y):
            labmat2[x][y] = "S"
        elif yList[len(yList)-1] == (x,y):
            labmat2[x][y] = "F"
        else:
            labmat2[x][y] = str(1)
            

ListeDonustur(labmat2,yList)
labmat2      


def soncıktı(isim):
    
   f = open(isim,"w+")
    
   i = 0
   for satır in labmat2:
      
       for sutun in satır:
            
            #deger = " {} ".format(sutun)
            if len(satır) == i:
                f.write("\n")
                i = 0
            if len(satır) != i and 0 != i:
                f.write(", ")
                
            f.write(sutun)
            #f.write(" , ")
            i+=1
            
            
            
   f.close()
        
soncıktı("cikti.txt")    
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

            
        
 






































    



            
        
