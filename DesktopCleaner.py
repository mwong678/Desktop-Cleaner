#!/usr/bin/env python

import sys
import os
import platform

class DesktopCleaner:

    listOfExtensions = [];
    doNotInclude = ['BIN','DS_Store','localized','ini','db'];
    listOfFiles = [];
    userhome = os.path.expanduser('~');
    desktop = userhome + '/Desktop/';
    useros = platform.system(); # returns e.g. 'Linux' 'Windows'
    distribution = platform.linux_distribution(); #in case it is a Unix

    def __init__(self, path):
        if len(path) != 0:
            self.desktop = path;
        self.getExtensions();
        self.makeDirectories();
        self.cleanUp();
    def getExtensions(self):
        for f in os.listdir(self.desktop):
            ext = f.split(".")[-1];
            if len(f.split(".")) > 1 and ext not in self.doNotInclude and os.path.isfile(self.desktop+f):
                self.listOfFiles.append(f);
                if ext not in self.listOfExtensions:
                    self.listOfExtensions.append(ext);
    def makeDirectories(self):
        for e in self.listOfExtensions:
            if not os.path.exists(self.desktop+e):
                os.makedirs(self.desktop+e);
    def cleanUp(self):
        for i in self.listOfFiles:
            for j in self.listOfExtensions:
                if j in i:
                    os.rename(self.desktop+i,self.desktop+j+'/'+i);

if __name__ == "__main__":
    path = raw_input("Enter path name(enter no path for desktop): ");
    cleaner = DesktopCleaner(path);
