
def reshape(pattern):
    return [elem for row in pattern for elem in row]

def replace_zeros(pattern,n):
    for i in range(n):
        if pattern[i] == 0 :
            pattern[i] = -1
    return pattern

def transposed_multiplied(pattern,n):
    multiplied = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            multiplied[i][j] = pattern[i] * pattern[j]
    return multiplied
    
def sum_patterns(pattern1,pattern2,n1,n2):
    if n1 != n2:
        print ("Different sizes!")
        return
    
    for i in range(n1):
        for j in range(n1):
            pattern1[i][j] = pattern1[i][j] + pattern2[i][j]
    return pattern1

def insert_zeros_diagonal(pattern,n):
    i=0
    j=0
    for i in range(n):
        pattern[i][j] = 0
        j = j + 1
    
    return pattern

def act_funct(pattern,n):
    for i in range(n):
        if pattern[i] < 0 :
            pattern[i] = -1
        if pattern[i] > 0:
            pattern[i] = 1
    return pattern
    

def recogn_pattern(pattern, pattern1, n):
    helper = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            helper[i] = helper[i] + (pattern[i][j] * pattern1[j])
    
    helper = act_funct(helper, n)
    print (helper)

    if helper == pattern1:
        print("Terminado! Patron reconocido")
        return

    else: 
        print("Patron NO reconocido, otro intento")
        recogn_pattern(pattern, helper,n)
        


def main():
    doc1 = open("muestras/muestra1.txt", "r")
    pattern1 = [list(map(int, line.rstrip('\n'))) for line in doc1.readlines()]
    print (pattern1)
    pattern1 = reshape(pattern1)
    n1 = len(pattern1)


    doc2 = open("muestras/muestra4.txt", "r")
    pattern2 = [list(map(int, line.rstrip('\n'))) for line in doc2.readlines()]
    print (pattern2)
    pattern2 = reshape(pattern2)
    n2 = len(pattern2)


    pattern1 = replace_zeros(pattern1,n1)
    pattern2 = replace_zeros(pattern2,n2)

    pattern1_processed = transposed_multiplied(pattern1,n1)
    pattern2_processed = transposed_multiplied(pattern2,n2)

    pattern = sum_patterns(pattern1_processed, pattern2_processed,n1,n2)

    pattern = insert_zeros_diagonal(pattern, n1)

    recogn_pattern (pattern, pattern1, n1)
    recogn_pattern (pattern, pattern2, n1)

    doc3 = open("muestras/randomPattern.txt", "r")
    pattern3 = [list(map(int, line.rstrip('\n'))) for line in doc3.readlines()]
    pattern3 = reshape(pattern3)
    
    recogn_pattern (pattern, pattern3, n1)

   

main()










    

