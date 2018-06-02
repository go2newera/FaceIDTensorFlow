# -*- coding: utf-8 -*-
import os

DATA_INFO_LIST = ["./wider_face_split/wider_face_train_bbx_gt.txt"]
SAVE_FILE_NAME = "./AnnoDir/wilderFaceAnno.txt"

def generateWiderFaceAnnoInfo(OriginalAnnoList, saveFile):

    allFormatedAnnoInfo = []
    onesAnnoInfo = []

    for file in DATA_INFO_LIST:

        originalAnno = []

        with open(file) as f :
            originalAnno = f.read().split("\n")

        if originalAnno is None:
            print("File name %s Failure"%(file))
            return "Failure"

        for content in originalAnno:

            if content.find(".jpg") != -1:  #find a new picture

                if len(onesAnnoInfo) > 1:
                    allFormatedAnnoInfo.append(onesAnnoInfo)  #add a formated anno information

                onesAnnoInfo = []
                onesAnnoInfo.append(content)

            elif len(content) > 5: #skip anno number

                content = content.split(" ")

                x1 = str(float(content[0]))
                y1 = str(float(content[1]))
                x2 = str(float(content[0]) + float(content[2]))
                y2 = str(float(content[1]) + float(content[3]))

                onesAnnoInfo.append(x1)
                onesAnnoInfo.append(y1)
                onesAnnoInfo.append(x2)
                onesAnnoInfo.append(y2)
            else:
                pass

    counter = 0

    for context in allFormatedAnnoInfo:

        tmp = " ".join(context).strip()

        counter+=1

        with open(SAVE_FILE_NAME, "a") as f:
            f.write(tmp + "\n")
            # f.writelines("\n")

    return "OK And The number processed is %d"%(counter)


if __name__ == "__main__":

    if os.path.exists(SAVE_FILE_NAME):
        os.remove(SAVE_FILE_NAME)

    ret = generateWiderFaceAnnoInfo(DATA_INFO_LIST, SAVE_FILE_NAME)

    print(ret)