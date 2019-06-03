'''
跑马灯
'''
import os,time

def main():
    os.system('cls')
    content="北京欢迎你————"

    while True:
        print(content)
        time.sleep(0.2)
        content=content[1:]+content[0]

if __name__=="__main__":
    main()