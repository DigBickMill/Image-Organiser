
# input the file path, then it will make folders of all image extensions in that folder

import os
import sys
import shutil

def getImginDIR(specpath):
#make sure its a directory and go into it
    try:
        os.chdir(specpath)
    except:
        print("not a directory")
    else:
        #find all images
        jpg, png, gif = createDIRArr(os.listdir())
        #move them
        [createandfillDir(x) for x in (jpg,png,gif)]
    return

def createandfillDir(x):
    if len(x)>0:
        #if there are images with this extension, make a new dir
        extname = x[0].split(".")[1]
        newdir = os.path.join(os.getcwd(),extname)
        if os.path.isfile(newdir) == True:  #if there is not already a directory
            print("Creating new folder called " + extname)
            os.mkdir(newdir)
        for i in x:
            #use shutil to move files to the new folder
            currentfilepath = str(os.getcwd()) + "\\" + i
            newfilepath = os.getcwd() + "\\" + extname + "\\" + i
            shutil.move(currentfilepath,newfilepath)
            print("Added " + i + " to " + extname + " new folder")


def createDIRArr(dirArr):
    extensions = [".jpeg", ".png",".jpg",".gif"] #NEEDS IMPROVEMENT (better way to do this)
    #bad practice to have hardcoded file extensions
    jpgArr =[]
    pngArr=[]
    gifArr=[]
    #sorts images into arrays of their given extenstion
    for ext in extensions:
        for file in dirArr:
            if ext in file.lower():
                if ext == ".jpeg" or ext == ".jpg":
                    jpgArr.append(file)
                elif ext == ".png":
                    pngArr.append(file)
                elif ext == ".gif":
                    gifArr.append(file)
    return jpgArr, pngArr, gifArr


if len(sys.argv) <=1:
    # let user know how to use script
    print("Add the file directory which in which images need to be found")
else:
    #use the path given to run the script
    image_path = sys.argv[1]
    getImginDIR(image_path)
