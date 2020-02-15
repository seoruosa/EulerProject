
class Routes:
    def __init__(self):
        self.memo = {(0,0):0, (1,0):1, (0,1):1}

    def __call__(self, rows, columns):
        if (rows,columns) not in self.memo:
            if (rows==0 or columns==0):
                self.memo[(rows, columns)] = 1
            else:
                self.memo[(rows,columns)] = self.__call__(rows-1, columns) + self.__call__(rows, columns-1)
        return self.memo[(rows, columns)]

def main():
    routes = Routes()
    for i in range(1,200):
        print(f"{i} - {routes(i, i)}")

if __name__ == '__main__':
    main()