
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N10212361
#    Student name: Jamie Martin
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  The Best, Then and Now
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application that allows the user to preview and print lists of
#  top-ten rankings.  See the instruction sheet accompanying this
#  file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.  YOU MAY NOT USE
# ANY NON-STANDARD MODULES SUCH AS 'Beautiful Soup' OR 'Pillow'.  ONLY
# MODULES THAT COME WITH A STANDARD PYTHON 3 INSTALLATION MAY BE
# USED.

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)
from urllib.request import urlopen

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.)
from tkinter import *

# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL

# Import the standard SQLite functions (just in case they're
# needed).
from sqlite3 import *

#
#--------------------------------------------------------------------#



#-----Downloader Function--------------------------------------------#
#
# This is our function for downloading a web page's content and both
# saving it on a local file and returning its source code
# as a Unicode string. The function tries to produce a
# meaningful error message if the attempt fails.  WARNING: This
# function will silently overwrite the target file if it
# already exists!  NB: You should change the filename extension to
# "xhtml" when downloading an XML document.  (You do NOT need to use
# this function in your solution if you choose to call "urlopen"
# directly, but it is provided for your convenience.)
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'download',
             filename_extension = 'html'):

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        web_page = urlopen(url)
    except ValueError:
        raise Exception("Download error - Cannot find document at URL '" + url + "'")
    except HTTPError:
        raise Exception("Download error - Access denied to document at URL '" + url + "'")
    except:
        raise Exception("Download error - Something went wrong when trying to download " + \
                        "the document at URL '" + url + "'")

    # Read its contents as a Unicode string
    try:
        web_page_contents = web_page.read().decode('UTF-8')
    except UnicodeDecodeError:
        raise Exception("Download error - Unable to decode document at URL '" + \
                        url + "' as Unicode text")

    # Write the contents to a local text file as Unicode
    # characters (overwriting the file if it
    # already exists!)
    try:
        text_file = open(target_filename + '.' + filename_extension,
                         'w', encoding = 'UTF-8')
        text_file.write(web_page_contents)
        text_file.close()
    except:
        raise Exception("Download error - Unable to write to file '" + \
                        target_file + "'")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

#-----------------------HTML DECODER AND BUTTON COMMANDS-------------------------------------------


#HTML TEMPLATE FOR EXPORTING DATA
html_template = """<!DOCTYPE html>
<html>

  <head>
    <meta charset = 'UTF-8'>
    <title>***TITLE***</title>
    <style>
        body {
            height: 100vh;
            margin: 0%;
        }
        h1 {
            width: 100%;
            text-align: center;
        }
        img {
            max-height: 50%;
            display: flex;
            margin: 1.5% auto;
        }
        table {
            width: 70%;
            text-align: center;
            margin: 0% 15%;
        }
        table, th, td {
            border: 1px solid black;
        }
        p {
            width: 100%;
            text-align: center;
        }
    </style>
  </head>
  <body>
      <h1>***TITLE***</h1>
      <h1>***DATE***</h1>
      <img src="***SRC***">  
      <table>
          <tr>
              <th>Number</th>
              <th>***HEAD1***</th>
              <th>***HEAD2***</th>
          </tr>
          <tr>
              <td>1</td>
              <td>***TEXT1***</td>
              <td>***DATA1***</td>
          </tr>
          <tr>
              <td>2</td>
              <td>***TEXT2***</td>
              <td>***DATA2***</td>
          </tr>
          <tr>
              <td>3</td>
              <td>***TEXT3***</td>
              <td>***DATA3***</td>
          </tr>
          <tr>
              <td>4</td>
              <td>***TEXT4***</td>
              <td>***DATA4***</td>
          </tr>
          <tr>
              <td>5</td>
              <td>***TEXT5***</td>
              <td>***DATA5***</td>
          </tr>
          <tr>
              <td>6</td>
              <td>***TEXT6***</td>
              <td>***DATA6***</td>
          </tr>
          <tr>
              <td>7</td>
              <td>***TEXT7***</td>
              <td>***DATA7***</td>
          </tr>
          <tr>
              <td>8</td>
              <td>***TEXT8***</td>
              <td>***DATA8***</td>
          </tr>
          <tr>
              <td>9</td>
              <td>***TEXT9***</td>
              <td>***DATA9***</td>
          </tr>
          <tr>
              <td>10</td>
              <td>***TEXT10***</td>
              <td>***DATA10***</td>
          </tr>
      </table>
      <p>The data from this document was generate from ***LINK***</p>
  </body>
</html>
"""

#Set the variables and create Tk window
window = Tk()
window.title("Top And Trending Right Now")
window.config(background="white")
font = 'Arial'
fontSize = 14
fileType = IntVar()
dataList = []
publication_date = ""
title = StringVar()

#custom imports for time, and to find the file path of the archived HTML documents
import time
import datetime
import os.path

#HTML decoder takes the link and regex and opens HTML document and finds specified text
def decoder(chartType, indexMultiplier):
    #draws variables globally
    global dataList
    global publication_date
    #resets variables
    publication_date = ""
    dataList = []
    outputText.delete('1.0', END)
    #gets the file Type
    fileChecker = fileType.get()

    #if the user wants a previous file then search the directory for the link and read
    if fileChecker == 0:
        response = open(chartType[1], encoding='utf-8')
        #publication dates could not be found on website source, code pulls date of download on the HTML file
        publication_date = str(time.strftime('%d/%m/%Y', time.gmtime(os.path.getmtime(chartType[1]))))
        html = response.read()

    #else if the user wants a current file then search the web for link and read plus decode to UTF-8    
    elif fileChecker == 1:
        response = urlopen(chartType[0])
        #publication dates could not be found on website source, code pulls date from current date
        publication_date = str(datetime.datetime.today().strftime('%d/%m/%Y'))
        html = response.read().decode('utf-8')
        
    else:
        print("Please Choose Previous or Current Charts")
    #uses the custom regex to find the primary and secondary Data in the html file      
    primaryData = findall(chartType[2], html)
    secondaryData = findall(chartType[3], html)
    #appends the data to a list and groups sibling info together
    for i in range(10):
        dataList.append([])
        dataList[i].append(primaryData[i])
        dataList[i].append(secondaryData[i*indexMultiplier])
    #packs the label and text area
    outputLabel.pack(side=TOP)
    outputText.pack(side=TOP)
    #inserts the data into the text area
    for item in dataList:
        index = dataList.index(item)
        #output creates numbers and adds the item on
        output = "(" + str(index + 1) + ") " + item[0] + "\n"
        outputText.insert(END, output)

#Sets decoder to run Steam Game Highest Played Games Right Now - updates on refresh in browser
def gamesStats():
    chartGames = ['https://store.steampowered.com/stats/',
              'Archives\SteamGameAndPlayerStats19092018.html',
              r'<a class="gameLink" .+>(.+)</a>',
              r'<span class="currentServers">(.+)</span>']
    outputPhoto.configure(file='GamesLogo.gif')
    title.set("Top 10 Video Games Being Played")
    indexMultiDouble = 2
    decoder(chartGames, indexMultiDouble)


#Sets decoder to run Cryptocurrency Highest Priced Market Cap - updates on refresh in browser
def cryptoStats():
    chartCrypto = ['https://cryptoreport.com/all/AUD/forex',
                'Archives\CryptoCurrencyForexChart19092018.html',
                r'id="td-name"><a href=".+/AUD/forex">(.+)</a></td>',
                r'<td class="mobile-td">([0-9]+[.][0-9]+)</td>']
    outputPhoto.configure(file='CryptoLogo.gif')
    title.set("Top 10 Most Popular Cryptocurrency")
    indexMultiDouble = 2
    decoder(chartCrypto, indexMultiDouble)


#Sets decoder to run Twitter Top Hashtags Used - updates continually in browser     
def twitterStats():
    chartHashtag = ['http://tweeplers.com/hashtags/?cc=WORLD',
                'Archives\TweeplersTrendingTwitterHashtags19092018.html',
                r'<a href="http://www.twitter.com/hashtag/.+"><b>(.+)</b></a>',
                r'<div class="col-xs-2" id=".+" style=".+">(.+)</div>']   
    outputPhoto.configure(file='The_Luigi_Twitter_Bird.gif')
    title.set("Top 10 Hashtags Used On Twitter")
    indexMultiOne = 1
    decoder(chartHashtag, indexMultiOne)


#EXPORTS DATA INTO A HTML FILE

def export():
    #gathers global data
    global dataList
    global publication_date
    #link and image sources for individual websites
    imgsrc = ['https://vignette.wikia.nocookie.net/tf2freakshow/images/d/d8/Steam-logo.png/revision/latest?cb=20160704160029',
           'https://banner2.kisspng.com/20180426/oie/kisspng-cryptocurrency-exchange-bitcoin-trade-initial-coin-5ae208da75b863.8036990215247628424822.jpg',
           'http://www.taylorclark.co/wp-content/uploads/2013/07/facebook-hashtags.png']
    linksrc = ['https://store.steampowered.com/stats/',
            'https://cryptoreport.com/all/AUD/forex',
            'http://tweeplers.com/hashtags/?cc=WORLD']
    #opens/creates the html file
    html_file = open('export.html', 'w', encoding = "utf-8")
    #gets the title and inputs the title + publication date into the html document
    inputTitle = title.get()
    html_new = html_template.replace('***TITLE***', inputTitle)
    html_new = html_new.replace('***DATE***', publication_date)
    #depending on the title, imports specific img links and content
    if inputTitle == "Top 10 Video Games Being Played":
        index = 0
        html_new = html_new.replace('***SRC***', imgsrc[0])
        html_new = html_new.replace('***HEAD1***', 'Game')
        html_new = html_new.replace('***HEAD2***', 'Players Online Right Now')
    elif inputTitle == "Top 10 Most Popular Cryptocurrency":
        index = 1
        html_new = html_new.replace('***SRC***', imgsrc[1])
        html_new = html_new.replace('***HEAD1***', 'Cryptocurrency')
        html_new = html_new.replace('***HEAD2***', 'Price in AUD $')
    elif inputTitle == "Top 10 Hashtags Used On Twitter":
        index = 2
        html_new = html_new.replace('***SRC***', imgsrc[2])
        html_new = html_new.replace('***HEAD1***', 'Hashtag')
        html_new = html_new.replace('***HEAD2***', 'Tweets per 20,000 tweets')
    else:
        pass
    #sets the source link for viewers to go to the website
    link = '<a href="'+linksrc[index]+'">'+linksrc[index]+'</a>'
    html_new = html_new.replace('***LINK***', link)
    #inserts the data into the HTML list
    for item in dataList:
        name = item[0]
        data = item[1]
        #gets the index of the item to use in the for loops
        index = dataList.index(item)
        #txtSearch and dataSearch are strings used in the replace functions
        txtSearch = '***TEXT' + str(index+1) + '***'
        dataSearch = '***DATA' + str(index+1) + '***'
        html_new = html_new.replace(txtSearch, name)
        html_new = html_new.replace(dataSearch, data)
    #writes/saves the new content to the document and closes it
    html_file.write(html_new)
    html_file.close()

def save():
    #gather global variables
    global dataList
    global publication_date
    #replaces any apostrophes with two apostrophes (used in SQL)
    for item in dataList:
        item[0] = item[0].replace("'", "''")
        item[1] = item[1].replace("'", "''")
    #Connects to the SQL Database
    connection = connect(database = 'top_ten.db')
    top_ten = connection.cursor()
    #For the items in the dataList create new records and insert them
    for item in dataList:
        name = item[0]
        info = item[1]
        index = dataList.index(item)
        ranking = index + 1
        sql = "INSERT INTO top_ten VALUES ('" + str(publication_date) + "', '" + str(ranking) + "', '" + str(name) + "', '" + str(info) + "')"
        top_ten.execute(sql)
    #write/save the new records in the SQL Database and close it
    connection.commit()
    top_ten.close()
    connection.close()


    
#-------------------TKINTER CODE----------------------------------------

#front image of the GUI
photo = PhotoImage(file='TrendingLogo.gif')
img = Label(image=photo, border=0)
img.image = photo
img.pack()

#creates the frame for the buttons
mainframe = Frame(window)
mainframe.pack()

#main buttons that previews each list and outputs it to a text area
btn_1 = Button(mainframe, text="Preview Video Games", command = gamesStats, font = (font, fontSize), pady=10, width=25, bg="white", border=0.5).pack(side=LEFT)
btn_2 = Button(mainframe, text="Preview Cryptocurrency", command = cryptoStats, font = (font, fontSize), pady=10, width=25, bg="white", border=0.5).pack(side=LEFT)
btn_3 = Button(mainframe, text="Preview Twitter Hashtags", command = twitterStats, font = (font, fontSize), pady=10, width=25, bg="white", border=0.5).pack(side=LEFT)

#output area; consists of image and text area. Image changes depending on chart type
#output Image
outputFrame = Frame(window, bg="white")
outputFrame.pack()

outputPhoto = PhotoImage(file="")
outputImg = Label(outputFrame, image=outputPhoto, border=0, bg="white")
outputImg.image = outputPhoto
outputImg.pack(side=LEFT)

#output Text
outputTextFrame = Frame(outputFrame, bg="white")
outputTextFrame.pack()
outputLabel = Label(outputTextFrame, textvariable=title,border=0, bg="white", font = (font, fontSize), pady=25)
outputText = Text(outputTextFrame, border = 0, bg="white", width=45, padx=40, font = (font, (fontSize-1)), height=10)

#Radiobuttons that set Previous or Current Charts
checkerFrame = Frame(window)
checkerFrame.pack()
rdo1 = Radiobutton(checkerFrame, text="Previous Charts", variable = fileType, value = 0, pady=10, font = (font, fontSize), width=15, bg="white")
rdo1.pack(side=LEFT)
rdo2 = Radiobutton(checkerFrame, text="Current Charts", variable = fileType, value = 1, pady=10, font = (font, fontSize), width=15, bg="white")
rdo2.pack(side=LEFT)

#Export button which runs export() and the Save Button which runs save()
buttonFrame = Frame(window)
buttonFrame.pack()
btn_4 = Button(buttonFrame, text="Export", command = export, font = (font, fontSize), pady=10, width=15, bg="white", border=0.5).pack(side=LEFT)
btn_5 = Button(buttonFrame, text="Save", command = save, font= (font, fontSize), pady=10, width=15, bg="white", border=0.5). pack()

window.mainloop()
#-----------------------END TKINTER----------------------------------------------
