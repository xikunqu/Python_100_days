import time
def main():
    try:
        #一次性读取整个文件内容
        with open('a.txt','r',encoding='utf-8') as f:
            print(f.read())

        #通过for-in循环逐行读取
        with open('a.txt','r',encoding='utf-8') as f:
            for line in f:
                print(line,end='')
                time.sleep(0.5)
        print()

        #读取文件按行读取到列表中
        with open('a.txt','r',encoding='utf-8') as f:
            lines=f.readlines()
        print(lines)

    except FileNotFoundError:
        print('无法打开指定的文件！')
    except LookupError:
        print("指定了未知的编码")
    except UnicodeDecodeError:
        print('读取文件时解码错误！')


if __name__=='__main__':
    main()