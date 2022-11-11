import datetime
import json
import random
from datetime import date

import requests
from bs4 import BeautifulSoup
from gforms import Form
from gforms.elements import Paragraph, Short, Value

from Data.discordUsers import discordUser

x = 0

def info():
    
    url = 'https://docs.google.com/forms/d/e/1FAIpQLSdKCRY4WqJgLBhsaoAu4iWPzPpHAuQrfVOoKtZTKGAxKGZCNg/formResponse'

    formID = random.randint(1,4896)
    r = requests.get(f'https://earth2.kiwismp.fun/info.php?type=ban&id={formID}')
    global soup
    soup = BeautifulSoup(r.content, 'html.parser')
    
    
    def getName():
        try:
            names = soup.find_all('a')
            formatedName = ((names[7].prettify()).split())[2]
            print(formatedName) #remove debug line
            return formatedName
        except:
            KeyError, IndexError, ValueError, NameError
            return

    global ign
    ign = getName()
    
    def getStaff():
        try:
            names = soup.find_all('a')
            formatedStaffIGN = ((names[8].prettify()).split())[2]
            print(formatedStaffIGN) #remove debug line
            return formatedStaffIGN
        except:
            KeyError, IndexError, ValueError, NameError
            return

    def getReason():
        try: 
            scrape = soup.find_all('td')
            formatedReason = scrape[5].string
            print(formatedReason)
            return formatedReason
        except:
            KeyError, IndexError, ValueError, NameError
            return
    
    global reason
    reason = getReason()
    global discordUsername
    def pseudoDiscord():
        try:
            tag = []
            digits = 0
            while digits < 4:
                discordDigits = random.randint(0,9)
                digits += 1
                tag.append(discordDigits)
            _tag = f"{tag[0]}{tag[1]}{tag[2]}{tag[3]}"
            digits = 0
            pseudoDiscord = f'{discordUser[random.randint(0,526)]}#{_tag}'
            print(pseudoDiscord)
            return pseudoDiscord
        except:
            KeyError, IndexError, ValueError, NameError
            return
    
    
    discordUsername = pseudoDiscord()

    def unbanReasoning():
        try:
                #scrape
            scrape = soup.find_all('td')
            _getDate = scrape[7].string
            try:
                names = soup.find_all('a')
                IGN = ((names[7].prettify()).split())[2]
            except:
                KeyError, IndexError, ValueError, NameError
                return
            try: 
                scrape = soup.find_all('td')
                reason = scrape[5].string
            except:
                KeyError, IndexError, ValueError, NameError
                return
            
            #logic
            remTime = _getDate[:-7]
            getYear = remTime[-4:]
            getDay = _getDate[:-13]
            Day = getDay[-2:]
            getMonth = _getDate[:-15]
            Months = ['January ','February ','March ','April ','May ','June ','July ','August ','September ','October ','November ','December ']
            res = any(ele in getMonth for ele in Months)
            if res == True:
                monthCheck = Months.index(getMonth)
                monthInt = monthCheck + 1
            else: 
                monthCheck = 'January'
                monthInt = 1
            today = datetime.date.today()
            year = today.year
            currentTime = datetime.datetime(year, today.month, today.day)
            banDate = datetime.datetime(int(getYear), int(monthInt), int(Day))
            deltaTime = currentTime - banDate
            # Get Intro
            intro = f'intro{random.randint(1,11)}'
            #line 1
            if int(deltaTime.days) <= 30:
                line1_start = f'banTime{random.randint(1,3)}'
                realize = f'realize{random.randint(0,3)}'
            if deltaTime.days > 30 and deltaTime.days <= 350:
                line1_start = f'banTime{random.randint(4,5)}'
                realize = f'realize{random.randint(2,4)}'
            elif deltaTime.days > 350:
                line1_start = f'banTime{random.randint(4,7)}'
                realize = f'realize{random.randint(2,4)}'
            if line1_start != 'banTime1':
                    connectingWord = f'words{random.randint(1,2)}'
                    line1_end = f'banTime_ending{random.randint(1,3)}'
            else:
                connectingWord = 'words3'
                line1_end = 'banTime_ending4'
            
            # Ban Reasoning
            if line1_end == 'banTime_ending4':
                ban_reasoning = 'banReasoning8'
            else:
                ban_reasoning = f'banReasoning{random.randint(1,7)}'
            _realize = f'realize-{random.randint(4,8)}'
            miss = f'miss{random.randint(1,7)}'
            appology = f'appology{random.randint(1,6)}'
            appologyEnd = f'appologyEnd{random.randint(1,4)}'
            appologyOption = f'appologyOption{random.randint(1,12)}'
            chance = f'chance{random.randint(1,2)}'
            conclusion = f'conclusion{random.randint(1,8)}'
            sign = random.randint(0,1)
            if sign == 1:
                addName = str(IGN)
            elif sign == 0:
                addName = ''
            
            #Get JSON Data
            with open("Data\Logic.json", "r") as data_options:
                options = json.load(data_options)
                intro = options[f"{intro}"]
                line1_start = options[f'{line1_start}']
                connectingWord = options[f'{connectingWord}']
                line1_end = options[f'{line1_end}']
                ban_reasoning = options[f'{ban_reasoning}']
                realize = options[f'{realize}']
                _realize = options[f'{_realize}']
                miss = options[f'{miss}']
                appology = options[f'{appology}']
                appologyEnd = options[f'{appologyEnd}']
                appologyOption = options[f'{appologyOption}']
                chance = options[f'{chance}']
                conclusion = options[f'{conclusion}']
            
            #WSIBU Text
            Text = f'''{intro}\n{line1_start}{connectingWord} {line1_end}{ban_reasoning} '{reason}'. After {realize} {_realize} I missed kiwi and {miss}.{appology} {appologyEnd} {appologyOption} {chance} {conclusion} {addName}'''
            print(Text) 
            return Text       
        except:
            KeyError, IndexError, ValueError, NameError, TypeError
            return
    
    global pseudoReason
    pseudoReason = unbanReasoning()
    
    def extra():
        isTrue = random.randint(0,500)
        if isTrue == 500:
            with open('Data\extraData.json', 'r') as extraInfo:
                options = json.load(extraInfo)
                logic = options[f'option{random.randint(1,6)}']
            
            return logic
        else:
            return ''
    
    global extraInfoSend
    extraInfoSend = extra()
    
    #data
    print('======================================')
    getName()
    pseudoDiscord()
    getStaff()
    getReason()
    unbanReasoning()
    extra()
    print('======================================')
    
    def data_input(element, page_index, element_index):
        if page_index == 1 and element_index == 1:
            return getName()
        if isinstance(element, Short) and element.name == 'Discord Username and Tag':
            return pseudoDiscord()
        if isinstance(element, Short) and element.name == 'Minecraft Username':
            return getName()
        if isinstance(element, Paragraph) and element.name == 'Ban Reason':
            return getReason()
        if isinstance(element, Paragraph) and element.name == 'Why do you deserve to be unbanned?':
            return unbanReasoning()
        if isinstance(element, Paragraph) and element.name == 'Extra Information (Optional)':
            return extra()
        return Value.DEFAULT
    form = Form()
    form.load(url)
    print(form.to_str(indent=2))
    form.fill(data_input)
    form.submit()
    
    global x
    x += 1