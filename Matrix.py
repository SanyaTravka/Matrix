def Author():
    print("The module is created by Travnikov Alexandr, student of school 218, 2021 year.")
def Help():
    print("Author - the author module")
    print("PrintMatr - printing Matrix, input parameter: matrix")
    print("Zeros - matrix of zeros(memory alocation), input parameters: rows, cols")
    print("PlusMatr and MinusMatr - matrix addition and matrix substraction, input parameters: matrix1, matrix2")
    print("Transpos - transposing the matrix, input parameter: matrix")
    print("MatrixMultyNumber, input parameters: matrix, number")
    print("Multipy - matrix Multiplication, input parameter: matrix1, matrix2")
    print("Determiner - determiner of matrix, input parameter: matrix")
    print("Kramer - solving systems of linear equations by the Kramer method, input parameters: matrix, vector")
    print("InverseMatrix - finding the inverse matrix, input parameter: matrix")
def Zeros(row,col):
    rez = []
    for i in range(row):
        st = []
        for j in range(col):
            st.append(0)
        rez.append(st)
    return rez
def Ones(row,col):
    rez = []
    for i in range(row):
        st = []
        for j in range(col):
            st.append(1)
        rez.append(st)
    return rez    

def PrintMatr(matr):
    if len(matr) == 0:
        return
    for i in range(len(matr)):
        print(matr[i])

def MatrixMultyNumber(matr,num):
    endMatr = Zeros(len(matr),len(matr[0]))
    for i in range(len(matr)):
        for j in range(len(matr[0])):
            endMatr[i][j] = matr[i][j] * num
    return endMatr

def PlusMatr(matr1,matr2):
    row1,col1 = len(matr1),len(matr1[0])
    row2,col2 = len(matr2),len(matr2[0])
    if (row1 != row2) or (col1 != col2):
        print("Matrixes have diffetent sizes!!!")
        return []
    endMatr = Zeros(row1,col1)
    for i in range(row1):
        for j in range(col1):
            endMatr[i][j] = matr1[i][j] + matr2[i][j]
    return endMatr

def MinusMatr(matr1,matr2):
    row1,col1 = len(matr1),len(matr1[0])
    row2,col2 = len(matr2),len(matr2[0])
    if (row1 != row2) or (col1 != col2):
        print("Matrixes have diffetent sizes!!!")
        return []
    endMatr = Zeros(row1,col1)
    for i in range(row1):
        for j in range(col1):
            endMatr[i][j] = matr1[i][j] - matr2[i][j]
    return endMatr

def Transpos(matr):
    rows = len(matr)
    cols = len(matr[0])
    if rows==0:
        print("The rows number can't be 0 !!!")
        return []
    if cols==0:
        print("The cols number can't be 0 !!!")
        return []        
    endMatr = Zeros(cols,rows)
    for i in range(rows):
        for j in range(cols):
            endMatr[j][i] = matr[i][j]
    return endMatr

def Multipy(matr1,matr2):
    
    def GetRezInOneStr(vec1,vec2):
        summ = 0
        for i in range(len(vec1)):
            summ = summ + vec1[i] * vec2[i]
        return summ
    
    def GetStrFromMatr(matr, numStr, kStolb):
        vec = []
        for i in range(kStolb):
            vec.append(matr[numStr][i])
        return vec
    
    def GetStolbFromMatr(matr, numStolb, kStr):
        vec = []
        for i in range(kStr):
            vec.append(matr[i][numStolb])
        return vec        
    
    row1,col1 = len(matr1),len(matr1[0])
    row2,col2 = len(matr2),len(matr2[0])
    if col1 != row2:
        print("The number of columns(Matrix1) != the number of rows(Matrix2)")
        return []
    if row1 != col2:
        print("row1 != col2 !!!")
        return []
    rez = Zeros(row1,col2)
    for i in range(row1):
        vec1 = GetStrFromMatr(matr1, i, col1)
        for j in range(col2):
            vec2 = GetStolbFromMatr(matr2,j,row2)
            rez[i][j] = GetRezInOneStr(vec1,vec2)
    return rez
def DeleteCol(matr, numCol):
    stro = len(matr)
    col = len(matr[0])
    rez = Zeros(stro,col-1)
    for i in range(stro):
        l = 0
        for j in range(col):
            if j != numCol:
                rez[i][l] = matr[i][j]
                l += 1
    return rez 

def DeleteRow(matr, numRow):
    stro = len(matr)
    col = len(matr[0])
    rez = Zeros(stro-1,col)
    for j in range(col):
        l = 0
        for i in range(stro):
            if i != numRow:
                rez[l][j] = matr[i][j]
                l += 1
    return rez 

def PlusOrMinusMatr(matr):
    def IsEven(num):
        if (num % 2 == 0):
            return True
        return False
    
    n = len(matr)
    matrZn = Zeros(n,n)    
    for i in range(n):
        for j in range(n):
            if IsEven(i):
                if IsEven(j):
                    matrZn[i][j] = 1
                else:
                    matrZn[i][j] = -1
            else:
                if IsEven(j):
                    matrZn[i][j] = -1
                else:
                    matrZn[i][j] = 1 
    return matrZn

def Determiner(matr):
    matrZn = PlusOrMinusMatr(matr)
    str1 = []
    n = len(matr)
    if n == 1:
        return matr[0][0]
    
    for i in range(n):
        str1.append(matr[0][i])

    matr1 = Zeros(n-1,n)

    ORez = 0
    for i in range (1,n):
        for j in range (n):
            matr1[i-1][j] = matr[i][j]
            
    for i in range (n):
        for j in range (n):
            matrRez = DeleteCol(matr1,j)
            opr = Determiner(matrRez)
            ORez = ORez + matrZn[i][j] * str1[j] * opr
            if j == n-1:
                return ORez


def Kramer(matr, vec):
    def ChangeK(matr, vec, zn, col):
        rez = []
        for i in range(zn):
            st = []
            for j in range(zn):
                st.append(0)
            rez.append(st)
        for i in range(zn):
            for j in range(zn):
               rez[i][j] = matr[i][j]
        for i in range(zn):
            rez[i][col] = vec[i]
        return rez      
    
    zn = len(vec)
    oprM = Determiner(matr)
    err = "Determiner = 0, two or more rows or columns of the matrix are linearly dependent"
    if oprM == 0:
        return err
    opr = []
    x = []
    for i in range(zn):
        opr.append(0)
        x.append(0)
    for i in range(zn):
        matrI = ChangeK(matr,vec,zn,i)
        opr[i] = Determiner(matrI)
        x[i] = round(opr[i] / oprM,2)
        print("x[i] = ",x[i])
    return "OK"


def DeleteColRow(matr,delRow,delCol):
    if matr == []:
        return matr
    rez = DeleteCol(matr,delCol)
    rez = DeleteRow(rez,delRow)
    return rez

def InverseMatrix(matr):
    row,col = len(matr),len(matr[0])
    if row != col:
        print("Error! Number of rows is not equal to number of collumns!")
        return []
    determ = Determiner(matr)
    if determ == 0:
        print("Determiner = 0, two or more rows or columns of the matrix are linearly dependent")
        return []  
    tempMatr = Zeros(row-1,col-1)
    minorMatr = Zeros(row,col)
    for i in range(row):
        for j in range(col):
            tempMatr = DeleteColRow(matr,i,j)
            minorMatr[i][j] = Determiner(tempMatr)
    matrZn = PlusOrMinusMatr(minorMatr)
    for i in range(row):
        for j in range(col):
            minorMatr[i][j] = minorMatr[i][j] * matrZn[i][j]
    minorMatr = Transpos(minorMatr)
    minorMatr = MatrixMultyNumber(minorMatr,1/determ)
    return minorMatr
    
            
    
    
    

    



