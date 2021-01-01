import tkinter as tk
from tkinter import Listbox
import json
import os
from scrapy.crawler import CrawlerProcess
# cannot use: from scrapy import log
from gundam_spider.gundam_spider.spiders.gundam_spider import GundamSpider

with open('gundam_spider\gundams.json') as f:
  data = json.load(f)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Scrape"
        self.hi_there["command"] = self.display_gundam
        self.hi_there.pack(side="top")

        self.quit_btn = tk.Button(self, text="QUIT", fg="red",
                              command=self.quit_gundam)
        self.quit_btn.pack(side="bottom")

    def quit_gundam(self):
        file_path = 'items.json'
        if os.path.exists(file_path):
            os.remove(file_path)
        root.destroy()

    def display_gundam(self):
        # print(data)
        process = CrawlerProcess(settings={
            "FEEDS": {
                "items.json": {"format": "json"},
            },
        })
        process.crawl(GundamSpider)
        process.start()
        
        with open('items.json') as f:
            parsed_gundams = json.load(f)

        for g in parsed_gundams:
            # print(type(g))
            listbox.insert(0, g)

        # print(parsed_gundams)
        # print(type(parsed_gundams))

root = tk.Tk()
root.title("Gundam Scraper")
root.minsize(300,300)
photo = tk.PhotoImage(file = "icon.png")
root.iconphoto(False, photo)

listbox = Listbox(root, height = 10, width = 20, bg = "white", font = ('Times',8), fg = "blue") 
listbox.pack()

app = Application(master=root)

app.mainloop()