# sample.py
"""
sample search functions from https://marcobonzanini.com/2015/01/12/searching-pubmed-with-python/
provides two functions, search and fetch details, that find fetch citation IDs from a search query, and displays details
about specific citation IDs
"""

from Bio import Entrez
from tkinter import ttk
import tkinter as tk
from tkinter import scrolledtext


class App(tk.Frame):
    def __init__(self, master):
        self.papers = None
        self.results = None

        self.master = master
        self.master.title('NCBI Crawler')
        self.master.geometry('700x700')

        # gives weight to the cells in the grid
        for rows in range(70):
            master.rowconfigure(rows, weight=1)
            master.columnconfigure(rows, weight=1)

        # Defines and places the notebook widget
        tk.Label(self.master, text="Search:").grid(row=0, column=66, sticky='E')
        self.searchbar = tk.Entry(self.master, insertwidth=1)
        self.searchbar.bind('<Return>', self.updateTab)
        self.searchbar.grid(row=0, column=67, columnspan=3, sticky="W")
        self.nb = ttk.Notebook(self.master)
        self.nb.grid(row=1, column=0, columnspan=70, rowspan=69, sticky='NESW')

        # Adds tab 1 of the notebook
        self.tablist = []
        for x in range(10):
            self.tablist.append(tk.Frame(self.nb))

        page = 1
        for tab in self.tablist:
            for rows in range(70):
                tab.rowconfigure(rows, weight=1)
                tab.columnconfigure(rows, weight=1)

            '''tk.Label(master=tab, text="Title").grid(row=0,column=0, columnspan=50)
            tk.Label(master=tab, text="Choose a section:").grid(row=1,column=0, columnspan=2)
            combo = ttk.Combobox(master=tab, state='readonly',
                         values=[
                             'Abstract',
                             'Author(s)',
                             'Keywords',
                         ])
            combo.bind("<<ComboboxSelected>>", selectioncommand=self.callbackFunc)
            combo.grid(row=1, column=2, columnspan=4)
            
            scrolledtext.ScrolledText(master=tab, wrap=tk.WORD, width=40).grid(row=2,column=0, columnspan=50, rowspan=49)'''
            self.nb.add(tab, text=f'Tab {page}')
            page += 1

    def search(self, query):
        Entrez.email = "coop.hopkin@gmail.com"
        handle = Entrez.esearch(db='pubmed',
                                sort='relevance',
                                retmax='20',
                                retmode='xml',
                                term=query)
        self.results = Entrez.read(handle)

        ids = ','.join(self.results['IdList'])
        Entrez.email = "coop.hopkin@gmail.com"
        handle = Entrez.efetch(db='pubmed',
                               retmode='xml',
                               id=ids)
        self.papers = Entrez.read(handle)

    '''def fetch_details(self):
        ids = ','.join(self.results['IdList'])
        Entrez.email = "coop.hopkin@gmail.com"
        handle = Entrez.efetch(db='pubmed',
                               retmode='xml',
                               id=ids)
        self.papers = Entrez.read(handle)'''

    def updateTab(self, event):
        self.search(self.searchbar.get())
        i = 0
        for tab in self.tablist:
            # Title of the current article
            tk.Label(master=tab, text=self.papers['PubmedArticle'][i]['MedlineCitation']['Article']['ArticleTitle']).grid(row=0,column=0,columnspan=50)
            # new notebook object for each tab
            currentnb = ttk.Notebook(master=tab)
            currentnb.grid(row=1, column=0)

            # tab for abstract
            absTab = tk.Frame(master=currentnb)
            absBody = scrolledtext.ScrolledText(absTab, wrap=tk.WORD)
            for line in self.papers['PubmedArticle'][i]['MedlineCitation']['Article']['Abstract']['AbstractText']:
                absBody.insert(tk.END, line + '\n\n')
            absBody.pack(expand=True, fill='both')
            currentnb.add(absTab, text='Abstract')

            # tab for Authors
            authTab = tk.Frame(master=currentnb)
            authBody = scrolledtext.ScrolledText(authTab, wrap=tk.WORD, width=50)
            for author in self.papers['PubmedArticle'][i]['MedlineCitation']['Article']['AuthorList']:
                if len(author) >= 5:
                    authBody.insert(tk.END, f'{author["LastName"]}, {author["ForeName"]}\n')
                    if len(author["AffiliationInfo"])>0:
                        authBody.insert(tk.END, f'Affiliation:{author["AffiliationInfo"][0]["Affiliation"]}\n\n')
                    else:
                        authBody.insert(tk.END, '\n\n')
            authBody.pack(expand=True, fill='both')
            currentnb.add(authTab, text='Authors')

            # tab for Keywords
            keyTab = tk.Frame(master=currentnb)
            keyBody = scrolledtext.ScrolledText(keyTab, wrap=tk.WORD, width=50)
            for keyword in self.papers['PubmedArticle'][i]['MedlineCitation']['KeywordList'][0]:
                keyBody.insert(tk.END, f'{keyword}\n')
            keyBody.insert(tk.END, '\n')
            keyBody.pack(expand=True, fill='both')
            currentnb.add(keyTab, text='Keywords')

            i+= 1


        '''page1 = scrolledtext.ScrolledText(master=nb, wrap=tk.WORD,width=40)
        nb.add(page1, text='Tab1')

        # Adds tab 2 of the notebook
        page2 = scrolledtext.ScrolledText(master=nb, wrap=tk.WORD,width=40)
        nb.add(page2, text='Tab2')'''




'''def wordWrap(string, length=120):
    for line in string:
        lineLength = 0
        for word in line.split(' '):
            lineLength += len(word) + 1
            if lineLength < length:
                print(word, end=' ')

            else:
                print()
                print(word, end=' ')
                lineLength = len(word)+1
        print()


def search(query):
    Entrez.email = "coop.hopkin@gmail.com"
    handle = Entrez.esearch(db='pubmed',
                            sort='relevance',
                            retmax='20',
                            retmode='xml',
                            term=query)
    results = Entrez.read(handle)
    return results


def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = "coop.hopkin@gmail.com"
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results = Entrez.read(handle)
    return results'''


if __name__ == '__main__':
    """results = search('vagal nerve stimulation epilepsy')
    id_list = results['IdList']
    papers = fetch_details(id_list)
    for i, paper in enumerate(papers['PubmedArticle']):
        print("%d) %s" % (i + 1, paper['MedlineCitation']['Article']['ArticleTitle']))

    # Pretty print the first paper in full to observe its structure
    import json
    with open('paperJSON.txt', 'w') as f:
        print(json.dumps(papers['PubmedArticle'][0], indent=2, separators=(',', ':')), file=f)

    print()
    wordWrap(papers['PubmedArticle'][0]['MedlineCitation']['Article']['Abstract']['AbstractText'], 80)"""

    root = tk.Tk()
    app = App(root)

    root.mainloop()