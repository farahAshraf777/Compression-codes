def calc_frequency(data):
    index = 0
    unique_data = []
    frequency = {}
    while index < len(data):
        if data[index] == '\n':
            break
        if data[index] not in unique_data:
            unique_data.append(data[index])
        index += 1

    for x in unique_data:
        index = 0
        counter = 0
        while index < len(data):
            if x == data[index]:
                counter += 1
            index += 1
        frequency[x] = counter
    return frequency


class Node:
    def __init__(self, ch, freq, left=None, right=None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def Tree(text):
    frequency = calc_frequency(text)
    frequency_list = [Node(ch, frequency[ch]) for ch in frequency]
    frequency_list.sort()
    while len(frequency_list) > 1:
        left = frequency_list[0]
        frequency_list.remove(left)
        right = frequency_list[0]
        frequency_list.remove(right)
        parent = Node(None, left.freq + right.freq, left, right)
        frequency_list.append(parent)
        frequency_list.sort()
    last_element = frequency_list[0]
    frequency_list.remove(last_element)
    return last_element


def Huffman_code(root):
    def dfs(root, code, encoding_dic):
        if root.ch:
            encoding_dic[root.ch] = ''.join(code)
        else:
            code.append('0')
            dfs(root.left, code, encoding_dic)
            code.pop()
            code.append('1')
            dfs(root.right, code, encoding_dic)
            code.pop()

    encoding_dic = {}
    dfs(root, [], encoding_dic)
    return encoding_dic

def encode(text):
    root = Tree(text)
    encoding_dic = Huffman_code(root)

    with open("huffman_table.txt", "w") as Huffman_table:
        for key, value in encoding_dic.items():
            Huffman_table.write('%s %s\n' % (value, key))
    Huffman_table.close()

    with open("output_encode.txt", "w") as Write_file:
        for x in text:
            Write_file.write(encoding_dic[x])

    Write_file.close()


