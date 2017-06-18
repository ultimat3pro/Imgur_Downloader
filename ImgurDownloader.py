# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 07:35:01 2017

@author: Ultimate Pro
"""

import urllib
import re
import os


def findImagesIn(albumId):
    print("Finding images in album....")
    #Create album link
    prefix = "https://imgur.com/a/"
    albumLink = prefix + albumId+"/layout/blog"
    #read source
    page = urllib.request.urlopen(albumLink)
    lines = str(page.readlines())
    #Find end identifier and type of image
    images = re.findall('.*?{"hash":"([a-zA-Z0-9]+)".*?"ext":"(\.[a-zA-Z0-9]+)".*?', lines)
    download(images,albumId)
    #return images
    
def download(images,albumId):
    print("Creating direct links to images...")
    #create image array without duplicates
    imgB = list(set(images))
    
    #create complete path
    path = "albums/"+albumId+"/"
    
    #Create directory if not exists from path
    if not os.path.exists(path):
        os.makedirs(path)
    
    #Create list with completed link for each image
    imgLinks = []
    for i in range(len(imgB)):
        url = "https://i.imgur.com/"+imgB[i][0]+imgB[i][1]
        imgLinks.append(url)
    
    print("Downloading and saving images...")
    
    #Retrieve images following links
    for i in range(len(imgLinks)):
        print(imgLinks[i])
        urllib.request.urlretrieve(imgLinks[i],path+str(i)+imgB[i][1])
    
    print("Download complete")
    
def main():
    findImagesIn("tFOwd")
    findImagesIn("UrVN2")
    
main()    