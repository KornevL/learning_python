from sys import stdin


class MatrixError(BaseException):
    def __init__(self, mat1, mat2):
        self.matrix1 = mat1
        self.matrix2 = mat2


class Matrix:
    def __init__(self, ma):
        mam = []
        for rows in ma:
            mam.append(rows[:])
        self.ma = mam

    def __str__(self):
        row = []
        for rows in self.ma:
            row.append('\t'.join(map(str, rows)))
        return '\n'.join(map(str, row))

    def size(self):
        rows = len(self.ma)
        cols = len(self.ma[-1])
        return (rows, cols)

    def __add__(self, other):
        if len(self.ma) == len(other.ma):
            summatx = []
            for i in range(len(self.ma)):
                row = []
                for j in range(len(self.ma[i])):
                    a = int(self.ma[i][j])
                    b = int(other.ma[i][j])
                    c = a + b
                    row.append(c)
                summatx.append(row)
        else:
            raise MatrixError(self, other)
        return (Matrix(summatx))

    def __mul__(self, chis):
        if isinstance(chis, int) or isinstance(chis, float):
            summatx = []
            for i in range(len(self.ma)):
                row = []
                for j in range(len(self.ma[i])):
                    row.append(self.ma[i][j]*chis)
                summatx.append(row)
        else:
            raise MatrixError(self, other)
        return (Matrix(summatx))

    __rmul__ = __mul__

    def transpose(self):
        summatx = []
        for i in range(len(self.ma[0])):
            summatx.append([])
        for i in range(len(self.ma)):
                for j in range(len(self.ma[i])):
                    summatx[j].append(self.ma[i][j])
        self.ma = summatx
        return Matrix(summatx)

    @staticmethod
    def transposed(x):
        summatx = []
        for i in range(len(x.ma[0])):
            summatx.append([])
        for i in range(len(x.ma)):
                for j in range(len(x.ma[i])):
                    summatx[j].append(x.ma[i][j])
        return Matrix(summatx)

exec(stdin.read())
