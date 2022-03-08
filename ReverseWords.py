def ReserveWords(input):
    InputWords = input.split(" ")
    # 通过空格将字符串分隔开来
    InputWords = InputWords[-1::-1]
    output = ' '.join(InputWords)
    return output

if __name__ == "__main__":
    input = 'Hello My Friend'
    res = ReserveWords(input)
    print(res)