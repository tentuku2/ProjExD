import random
def shutudai(qnum):
    list_quiz = ["サザエの旦那の名前は？","カツオの妹の名前は？ ","タラオはカツオから見てどんな関係？"]
    print("問題:" + list_quiz[qnum])
    
def kaito(qnum):
    anser = input("わかるよね？＞＞")
    ans_list = [["マスオ","ますお","ますおさん","アナゴ課長"],["ワカメ","わかめ"],["甥","おい","甥っ子","不倫相手"]]
    if anser in ans_list[qnum]:
        print("正解！君はサザエさんマスターだ！")
    else:
        print("不正解！君はちびまる子ちゃん派の用だね！")

if __name__ == "__main__":
    qnum = random.randint(0,2)
    shutudai(qnum)
    kaito(qnum)