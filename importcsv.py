import csv
from tkinter import *
import tkinter.filedialog

header = []
c_list = []
data = []
line_counter = 0
j =1

print("선택파일의 확장자는 .csv 이며 형식은 [TagName, Timestamp, Value, Quality] ")
print("선택파일의 구조는 아래와 같다 ")
print("Row 1 > '', Tag 1, Tag 2, .....")
print("Row 2 > 시간, Tag 1의 값, Tag 2의 값, .....")
print("Row 3 > 시간, Tag 1의 값, Tag 2의 값, .....\n")

tryinput= input("Flat File로 떨구겠습니까? Y/N >  ")

if tryinput =="Y":
#입력 경로
    root = Tk().withdraw()
    title = 'Open csv.file as'
    ftypes = [('csv file', '.csv'), ('All files', '*')]
    inputFileName = tkinter.filedialog.askopenfilename(filetypes=ftypes, title="Select file",initialdir="/")

    print("선택파일 : " + inputFileName)

#저장경로
    root = Tk().withdraw()
    title = 'Save csv.file as'
    ftypes = [('csv file', '.csv'), ('All files', '*')]
    filename = tkinter.filedialog.asksaveasfilename(filetypes=ftypes, title=title,initialfile='.csv')
    print("저장경로 : " + filename)
    o = open(filename, "w",newline="")
    writer = csv.writer(o)

    with open(inputFileName,'rt', encoding='UTF-8-sig') as f:
        reader = csv.reader(f, delimiter=",")
        for line in reader:
            if line_counter == 0:
                header = line
            else:
                c_list=line
                for k in range(0,len(line)):
                    if k > 0:
                        writer.writerow([str(header[k]), str(c_list[0]),str(c_list[k]),"192"])
                    k += 1

            line_counter += 1

    o.close()
    f.close()
    print("완료")
else:
    exit()