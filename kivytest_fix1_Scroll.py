import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
import pickle
import os
Builder.load_string('''
<Label>:
    font_name: 'Modern.ttf' # เปลี่ยน font label เป็น Angsana New ทำให้พิมพ์ภาษาไทยได้
    font_size: 50
<TextInput>:
    font_name: 'Modern.ttf' # เปลี่ยน font Input เป็น Angsana New ทำให้พิมพ์ภาษาไทยได้
    font_size: 50
<ScrollableLabel>:
    Label:
        size_hint_y: None
        height: self.texture_size[1]
        text_size: self.width, None
        text: root.text
        font_size: 40

''')
class PSHITMIDTERMPROJECT(App):
    def build(self):
        return GenB()
class ScrollableLabel(ScrollView):
    text = StringProperty('')
class GenB(GridLayout):
    def __init__(self):
        super().__init__()
        self.cols = 2
        if os.path.isfile("prev_input.txt"): # import ข้อมูลจาก file text ที่ save ไว้
            """with open("prev_input.txt", "r") as p:
                d = p.read().split(":")
                dict2 = {}
                if len(d) > 4: # input ข้อมูลจาก file text เข้ามาใน dict2
                    while d:
                        if len(d) >= 4:
                            list2 = []
                            list2.append(float(d[1]))
                            list2.append(d[2])
                            list2.append(d[3])
                            dict2[d[0]] = list2
                            d.pop(0)
                            d.pop(0)
                            d.pop(0)
                            d.pop(0)
                        elif len(d) < 2:
                            break"""
        with open("test" + '.pkl', 'rb') as f:
            dict2 = pickle.load(f)
        self.dict2 = dict2

        self.name1 = TextInput(text="ใส่ชื่อสินค้า")
        self.add_widget(self.name1)
        self.value1 = TextInput(multiline=False)
        self.add_widget(self.value1)
        self.value2 = TextInput(multiline=False)
        self.add_widget(self.value2)
        self.value3 = TextInput(multiline=False)
        self.add_widget(self.value3)

        self.submit = Button(text="Submit")
        self.submit.bind(on_press=self.calculate)
        self.add_widget(self.submit)

        self.check = Button(text="Check")
        self.check.bind(on_press=self.checkstore)
        self.add_widget(self.check)

        """self.name4 = TextInput(text="Delete Item?")
        self.add_widget(self.name4)

        self.delete = Button(text="Delete")
        self.delete.bind(on_press=self.delete2)
        self.add_widget(self.delete)

        self.name5 = TextInput(text="Delete Value?")
        self.add_widget(self.name5)
        self.value2 = TextInput(multiline=False)
        self.add_widget(self.value2)

        self.delete = Button(text="Delete")
        self.delete.bind(on_press=self.delete3)
        self.add_widget(self.delete)"""
    def delete2(self, value):
        dict2 = self.dict2
        dict2.pop(self.name4.text, None)
    def delete3(self, value):
        dict2 = self.dict2
        dict2   [self.name5.text] = float(self.value2.text)
    def checkstore(self, value):
        """Check จำนวนของที่มีอยู่ใน dict2"""
        dict2 = self.dict2
        test = ""
        count = 0
        """for i in dict2:
            print(i, dict2[i])
            count += 1
            test += str(count) + ". " + str(i) + " "
            for j in dict2[i]:
                test += str(j) + " "
            test += "\n"
        alpha = Popup(title="Inventory", content=ScrollableLabel(text=test), size_hint_y=None, height=500)
        alpha.open()"""
        """layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(30):
            btn = Button(text=str(i), size_hint_y=None, height=40)
            layout.add_widget(btn)
        root = ScrollView()
        root.add_widget(layout)
        alpha = Popup(title="Inventory", content=root, size_hint_y=None, height=500)
        alpha.open()"""
        details = BoxLayout(size_hint_y=None, height=30, pos_hint={'top': 1})

        for i in dict2:
            name = Label(text=i)
            value = Label(text=dict2[i][1])
            fromm = Label(text="test")
            price = Label(text="test")
            details.add_widget(name)
            details.add_widget(value)
            details.add_widget(fromm)
            details.add_widget(price)

        alpha = Popup(title="Inventory", content=details, size_hint_y=None, height=500)
        alpha.open()

    def save_obj(obj, name):
        with open(name + '.pkl', 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

    def load_obj(name):
        with open(name + '.pkl', 'rb') as f:
            return pickle.load(f)

    def calculate(self, value):
        """เก็บข้อมูลเข้าไปไว้ในไฟล์ prev_input.txt"""
        dict1 = self.dict2
        list1 = []
        list1.append(float(self.value1.text))
        list1.append(self.value2.text)
        list1.append(self.value3.text)
        dict1[self.name1.text] = list1
        with open("test" + '.pkl', 'wb') as f:
            pickle.dump(self.dict2, f, pickle.HIGHEST_PROTOCOL)

        print(dict1)
"""class yourname(GridLayout): # Ref.
    def __init__(self):
        super().__init__()
        self.cols = 2
        if os.path.isfile("prev_input.txt"):
            with open("prev_input.txt", "r") as p:
                d = p.read().split(",")
                prev_name = d[0]
                prev_nickname = d[1]
                prev_age = d[2]
        else:
            prev_name = d[0]
            prev_nickname = d[1]
            prev_age = d[2]
        self.add_widget(Label(text="Name: "))
        self.name = TextInput(text=prev_name, multiline=True)
        self.add_widget(self.name)

        self.add_widget(Label(text="Nickname: "))
        self.nickname = TextInput(text=prev_nickname, multiline=True)
        self.add_widget(self.nickname)

        self.add_widget(Label(text="Age: "))
        self.age = TextInput(text=prev_age, multiline=False)
        self.add_widget(self.age)

        self.submit = Button(text="Submit")
        self.submit.bind(on_press=self.submit_button)
        self.add_widget(Label())
        self.add_widget(self.submit)
    def submit_button(self, value):
        name = self.name.text
        nickname = self.nickname.text
        age = self.age.text
        print(f"{name} {nickname} {age}")
        with open("prev_input.txt", "w") as p:
            p.write(f"{name},{nickname},{age}")"""
if __name__ == "__main__":
    PSHITMIDTERMPROJECT().run()
