from flask import Flask, request, jsonify

app = Flask(__name__)

class PrefixTree:
    #TODO реализация класса prefix tree, методы как на лекции + метод дать топ 10 продолжений. Скажем на строку кросс выдаем кроссовки, кроссовочки итп. Как хранить топ? 
    #Решать вам. Можно, конечно, обходить все ноды, но это долго. Дешевле чуток проиграть по памяти, зато отдавать быстро (скажем можно взять кучу)
    #В терминальных (конечных) нодах может лежать json с топ актерами.
    def __init__(self):
        self.root = [{}]
        
    def add(self, string):
        if self.check(string):
            return
        wrk_dict = self.root
        for i in string:
            if i in wrk_dict[0]:
                wrk_dict = wrk_dict[0][i]
            else:
                wrk_dict[0][i] = [{}]
                wrk_dict = wrk_dict[0][i]
        wrk_dict.append(True)
        #TODO добавить строку
        
    def check(self, string):
        wrk_dict = self.root
        for i in string:
            if i in wrk_dict[0]:
                wrk_dict = wrk_dict[0][i]
            else:
                return False
        if len(wrk_dict) != 1:
            return True
        return False
        #TODO проверить наличие строки
    
    def check_part(self, string):
        wrk_dict = self.root
        for i in string:
            if i in wrk_dict[0]:
                wrk_dict = wrk_dict[0][i]
            else:
                return False
        return True
        #TODO проверить наличие строки как префикса

def init_prefix_tree(filename):
    #TODO в данном методе загружаем данные из файла. Предположим вормат файла "Строка, чтобы положить в дерево" \t "json значение для ноды" \t частота встречаемости


@app.route("/get_sudgest/<string>", methods=['GET', 'POST'])
def return_sudgest(string):
    #TODO по запросу string вернуть json, c топ-10 саджестами, и значениями из нод

@app.route("/")
def hello():
    #TODO должна возвращатьс инструкция по работе с сервером
    return

if __name__ == "__main__":
    app.run()
