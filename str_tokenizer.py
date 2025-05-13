import re

def stringTokenizer(e):
    # 1st solution
    return re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\/])", e)
    # 2nd solution
    # lst = []
    # for item in expression.split():
    #     if item.startswith("("):
    #         lst.append(item[0])
    #         lst.append(item[1:])
    #     elif item.endswith(")"):
    #         lst.append(item[:-1])
    #         lst.append(item[-1])
    #     else:
    #         lst.append(item)
    # return lst
