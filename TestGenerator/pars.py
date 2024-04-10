from tree_sitter import Language, Parser
import json
from copy import deepcopy
import random
import sys
sys.setrecursionlimit(100000000)  # new_limit是你想设定的新限制

dict = {}
count = 0

import time

# 记录开始时间
start_time = time.time()

def ast_to_codeori(node, fa):
    global dict
    global count
    # 如果节点是叶子节点，返回它的文本内容
    if node.child_count == 0:
        text = source_code[node.start_byte:node.end_byte].decode('utf8')
        return text #source_code[node.start_byte:node.end_byte].decode('utf8')
    f = f"{node.type}"
#    else:
        # 否则，递归处理所有子节点，并将结果拼接起来
    
    return ' '.join(ast_to_codeori(child, f) for child in node.children)

def ast_to_code(node, fa):
    global dict
    global count
    # 如果节点是叶子节点，返回它的文本内容
    if fa in ["if_statement"]:
        if node.type == "condition":
            text = ["( true )", '( false )'][random.randint(0, 1)]
            return text
    if node.child_count == 0:
        text = source_code[node.start_byte:node.end_byte].decode('utf8')
        if fa in ["if_statement"]:
            if node.type == "condition":
                text = ["true", 'false'][random.randint(0, 1)]
#                if text in dict:
#                    text = dict[text]
#                else:
#                    if count >= 1:
#                        return text 
#                if text not in dict:
#                    dict[text] = f"<extra_id_{len(dict)}>" #f"<mask>_{len(dict)}"
#                    text = dict[text]
#                    count += 1
#                print(f"['{node.type}', '{text}']")
#        else:
#            if node.type == "identifier":
#                if text in dict:
#                    text = dict[text]
        return text #source_code[node.start_byte:node.end_byte].decode('utf8')
    f = f"{node.type}"
#    else:
        # 否则，递归处理所有子节点，并将结果拼接起来
    
    return ' '.join(ast_to_code(child, f) for child in node.children)

def print_tree(node, level=0):
    # 缩进，更好地显示层级结构
    indent = "  " * level
    # 获取节点的文本内容（如果是叶子节点）
    if str(node.type) == "ERROR":
        raise Exception
    if node.child_count == 0:
        text = source_code[node.start_byte:node.end_byte].decode('utf8')
#        print(f"{indent}{node.type}: '{text}'")
#    else:
#        print(f"{indent}{node.type}")
    # 递归遍历子节点
    for n in node.children:
        print_tree(n, level + 1)


# 加载C++语言的grammar（这需要事先构建好）
Language.build_library(
  # 存放构建的库的路径
  'build/my-languages.so',
  # 语言的grammar的源码路径
  ['tree-sitter-java']
)

# 加载C++语言
CPP_LANGUAGE = Language('build/my-languages.so', 'java')

# 创建一个新的Parser对象
parser = Parser()
parser.set_language(CPP_LANGUAGE)

# 解析C++代码
fff = open("./test.txt") 
lines = fff.readlines()
fff.close()
from tqdm import tqdm
ans = open("./en_tk.txt", "w")
#outlist = []
for line in tqdm(lines):
    outlist = []
    target = json.loads(line)['target']
    if int(target) == 1:
        continue
    source_code = json.loads(line)['func'].encode("utf8")
#    print (source_code)
#    source_code = b'''int main1 (int *a) {if (a > 0) return a; }'''
    tree = parser.parse(source_code)
#    print_tree (tree.root_node)   
#    exit()
    used = []
    # 获取根节点并遍历
    dict = {}
    count = 0
    root_node = tree.root_node
    try:
        print_tree(root_node)
    except:
        continue
#    out = json.dumps([ast_to_code(root_node, ""), dict])
    for i in range(30):
        ele = [ast_to_codeori(root_node, ""), ast_to_code(root_node, ""), deepcopy(dict)]
#        print (ele[0])
#        print (ele[1])
#        print ("-----------------")
        if ele[0] != ele[1] and ele[1] not in used:
            used.append(ele[1])
            outlist.append(ele)#[target, ast_to_code(root_node, ""), deepcopy(dict)])

#    ans.write(out + "\n")
#    exit()
#    print (out)
    outlist = outlist
    for k in outlist:
    #    code = k[0]
    #    dict = k[1]
    #    dic = {}
    #    for i in dict:
    #        dic[dict[i]] = i
    #    for i in range(len(dict)):
    #        index = f"<extra_id_{i}>"
    #        ori = code
    #        codenew = code
    #        for key in dic:
    #            ori = ori.replace(key, dic[key])
    #            if key != index:
    #                codenew = codenew.replace(key, dic[key])
    #            else:
    #                codenew = codenew.replace(key, f"<extra_id_0>")
        ans.write(json.dumps(k) + "\n")

ans.close()


end_time = time.time()

# 计算并打印总运行时间
print(f"程序运行时间: {end_time - start_time} 秒")

