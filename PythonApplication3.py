
def main():
    try:
          fh = open("d:\employeee.txt")
          for line in fh.readlines():
              print(line)
    except IOError as e:
        print('bad {} is happenf'.format(e))
if __name__=="__main__":main()