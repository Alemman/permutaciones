#Permutaciones y combinaciones

array2 = []

def function_main():
    n = data_imput()
    array = createArray(n)
    showCombinations(array,0, n)
    printArray(array2, n)    
    print()
    print(f"Combinaciones: {Combinations(n)}")

def printArray(array, n):
    c = 1
    for i in range(len(array)):
        if(i%n == 0):
            print(f"{c}.- ", end="")
            for j in range(i,i+n):
                print(f"{array[j]}",end="")
            c += 1
            print()
        
def data_imput():
    while True:
        print("ingresa la cantidad de objetos----: ")
        n = input()
        try:
            n = int(n)
            return n
        except ValueError:
            print ("Atencion:debe ingresar un numero entero")

def createArray(n):
    array = []
    for i in range(n):
        array.append(i+1)
    return array

def showCombinations(array, c, n):
    if(c<n):
        for i in range(c,n):
            s = array[c]
            array[c] = array[i]
            array[i] = s
            showCombinations(array, c+1,n)
            s = array[c]
            array[c] = array[i]
            array[i] = s
    else:
        for i in range(len(array)):
            #print(array[i],end="")
            array2.append(array[i])
      #  print(", ", end="")

def Combinations(n):
    c = 1
    for i in range(n):
        c *= (i+1)
    return c

print("llamada a funciones")
function_main()
print()
