import tkinter as tk
from tkinter import filedialog, messagebox
import tkinter.font as tkfont
import os

print("\033c\033[43;30m\n")


class starts:
    def __init__(self):
        self.value=["gr","pt","fr","gm","es"]
        print("select from language 0-4? " )
        self.froms=self.value[self.lang()]
        print("select into language 0-4? " )
        self.into=self.value[self.lang()]
        print("from "+self.froms+" into "+self.into)
        print("give me a word to traslate to ? " )
        self.word0=input().strip()
        self.fromm=self.load_keywords(self.froms)
        self.intm=self.load_keywords(self.into)
        n=0
        for n in range(len(self.fromm)):
            nn=self.fromm[n].strip()
            if nn==self.word0:
                print(self.intm[n])

    def lang(self):
        print("0-gr inglish \n1-pt portugal\n2-fr france\n3-gm germany\n4-es spain\n? " )
        return int(input())
    def load_keywords(self,names):
        try:
            with open(names+".csv", "r") as f:
                data = f.read()
                keywords =  data.split(",") 
                #print(keywords)
                return keywords
        except FileNotFoundError:
            messagebox.showerror("Erro", "Ficheiro " + names + ".csv não encontrado!")
            return []

    



starts()
