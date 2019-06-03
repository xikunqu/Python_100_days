'''
返回给定文件名的后缀名
'''

def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    houzhui=filename.split(".")[-1]
    if has_dot:
        return "."+houzhui
    else:
        return houzhui
