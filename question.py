#!/usr/bin/env python3
import json
import time

TOPICS_LIST = ['science', 'history', 'commerce', 'technology', 'worldgk'] 
# this list has to in sync with the JSON filename and the Menu prompt inside test() method

def ask_one_question(question):
    print("\n" + question)
    choice = input("Chọn câu trả lời: [ a | b | c | d ]: ")
    while(True):
        if choice.lower() in ['a', 'b', 'c', 'd']:
            return choice
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại")
            choice = input("Chọn câu trả lời: [ a | b | c | d ]: ")

def score_one_result(key, meta):
    actual = meta["answer"]
    if meta["user_response"].lower() == actual.lower():
        print("Q.{0} Chính Xác!\n".format(key))
        return 1
    else:
        print("Q.{0} Không Chính Xác!".format(key))
        print("Câu trả lời đúng là: ({0})".format(actual))
        print ("Learn more : " + meta["more_info"] + "\n")
        return 0


def test(questions):
    score = 0
    print("Lưu Ý - Hướng Dẫn:\n1. Vui lòng chỉ nhập chữ cái tương ứng với câu trả lời.\n2. Mỗi câu hỏi là 1 điểm.\n3. Trả lời sai sẽ không có điểm cho câu đó.\nCâu đố sẽ bắt đầu trong 10 giây tới... Chúc bạn may mắn!\n")
    time.sleep(10)
    for key, meta in questions.items():
        questions[key]["user_response"] = ask_one_question(meta["question"])
    print("\n***************** Kết Quả - Đáp Án ********************\n")
    for key, meta in questions.items():
        score += score_one_result(key, meta)
    print("Điểm Số Của Bạn:", score, "/", (1 * len(questions)))

def load_question(filename):
    """
    loads the questions from the JSON file into a Python dictionary and returns it
    """
    questions = None
    with open(filename, "r") as read_file:
        questions = json.load(read_file)
    return (questions)


def play_quiz():
    flag = False
    try:
        choice = int(input("Chào mừng bạn đến với Huỳnh Vĩnh Tiến - Quiz!\nHãy chọn chủ đề phù hợp:\n(1). Khoa Học\n(2). Lịch Sử\n(3). Kiến Trúc\n(4). Công Nghệ\n(5). Điện Tử\nHãy nhập số chủ đề: [ 1 | 2 | 3 | 4 | 5 ]: "))
        if choice > len(TOPICS_LIST) or choice < 1:
            print("Invalid Choice. Enter Again")
            flag = True # raising flag
    except ValueError as e:
        print("Invalid Choice. Enter Again")
        flag = True # raising a flag

    if not flag:
        questions = load_question('topics/'+TOPICS_LIST[choice-1]+'.json')
        test(questions)
    else:
        play_quiz() # replay if flag was raised

def user_begin_prompt():
    print("Bạn có muốn chơi thử trò chơi không?\nA. Có\nB. Không!")
    play = input()
    if play.lower() == 'a' or play.lower() ==  'y':
        play_quiz()
    elif play.lower() == 'b':
        print("Hy vọng bạn sẽ quay lại sớm!")
    else:
        print("Nhấn A để bắt đầu | Nhấn B để thoát.")
        user_begin_prompt()
        
def execute():
    user_begin_prompt()

if __name__ == '__main__':
    execute()
