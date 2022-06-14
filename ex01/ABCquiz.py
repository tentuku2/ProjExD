import random
import datetime
q_all = 10
q_cut = 2
rimit = 3


def main():
    st = datetime.datetime.now()
    flag = shutudai(0)
    et = datetime.datetime.now()
    if flag == 1:
        print(f"クリアタイムは{(et-st).seconds}秒だ！ナイストライ")
    else:
        print("残念だったなクリア出来なかったようだ！")

def shutudai(count):
    if count<rimit:
        mozi_list = [chr(65+i) for i in range(26)]
        random.shuffle(mozi_list)
        q_list =  mozi_list[:q_all]
        q_list.sort()
        print(f"対象文字\n{q_list}")
        random.shuffle(q_list)
        cut_list = q_list[:q_cut]
        #print(f"欠損文字\n{cut_list}")
        q_list = q_list[q_cut:]
        print(f"表示文字列\n{q_list}")
        flag = kaitou(cut_list,count)
    else:
        flag = 0
    return flag

def kaitou(cut_list,count):
    ans_cut = int(input("欠損文字は何文字?"))
    if ans_cut ==  q_cut:
        print("正解だ！それじゃあ次は具体的にどの文字がないか入力してみたまえ！")
        ans_lis  = list(input("消えている文字をスペースで区切って大文字で全部入力しろ\n＞＞＞").split())
        if set(ans_lis) == set(cut_list):
            print("正解だ！おめでとう")
            return 1

        else:
            print(f"間違っているぞ！後{rimit-count-1}回だ！最初からやり直せ！")
            shutudai(count+1)
    else:
        print(f"間違っているぞ！あと後{rimit-count-1}回だ！最初からやり直せ！")
        shutudai(count+1)
    



if __name__ == "__main__":
    main()