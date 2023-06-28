import tkinter as tk
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# input_string = "How old is the actor in Mace Windu who played Star Wars"
def delay(x):
    time.sleep(x)

def Find(name):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.wikipedia.org/")
    delay(2)
    driver.find_element("id", "searchInput").send_keys(f"{name}")#in dev input box in input type
    delay(2)
    submit_button = driver.find_element(By.XPATH, "//body//div[3]//button[@type='submit']")
    submit_button.click()
    delay(2)
    table_row = driver.find_element(By.XPATH,"//body//div[2]//div[1]//div[3]//main[1]/div[3]//div[3]//div[1]//table//tr[6]")  # Replace with the appropriate XPath to locate the table row
    link = table_row.find_element(By.XPATH,"./td//a")  # Replace with the appropriate XPath to locate the desired link within the table row
    link.click()
    delay(20)


root=tk.Tk() # use to create new chat nav
root.geometry('400x380+30+400')#  30 , 400 showing where the box appear in screen


import spacy
#python -m spacy download en_core_web_sm
def extract_name(input_string):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(input_string)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None


def getresult(message):
    arr=str(message)
    name = extract_name(arr)
    textarea.insert("end", "\nBot : Processing.... ")
    Find(name)
    # else:
    #     textarea.insert("end", "Invalid Input")
    # destroy_window()


def botReply():
    question=query.get()
    textarea.insert("end","\nYou : "+question)
    query.delete(0, "end")
    getresult(question)

def destroy_window():
    root.destroy()

root.title("Chat Bot for new prompt")
root.config(bg="Indigo")
# Headear Logo
head=tk.PhotoImage(file='head1.png')

Insert_head=tk.Label(root,image=head)
Insert_head.config(bg='Indigo')
Insert_head.pack()

#Frame[Conatiner for message]
Centeral_frame=tk.Frame(root)
Centeral_frame.pack()
scrol=tk.Scrollbar(Centeral_frame)
scrol.pack(side='right')

#Text area
textarea=tk.Text(Centeral_frame,font=('time new roman',10,'bold'),height=10,yscrollcommand=scrol.set)
textarea.pack(side='left')
scrol.config(command=textarea.yview)

#Enter message
query=tk.Entry(root,font=('verdana',10,'bold'),width=30)
query.pack(pady=15)

#Button
btn = tk.Button(root, text = 'Send !', bd = '5',command = botReply)
btn.pack()
root.mainloop() # use to hold our
# root.destroy()
