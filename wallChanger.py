import os
import random
import time

path = '/home/rest/wall'
tempFileName = '/tmp/wallChanger.txt'
sleepTime = 1


# READ SHOWN IMAGES:
shownImagesList = []
with open(tempFileName) as openfileobject:
    for line in openfileobject:
        replaced = line.replace('\n', '')
        shownImagesList.append(replaced)
        # print(replaced)
openfileobject.close()


# print()
# READ IMAGES DIRECTORY
allImagesFromPath = []
# i = 0
for r, d, f in os.walk(path):
    for file in f:
        # i += 1
        join = os.path.join(r, file)
        allImagesFromPath.append(join)
        # if i == 10:
        #     break

random.shuffle(allImagesFromPath)


def writeToTempFile():
    tempFileWriter = open(tempFileName, "a+")
    tempFileWriter.write(image + '\n')
    tempFileWriter.close()


for image in allImagesFromPath:
    if set(shownImagesList) == set(allImagesFromPath):
        print('CONTENTS IDENTICAL! CLEAR')
        shownImagesList = []

        # clean temp file
        open(tempFileName, 'w').close()

    if image not in shownImagesList:
        shownImagesList.append(image)
        print('SHOW '+image)
        time.sleep(sleepTime)
        # WRITE SHOWN IMAGES
        writeToTempFile()
        myCmd = 'feh --bg-fill ' + image
        os.system(myCmd)
