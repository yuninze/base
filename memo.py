zyeon
zyeon=pd.pivot_table(a,values='money',index=['idx','name','cn','wm'],aggfunc=np.sum)
zyeon.unstack().to_csv('zyeon.csv',encoding='utf-8-sig')

ca=concoction('C:/82/stat/concat/ca',10,10)
cz=concoction('C:/82/stat/concat/cz',10,10)
la=concoction('C:/82/stat/concat/la',70,550)
lz=concoction('C:/82/stat/concat/lz',70,550)

filenamelist,dadtaidxlist=lachk('O:/82/result/PRJ3668_809900/ANNOTATION')

import csv

with open('c:/filenamelist.csv',encoding='utf-8',newline='',mode='w+') as filenamelistcsvfile:
	csvwriter=csv.writer(filenamelistcsvfile)
	[csvwriter.writerow([t]) for t in filenamelist]

with open('c:/dataidxlist.csv',encoding='utf-8',newline='',mode='w+') as dataidxlistcsvfile:
	csvwriter=csv.writer(dataidxlistcsvfile)
	[csvwriter.writerow([t]) for t in dataidxlist]

위반 이미지파일 개수, 위험 이미지파일 개수, 정상 이미지파일 개수
정상 이미지파일 개수=전체 개수-(위반 이미지파일 개수+위험 이미지파일 개수)

ArcNameList=ZipFile('PRJ3668.zip').namelist()
ArcNameListJsonfile=[x for x in ArcNameList if '.json' in x]
ArcNameListing=[x for x in ArcNameList if '.jpg' in x]
ArcNameListingSon={}
ArcNameListingSon['aw']=[h for h in ArcNameListing if 'IMAGE/A/WHITE/' in h]
ArcNameListingSon['ay']=[h for h in ArcNameListing if 'IMAGE/A/YELLOW/' in h]
ArcNameListingSon['ab']=[h for h in ArcNameListing if 'IMAGE/A/BLUE/' in h]
ArcNameListingSon['as']=[h for h in ArcNameListing if 'IMAGE/A/SHOULDER/' in h]
ArcNameListingSon['bw']=[h for h in ArcNameListing if 'IMAGE/B/WHITE/' in h]
ArcNameListingSon['by']=[h for h in ArcNameListing if 'IMAGE/B/YELLOW/' in h]
ArcNameListingSon['bb']=[h for h in ArcNameListing if 'IMAGE/B/BLUE/' in h]
ArcNameListingSon['bs']=[h for h in ArcNameListing if 'IMAGE/B/SHOULDER/' in h]
ArcNameListingSon['cw']=[h for h in ArcNameListing if 'IMAGE/C/WHITE/' in h]
ArcNameListingSon['cy']=[h for h in ArcNameListing if 'IMAGE/C/YELLOW/' in h]
ArcNameListingSon['cb']=[h for h in ArcNameListing if 'IMAGE/C/BLUE/' in h]
ArcNameListingSon['cs']=[h for h in ArcNameListing if 'IMAGE/C/SHOULDER/' in h]
for x,y in ArcNameListingSon.items():print(f'{x}: {len(y)}')

frame1=pd.read_csv('c:/82_stats_fuck.csv',nrows=5000,encoding='utf-8-sig',low_memory=False)

from libtype import *
cw=pd.read_csv('cw.csv')
cw.cn=cw.cn.apply(dashingcn)
cw.pn=cw.pn.apply(dashingpn)
cw.money=cw.money.apply(accountingtostr)
cw.set_index(['name','cn','pn'],inplace=True)

#cn slicing for new indexing
def cnslicing(scalar):
	return str(scalar)[:8]
def concatstr(scalar0,scalar1):
	return str(scalar0)+str(scalar1)
	
for i in stat.index:
	x=stat.loc[i,'성명']
	y=stat.loc[i,'주민번호\n(13자리)']
	stat.loc[i,'idx']=concatstr(x,cnslicing(y))

for i in frame1.index:
	x=frame1.loc[i,'name']
	y=frame1.loc[i,'cn']
	frame1.loc[i,'name']=concatstr(x,cnslicing(y))
	
for i in a.index:
	x=a.loc[i,'name']
	y=a.loc[i,'cn']
	a.loc[i,'idx']=concatstr(x,cnslicing(y))
	
for i in cw.index:
	x=cw.loc[i,'name']
	y=cw.loc[i,'cn']
	cw.loc[i,'idx']=concatstr(x,cnslicing(y))
	
	
frame3=frame2[pd.isna(frame2.성명)]
for i in frame3.index:
	frame3.loc[i,'name']=str(i)[:3]
	frame3.loc[i,'cn']=str(i)[3:]

frame0.set_index(inplace=True)
fuck=pd.pivot_table(frame0,values='money',index=['name','wm'])
fuck.unstack()

half
float16
single
float32
double
float64

a.iloc[:,56:]=a.iloc[:,56:].applymap(fuk)

#Load sheetfile
b=pd.read_excel(
"82.xlsx",
sheet_name=1,
na_filter=False,
nrows=5000,






#Set target columns
targetcols='H,CE,DM'

#Load sheetfile
a=pd.read_excel(
"82.xlsx",
sheet_name=1,
na_filter=False,
nrows=5000,
usercols=targetcols)

#Sanitize column names and row
a.columns=['idx','decPay','work']
a=a.iloc[4:,:]

#Set concatenated strings as index
a.set_index('idx',inplace=True)
#Remove stranges
a=a[a.index!='']
#Remove December nonparticipatants, typing
a=a.applymap(removeblank)
#Groupbying and transforming
a=a.groupby(by=a.index.names).transform('sum')

a.sort_index(inplace=True)



for fuck in d.index:
    col=d.loc[fuck]
    row=col.loc["variety"]
    if "장애" in row:
        col.loc["zangae"]="O"
    elif "임신" in row:
        col.loc["preg"]="O"
    elif "단절" in row:
        col.loc["gzy"]="O"
    elif "보훈" in row:
        col.loc["bohun"]="O"
    elif "다문화" in row:
        col.loc["damunwha"]="O"
    elif "초등" in row:
        col.loc["choding"]="O"
    elif "대학생" in row:
        col.loc["daeding"]="O"
    elif "투잡" in row:
        col.loc["jobtwo"]="O"
    elif "미취업자" in row:
        col.loc["jobno"]="O"
    elif "실직자" in row:
        col.loc["jobloss"]="O"
    elif "저소득" in row:
        col.loc["lowincome"]="O"
    elif "장기실업" in row:
        col.loc["jobless"]="O"
    elif "가장" in row:
        col.loc["mobuzang"]="O"
    elif "이주" in row:
        col.loc["visamarry"]="O"
    elif "북한" in row:
        col.loc["bukhan"]="O"
    elif "자영업" in row:
        col.loc["selfempoly"]="O"
    elif "AI" in row:
        col.loc["aihubhx"]="O"

import pandas as pd



#Groupbying, transforming


#Filter dupe indexes only




a.iloc[:,56:]=a.iloc[:,56:].applymap(fuk)

#Load sheetfile
b=pd.read_excel(
"82.xlsx",
sheet_name=1,
na_filter=False,
nrows=5000,

#Set target columns
targetcols='H,CE,DM'

#Load sheetfile
a=pd.read_excel(
"82.xlsx",
sheet_name=1,
na_filter=False,
nrows=5000,
usercols=targetcols)

#Sanitize column names and row
a.columns=['idx','decPay','work']
a=a.iloc[4:,:]

#Set concatenated strings as index
a.set_index('idx',inplace=True)
#Remove stranges
a=a[a.index!='']
#Remove December nonparticipatants, typing
a=a.applymap(removeblank)
#Groupbying and transforming
a=a.groupby(by=a.index.names).transform('sum')

a.sort_index(inplace=True)





def queuing():
arc=ZipFile(zipfile,"r")
infolist=arc.infolist()
arcnamelist=[infolist[x] for x in range(len(infolist)) if infolist[x].endswith(".jpg")]

queuing by genComp

factor=2000

blockcount=len(donefilename)//factor
blocknumber=len(donefilename)%factor
blockindex=0

donefilenamelist=[]
donefilenameblock=dict()

for x in range(blockSize)
    [blockindex:blockcontent for blockindex,blockcontent in range(blockcount),[donefilenamelist for x in range(blockSize 

d[["zangae","preg","gzy","bohun","damunwha","choding","daeding","jobtwo","jobno","jobloss","lowincome","jobless","mobuzang","visamarry","bukhan","selfempoly","aihubhx","ichx"]]="X"


def EndSwitch(VarBool):
    while VarBool:
        for x in ["--","//","\\\\"]:
            print("\b\b"+x,end="")

print("take care of utw")
os.chdir(arcDirPath)
foFromArc=arc.extractall(members=(set(arcil)-set(g)),path="")
print("..utw extracted: "+arc.filename)
foForEach=foFromArc.replace("e:\\82\\done\\",(arcDirPath.replace("\\done\\","\\cat\\utw\\"))+"\\")

try:
    os.makedirs(os.path.dirname(foForEach),exist_ok=True)
except:
    pass
finally:
    try:
        os.rename(foFromArc,foForEach)
    except:
        pass
    shutil.rmtree("IMAGE")
    ng1+=1


0. purify
1. indexing by name
2. .....fillna
3. fill wage-related object
4. .......
2. concat bo,ta
3. 



    for y in shoulder:
        if y in arc.namelist():
            arc.extract(y)
            shutil.make_archive(arc.filename+"_SHOULDER_"+str(len(shoulder)),"zip","IMAGE")
    return None

                for h in a:
                    arc.extract(h,path=arc.filename+"_A")
                with open(arc.filename+"_A_"+str(len(a))+".csv","w") as y:
                    csv.writer(y).writerow(["filename_a"])
                    for x in a:
                        csv.writer(y).writerow([x])
                pd.read_csv(arc.filename+"_A_"+str(len(a))+".csv",encoding=enc).to_csv(arc.filename+"_A_"+str(len(a))+".csv",encoding=enc,index=False)
                shutil.make_archive(format="zip",root_dir=arc.filename+"_A",base_name=arc.filename+"_A_"+str(len(a)))
                a=[]

                for h in bc:
                    arc.extract(h,path=arc.filename+"_BC")
                with open(arc.filename+"_BC_"+str(len(bc))+".csv","w") as y:
                    csv.writer(y).writerow(["filename_bc"])
                    for x in bc:
                        csv.writer(y).writerow([x])
                pd.read_csv(arc.filename+"_BC_"+str(len(bc))+".csv",encoding=enc).to_csv(arc.filename+"_BC_"+str(len(bc))+".csv",encoding=enc,index=False)
                shutil.make_archive(format="zip",root_dir=arc.filename+"_BC",base_name=arc.filename+"_BC_"+str(len(bc)))
                bc=[]

                for h in shoulder:
                    arc.extract(h,path=arc.filename+"_SHOULDER")
                with open(arc.filename+"_SHOULDER_"+str(len(shoulder))+".csv","w") as y:
                    csv.writer(y).writerow(["filename_shoulder"])
                    for x in shoulder:
                        csv.writer(y).writerow([x])
                pd.read_csv(arc.filename+"_SHOULDER_"+str(len(shoulder))+".csv",encoding=enc).to_csv(arc.filename+"_SHOULDER_"+str(len(shoulder))+".csv",encoding=enc,index=False)
                shutil.make_archive(format="zip",root_dir=arc.filename+"_SHOULDER",base_name=arc.filename+"_SHOULDER_"+str(len(shoulder)))
                shoulder=[]

shutil.unpack_archive makes folder.arcfilename as root
 a=[arc.infolist()[x] for x in range(len(arc.infolist())) if arc.infolist()[x].file_size==0]

any(x for x )

ifError(regExtract(b10,"\d+.csv"),"checkRefParam")

def brandnewListfile(p="",fo)

files,filesBad=[],[]
arc=ZipFile("zipfile.zip","r").infolist()
for z in range(len(arc)):
	if r".jp" in arc[z].filename:
		if arc[z].file_size!=0:
			files[len(files):]=[arc[z].filename]
		else:
			filesBad[len(filesBad):]=[arc[z].filename]
	else:
		continue
print(files)

0. create filelists from each archives
1. concatenate jpg filelists from done
2. load filenames from result jsonfile
3. load filenames to each typeValue-named lists 
4. zipfile.extract returns fullpath of each object in zipfile
5. os.rename()
6. arcname=abs path of arcfile
0. concatenate items in every keys
1. for z in arcil:if z not in items:ZipFile.extract


0. create filelist per archives
1. get list of per-condition filepath
2. unzip by per-condition filepath one by one (using arc.extractall with iterable members)
3. zip unzipped files



f=[]
f=
f=[e[z] for z in e.keys()]

f.update(y for y in [e[z] for z in e.keys()])

y for x in [test_list1, test_list2] for y in x]

f=[]
for z in e.keys():
    f+=e[z]
   



get fullpath of each arcfile
replace fullpath
e:\\82\\done\\chasu

e:\\82\\extracted\\str(z)\\chasu\\
e:\82\done\IMAGE\B\BLUE\[00084]B_BLUE\[BLUE]00084B_100912_005.jpg
foFromArc
foFromArc.replace("e:\\82\\done\\",(arcDirPath.replace("\\done\\","\\done\\"+str(z))))

arcDirPath
arc.filename
get fullpath of archives

[x for x in list if pred(x)]
[x for x in arcil if x 

list(arcinfolist[z].filename for z in range(len(arcinfolist)) if ".zip" in arcinfolist[z].filename)

list(arcname for arcname in arcfile
list(map(os.path.realpath,z)
arcnamepath[len(arcnamepath):]=[(os.path.realpath(z) for z in arcfile)]

il=list(arc.infolist()[x].filename for x in range(len(arc.infolist())) if ".jpg" in arc.infolist()[x].filename)

test={}
for x in range(len(jsonfile["result"])):
    if len(jsonfile["result"][x])>3:
        test=[x for x in jsonfile["result"][x]["data"][0]["value"][0]["value"]]
    else:
        continue




드라이버, 건전지

detectA	detectBC	detectS
typeAB	typeAB	typeA

normalA	normalBC	normalS
typeABCD	typeABCD	typeABC

fuck=pd.DataFrame()

for u in range(len(fuck.index)):
    if str(fuck.iloc[u,1])==


dano="json"
def pkr_drop(a):#removes 360> from pkr_rawdata
    a=pd.read_csv(a,encoding=enc,usecols=(1,3,5,7,8,9))
    a=a[~a["email"].isin(a["email"].value_counts()[a["email"].value_counts()<360].index)]
    a=a.set_index("email")
    a.to_csv("pkr_dropped_"+ima+".csv",encoding=enc)
#pkr_drop("4df.csv")



atc0=to_csv("fuck.csv",encoding="utf-8-sig",index=False)



def pig(a):
  return 2 * a + 2
target = range(5)
result = map(pig,targe
print(list(result))

def fuck(a):
    return a + 10
target = range()

a=pd.DataFrame()
a=[a["email"].drop(a["email"]==x) for x in a["email"].value_counts()<360==True]

a=str(ybg[str(y)]["1"]["_id"])+"-"+str(uuid.uuid1())+str(uuid.uuid4())+"-"+str(uuid.uuid4().hex)+str(uuid.uuid1())
b=str(uuid.uuid3(uuid.NAMESPACE_DNS,str(ybg[str(y)]["1"]["_id"])))+str(uuid.uuid5(uuid.NAMESPACE_DNS,str(ybg[str(y)]["1"]["_id"])))
c=str(uuid.uuid5(uuid.NAMESPACE_URL,str(ybg[str(y)]["1"]["phone_number"])))+str(uuid.uuid5(uuid.NAMESPACE_URL,str(ybg[str(y)]["1"]["_id"])))
ybg[str(y)]["1"]["_id"]=(((a+b+c)*3+((a+c).replace("a","f0a").replace("0","5a09").replace("1","02a01fac").replace("01","a0ccb"))+((c*2).replace("c","-c00a").replace("1","1ccd0"))+a+b)*4).replace("a","bb").replace("b","ac")
ybg[str(y)]["0"]=(((a+b+c)*3+((a+c).replace("a","f0a").replace("0","5a09").replace("1","02a01fcac").replace("01","a0ccfb"))+((c*2).replace("c","-ac-0f---0a").replace("1","1f-cc-cd0"))+a)*8).replace("b","06a").replace("0","010")

    #for y,x,z in range(height,width):
        #r=np.ndarray(())
    #for y,x in range(height,width):
        #for z in range(blockSize):
            #r=memo(img[y][x][0]/blockSize+img[y][x+1][0]/blockSize+img[y][x+2][0]/blockSize)
            #x,z=x+blockSize,z+blockSize
            #block[y][x]
            #a=a+np.unit8(r)

def classified(fo,p="D:\\aihub82"):
    os.chdir(p)
    arc,arcFilelist=ZipFile(fo,"r"),[]
    
    jpgfile=[]
    for z in arc.namelist():
        if ".jpg" in z:
            jpgfile[len(jpgfile):]=[z]
    jpgfileNumber=len(jpgfile)

    shoulder=[]
    for z in jpgfile:
        if "[SHOULDER]" in z:
            shoulder[len(shoulder):]=[z]
    listfileNameShoulder=str(fo)+"_SHOULDER_"+str(len(shoulder))+".csv"
    with open(listfileNameShoulder,"w",encoding=enc) as a:
        csv.writer(a).writerow(["filename_shoulder"])
        for x in shoulder:
            csv.writer(a).writerow([x])
    pd.read_csv(listfileNameShoulder,encoding=enc).to_csv(listfileNameShoulder,encoding=enc,index=False)

    channela=[]
    for z in jpgfile:
        if "A_BLUE" in z:
            channela[len(channela):]=[z]
        if "A_WHITE" in z:
            channela[len(channela):]=[z]
        if "A_YELLOW" in z:
            channela[len(channela):]=[z]
    listfileNameA=str(fo)+"_A_"+str(len(channela))+".csv"
    with open(listfileNameA,"w",encoding=enc) as a:
        csv.writer(a).writerow(["filename_a"])
        for z in channela:
                csv.writer(a).writerow([z])
    pd.read_csv(listfileNameA,encoding=enc).to_csv(listfileNameA,encoding=enc,index=False)

    channelbc=[]
    for z in jpgfile:
        if "B_BLUE" in z:
            channelbc[len(channelbc):]=[z]
        if "B_WHITE" in z:
            channelbc[len(channelbc):]=[z]
        if "B_YELLOW" in z:
            channelbc[len(channelbc):]=[z]
        if "C_BLUE" in z:
            channelbc[len(channelbc):]=[z]
        if "C_WHITE" in z:
            channelbc[len(channelbc):]=[z]
        if "C_YELLOW" in z:
            channelbc[len(channelbc):]=[z]
    listfileNameBC=str(fo)+"_BC_"+str(len(channelbc))+".csv"
    with open(listfileNameBC,"w",encoding=enc) as a:
        csv.writer(a).writerow(["filename_bc"])
        for z in channelbc:
                csv.writer(a).writerow([z])
    pd.read_csv(listfileNameBC,encoding=enc).to_csv(listfileNameBC,encoding=enc,index=False)
    return print("..done: jpgfileNumber: "+str(jpgfileNumber))
#classified(fo="20211129_DETECT_11535.zip",p="E:\\82\\target\\28차_DETECT_62039\\20211129_DETECT_11535")