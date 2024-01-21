import tkinter
from tkinter import *
from bs4.element import Comment
import manganelo.rewrite as manganelo
import os
from datetime import datetime, timedelta, date
import requests
from bs4 import BeautifulSoup
import calendar



m = tkinter.Tk()
m.title = ("Manga")
m.geometry("700x600")
last_update = tkinter.StringVar()
manga_title = tkinter.StringVar()
chapter_download = tkinter.StringVar()
max_chapters = tkinter.StringVar()
results_manganame = ""
chapters = []


def mangaSearch():
    #finds the manga based on the search query
    results = manganelo.search(title=manga_title.get())
    print("Loading chapters...")
    first = results[0]
    mangaURL = first.url
    page = requests.get(mangaURL)
    global chapters
    chapters = first.chapter_list()


    
    global max_chapters
    max_chapters.set(len(chapters))
    #max_chapters_int = len(chapters)
    chapNumber.config(from_ = 0, to = len(chapters))
    

    #webscrapes the website to find the last updated date on the website
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find("span", {"class": "stre-value"})
    global results_manganame
    results_manganame = soup.find("a", {"href": mangaURL})
    last_update.set("The manga I found on manganelo was: " + results_manganame.text + "which was last updated on: " + results.text)
    print(f"Manga search complete. The name of the manga I found on manganelo was: {results_manganame.text}") #testing purposes
    

def downloadManga():
    downloadChapter = chapters[int(chapNumber.get())].download(path = f"C:\\Soham\\Manga\\{results_manganame.text}{chapters[int(chapNumber.get())].title}.pdf")
    os.startfile("C:\\Soham\\Manga")
    
    
mangaNameEntry = tkinter.Label(m, bg = "#00002c", fg = "#ffc000" ,  font = ("Visby CF Bold", 25), text = "Enter Manga Name Below: ")
mangaNameEntry.pack()

mangaName = tkinter.Entry(m, cursor = "circle",  bg = "#00002c", highlightcolor = "#ffc000", highlightthickness = 2, highlightbackground = "#ffc000" ,fg = "#ffc000", textvariable = manga_title)
mangaName.pack(pady=15)

lastUpdateBtn = tkinter.Button(m, bg = "#ffc000", fg = "#00002c", padx = 5, pady = 5, text = "Index this manga", activebackground = "#00002c", activeforeground = "#ffc000", command = mangaSearch)
lastUpdateBtn.pack()

lastUpdateLabel = tkinter.Label(m, bg = "#00002c", fg = "#ffc000", font = ("Visby CF Bold", 10),  textvariable = last_update)
lastUpdateLabel.pack(pady = 10)

global chapNumber
chapNumber = tkinter.Spinbox(m, from_ = 0, to = 1000, textvariable = max_chapters)
chapNumber.pack()

downloadChapterBtn = tkinter.Button(m, text = "Download chapter", command = downloadManga)
downloadChapterBtn.pack()





m.config(background="#00002c")
m.mainloop()











# LEGACY ERRORS
# >>> creates another spinbox if u erase and type again. make sure to create 1 spinbox 
# >>> set the spinbox max value based on manga chapters 
# >>> then get the current spinbox value when downloading the chapter. 