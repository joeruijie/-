#利用字符串切片操作，将 "Python" 反转为 "nohtyP"

def str_back(str):
    str_old = list(str)
    for i in range(len(str_old)//2):
        str_now = str_old[i]
        str_old[i] = str_old[-(i+1)]
        str_old[-(i+1)] = str_now
    now_str = ''.join(str_old)
    print(now_str)

    return


if __name__ == '__main__':
    str = 'python'
    # str_back(str)
    print(str[::-1])