import tkinter as tk
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
# Add Max Nye at Workplete as the new lead
def delay(x):
    time.sleep(x)

def create_lead_salesforce():
    # Get Web Chrome driver
    driver = webdriver.Chrome()

    # Maximize Driver Window
    driver.maximize_window()

    # Open our targeted webpage on driver
    driver.get("https://www.salesforce.com/in/")
    delay(2)

    # Shadow element Travesing
    shadow_root0=driver.find_element('css selector',"hgf-c360nav[locale='in']").shadow_root
    shadow_root0.find_element('css selector', ".utility-icons-items.login").click()
    delay(1)
    shadow_root1=shadow_root0.find_element('css selector',"hgf-c360login[aria-haspopup='true']").shadow_root
    delay(2)

    # Get login Page
    shadow_root1.find_element('css selector',"hgf-popover:nth-child(2)>div:nth-child(2)>div:nth-child(2)>a:nth-child(2)>h4:nth-child(1)").click()
    delay(5)

    # Enter username in Login Page
    driver.find_element('xpath'," //input[@id='password']").send_keys('Saurabh@123')
    delay(2)

    #Enter Password in Login Page
    driver.find_element('xpath', "//input[@id='username']").send_keys('radkesaurabh1999-lem3@force.com')
    delay(2)

    # Try to Login
    driver.find_element('xpath',"//input[@id='Login']").click()
    delay(10)
    # After Succesfull Login go to Leads Section
    driver.find_element('xpath', "//span[@aria-description='Show more My Leads records']").click()
    delay(4)
    driver.find_element('xpath', "//div[@title='New']").click()
    # ADD getails to create Leads
    wait = WebDriverWait(driver,15)
    wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/div/records-lwc-record-layout/forcegenerated-detailpanel_lead___012000000000000aaa___full___create___recordlayout2/records-record-layout-block/slot/records-record-layout-section[1]/div/div/div/slot/records-record-layout-row[2]/slot/records-record-layout-item[1]/div/span/slot/records-record-layout-input-name/lightning-input-name/fieldset/div/div/div[2]/lightning-input/div/div/input"))).send_keys("Max")
    delay(1)
    driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/div/records-lwc-record-layout/forcegenerated-detailpanel_lead___012000000000000aaa___full___create___recordlayout2/records-record-layout-block/slot/records-record-layout-section[1]/div/div/div/slot/records-record-layout-row[2]/slot/records-record-layout-item[1]/div/span/slot/records-record-layout-input-name/lightning-input-name/fieldset/div/div/div[4]/lightning-input/div[1]/div/input").send_keys("Nye")
    delay(1)
    driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/div/records-lwc-record-layout/forcegenerated-detailpanel_lead___012000000000000aaa___full___create___recordlayout2/records-record-layout-block/slot/records-record-layout-section[1]/div/div/div/slot/records-record-layout-row[3]/slot/records-record-layout-item[2]/div/span/slot/records-record-layout-base-input/lightning-input/div[1]/div/input").send_keys('Workplete')
    delay(1)
    # Click to generate Lead
    driver.find_element('xpath', "//button[@name='SaveEdit']").click()
    delay(10)


root=tk.Tk() # use to create new chat nav
root.geometry('350x450+30+400')
def getresult(message):
    arr=message.split(" ")
    if arr[0]=="Add":
        textarea.insert("end", "Bot : Processing.... ")
        create_lead_salesforce()
    else:textarea.insert("end", "Invalid Input")


def botReply():
    question=query.get()
    textarea.insert("end","\nYou : "+question)
    query.delete(0, "end")
    getresult(question)



root.title("Chat Bot for new prompt")
root.config(bg="aquamarine")
# Headear Logo
head=tk.PhotoImage(file='head1.png')
Insert_head=tk.Label(root,image=head)
Insert_head.config(bg='aquamarine')
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

#Buttom
btn = tk.Button(root, text = 'Send !', bd = '5',command = botReply)
btn.pack()
root.mainloop()
