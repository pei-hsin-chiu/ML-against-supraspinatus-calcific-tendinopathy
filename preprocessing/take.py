import os
import random
import shutil

###short valid###
short_calcification_path='C:/Users/user/Desktop/0622/valid/short calcification/'
short_calcification_files=os.listdir(short_calcification_path)
short_no_calcification_path='C:/Users/user/Desktop/0622/valid/short no calcification/'
short_no_calcification_files=os.listdir(short_no_calcification_path)

##calcification##
##test#
test_target_path='C:/Users/user/Desktop/0622test/'
test_amount=10
test_choice = random.sample(short_calcification_files, test_amount)

for i in range(test_amount):
    oldname=short_calcification_path+test_choice[i]
    #print('oldname=',oldname)
    newplacename=test_target_path+test_choice[i]
    shutil.copyfile(oldname,newplacename)
    os.remove(oldname)
for index in range(test_amount):
    short_calcification_files.remove(test_choice[index])

##no calcification##
##test#
test_target_path='C:/Users/user/Desktop/0622test/'
test_amount=10
test_choice = random.sample(short_no_calcification_files, test_amount)

for i in range(test_amount):
    oldname=short_no_calcification_path+test_choice[i]
    #print('oldname=',oldname)
    newplacename=test_target_path+test_choice[i]
    shutil.copyfile(oldname,newplacename)
    os.remove(oldname)
for index in range(test_amount):
    short_no_calcification_files.remove(test_choice[index])
    

"""
###long valid###
long_calcification_path='C:/Users/user/Desktop/長軸 780-3541/calcification/'
long_calcification_files=os.listdir(long_calcification_path)
long_no_calcification_path='C:/Users/user/Desktop/長軸 780-3541/no calcification/'
long_no_calcification_files=os.listdir(long_no_calcification_path)


##calcification##
##train##
train_target_path='C:/Users/user/Desktop/0622-long/train/calcification/'
train_amount=600
train_choice = random.sample(long_calcification_files, train_amount)

for i in range(train_amount):
    oldname=long_calcification_path+train_choice[i]
    #print('oldname=',oldname)
    newplacename=train_target_path+train_choice[i]
    shutil.copyfile(oldname,newplacename)
for index in range(train_amount):
    long_calcification_files.remove(train_choice[index])

##valid##
valid_target_path='C:/Users/user/Desktop/0622-long/valid/calcification/'
valid_amount=50
valid_choice = random.sample(long_calcification_files, valid_amount)

for i in range(valid_amount):
    oldname=long_calcification_path+valid_choice[i]
    #print('oldname=',oldname)
    newplacename=valid_target_path+valid_choice[i]
    shutil.copyfile(oldname,newplacename)
for index in range(valid_amount):
    long_calcification_files.remove(valid_choice[index])
    
##test#
test_target_path='C:/Users/user/Desktop/0622-long-test/'
test_amount=80
test_choice = random.sample(long_calcification_files, test_amount)

for i in range(test_amount):
    oldname=long_calcification_path+test_choice[i]
    #print('oldname=',oldname)
    newplacename=test_target_path+test_choice[i]
    shutil.copyfile(oldname,newplacename)
for index in range(test_amount):
    long_calcification_files.remove(test_choice[index])

##no calcification##
##train##
train_target_path='C:/Users/user/Desktop/0622-long/train/no calcification/'
train_amount=600
train_choice = random.sample(long_no_calcification_files, train_amount)

for i in range(train_amount):
    oldname=long_no_calcification_path+train_choice[i]
    #print('oldname=',oldname)
    newplacename=train_target_path+train_choice[i]
    shutil.copyfile(oldname,newplacename)
for index in range(train_amount):
    long_no_calcification_files.remove(train_choice[index])
    
##valid##
valid_target_path='C:/Users/user/Desktop/0622-long/valid/no calcification/'
valid_amount=50
valid_choice = random.sample(long_no_calcification_files, valid_amount)

for i in range(valid_amount):
    oldname=long_no_calcification_path+valid_choice[i]
    #print('oldname=',oldname)
    newplacename=valid_target_path+valid_choice[i]
    shutil.copyfile(oldname,newplacename)
for index in range(valid_amount):
    long_no_calcification_files.remove(valid_choice[index])
##test#
test_target_path='C:/Users/user/Desktop/0622-long-test/'
test_amount=80
test_choice = random.sample(long_no_calcification_files, test_amount)

for i in range(test_amount):
    oldname=long_no_calcification_path+test_choice[i]
    #print('oldname=',oldname)
    newplacename=test_target_path+test_choice[i]
    shutil.copyfile(oldname,newplacename)
for index in range(test_amount):
    long_no_calcification_files.remove(test_choice[index])
    """