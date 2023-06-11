import tkinter as tk
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Find me a house in houston that works for 4. My budget is 600k
def delay(x):
    time.sleep(x)

def Find_A_House(Location,range):
    l = len(range)
    if(range[l-1]=='k' or range[l-1]=='K'):
        range=range[:l - 1] + "000"

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.redfin.com/")
    delay(2)
    driver.find_element("id", "search-box-input").send_keys(f"{Location}")#in dev input box in input type
    delay(2)
    driver.find_element('css selector', "#tabContentId0 > div > div > form > div > button").click()
    delay(2)
    driver.find_element('css selector',"#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div:nth-child(2) > div").click()
    # Price
    delay(4)
    driver.find_element("css selector","#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div:nth-child(2) > div > div.Flyout.standard.v83.position-right.alignment-below.CustomFilter__flyout.transparent.standard > div.flyout > div > div.CustomFilter__container > div > div > div.flex.align-center.inputRangeAfterHistogram > span:nth-child(3) > span > div > input").send_keys(f"{range}")
    delay(2)
    driver.find_element('css selector',"#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div:nth-child(2) > div > div.Flyout.standard.v83.position-right.alignment-below.CustomFilter__flyout.transparent.standard > div.flyout > div > div.CustomFilter__footer.flex.align-center > div > button.button.Button.primary").click()
    delay(2)
    # SELECT hometype
    driver.find_element('css selector',"#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div.CustomFilter.inline-block.desktopExposedSearchFilter.default.desktopExposedPropertyTypeFilter.showDesktopFilterMenuRedesign").click()
    delay(2)
    driver.find_element('css selector',"#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div.CustomFilter.inline-block.desktopExposedSearchFilter.desktopExposedPropertyTypeFilter.showDesktopFilterMenuRedesign > div.Flyout.standard.v83.position-left.alignment-below.CustomFilter__flyout.transparent.standard > div.flyout > div > div.CustomFilter__container > div > div > div > div > div > div > div:nth-child(1)").click()
    # SELECT HOUSE

    delay(2)
    driver.find_element('xpath',"/html/body/div[1]/div[9]/div[2]/div[2]/div[2]/div/div/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/button[2]/span").click()

    delay(2)
    driver.find_element('css selector',"#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div.CustomFilter.inline-block.desktopExposedSearchFilter.desktopExposedBedsAndBathsContainer.showDesktopFilterMenuRedesign").click()
    # HOUSE DONE
    delay(2)
    driver.find_element('xpath',"/html/body/div[1]/div[9]/div[2]/div[2]/div[2]/div/div/div[1]/form/div[4]/div[2]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div[6]").click()
    delay(2)
    driver.find_element('css selector',"#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div.CustomFilter.inline-block.desktopExposedSearchFilter.desktopExposedBedsAndBathsContainer.showDesktopFilterMenuRedesign > div.Flyout.standard.v83.position-left.alignment-below.CustomFilter__flyout.transparent.standard > div.flyout > div > div.CustomFilter__footer.flex.align-center > div > button.button.Button.primary").click()
    delay(2)
    parent_div = driver.find_element(By.ID, "MapHomeCard_0")
    link =parent_div.find_element(By.TAG_NAME, "a")
    link.click()
    delay(30)

root=tk.Tk() # use to create new chat nav
root.geometry('400x380+30+400')#  30 , 400 showing where the box appear in screen
def getresult(message):
    arr=message.split(" ")
    if arr[0]=="Find":
        textarea.insert("end", "\nBot : Processing.... ")
        Location=arr[5]
        range=arr[-1]
        Find_A_House(Location,range)
        textarea.insert("end", "\nBot : Wanna re-search for house? YES/NO")
        question = query.get()
        textarea.insert("end", "\nYou : " + question)
        arr= question.split(" ")
        if(arr[0] in ['Yes', 'yes', 'YES', 'y', 'Y']):
            textarea.insert("end", "\nBot : Please enter the search")
        else:
            destroy_window()
    else:
        textarea.insert("end", "Invalid Input")
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