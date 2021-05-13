import os
import shutil

target_path='C:/Users/user/NTU Graduate/肩部原始data/Archive_new data2017/201701-06/MBR_2017_03_shoulder_FILES_MBR/No Calcification/Long Ax/with label/'

img_path='C:/Users/user/NTU Graduate/research/1205label_test/'

img_files=os.listdir(img_path)
target_files=os.listdir(target_path)

for i in range(len(target_files)):
    oldname=target_path+target_files[i]
    #print('oldname=',oldname)
    #print(target_files[i])
    newname=img_path+'201703-'+target_files[i]
    #print(newname)
    shutil.copyfile(oldname,newname)
    #if target_files[i][-5]=='0':
        #newname=target_path+'No TB_'+target_files[i]
        #newplacename=target_path+'201701-C'+img_files[i].replace('JPG','jpg')
    #else:
     #   newname=target_path+'TB_'+target_files[i]
    #print('newname=',newname)
    #shutil.copyfile(oldname,newplacename)
    #os.rename(oldname, newname)


