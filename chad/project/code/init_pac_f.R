library(R.matlab)
library(doSNOW)
library(foreach)

# runs job in parallel
parallel <- T
if (parallel)
{
  cl<-makeCluster(4) #change the 2 to your number of CPU cores
  registerDoSNOW(cl)
  # gets the job to run 2-way parallel
  
}

setwd("/Users/chadleonard/Repos/DAT3_project/data/Dog_1/crossval_dir/") #!!! set path to your data !!!!
# setwd("/Users/chadleonard/Repos/DAT3_project/data/Dog_1/crossval_dir/")
num <- 24  # Why 24? 
part<-0.03
part1000<-round(part*1000)

chars <- function(data,pref) # need to understand this function. "pref" are the column names
{
  sg <- abs(fft(data))
  # getting absolute value fft for all the data in a channel (column)...
  sg <- sg[1:(part*length(sg))]
  # this is only taking 3% of the records .. that'sabout 7192 of 239766 records.
  ln=length(sg)
  # ln equals about 7192 records
  df<-aggregate(sg,by = list(trunc(num*((1:ln)-1)/ln)),FUN=mean)
  # It's taking 300 values at a time and finding their mean. 
  # This creates 24 versions of each field. 
  # i.e. NVC1202_32_002_Ecog_c001_f1 to NVC1202_32_002_Ecog_c001_f24
  # ((1:ln)-1) is returning the integers from 0 to 7191 (ln)...
  #num*((1:ln)-1) / ln ==> multiplies the integers from 0 to ln by 24 then divides by ln...
  # trun(num*((1:ln)-1)/ln)) round the numbers off... 
  # creates a list of integers 0 to 24 there are about 300 of each number i.e. 300 0s.
  # still don't understand what this is doing...
  df=data.frame(t(df))
  
  # names(df) <- paste(pref,paste("f",1:num,sep=""),sep="_")
  names(df) <- paste(substr(pref,7, 30 ),paste("f",1:num,sep=""),sep="_")
  
  # renames columns to things like  'list("NVC1202_32_002_Ecog_c001")_f1' 
  df["x",]
}

#sub_folders <- c("Patient_2", "Patient_1", "Dog_3", "Dog_4", "Dog_2", "Dog_1",  "Dog_5")
sub_folders <- c("test_dir")
# 
files <- function(sub_folder) # grabs all the files in the sub_folder..
{
  print(sub_folder)
  all_list <- NULL
  orig_file <- list.files(path=sub_folder)
  # list.files(path="Dog_1")
  # sub_folder="cv_0"
  file <- paste(sub_folder,orig_file,sep="/")
  print(file)
  all_list <- rbind(all_list,data.frame(file=file,orig_file=orig_file))
  # This creates the "file", "orig_file list
  print(sub_folder); flush.console()
  all_list[,"type"]<-unlist(lapply(as.character(all_list[,1]),function(x) strsplit(x,split="_")[[1]][4] ))
  # This adds "type" to the "file", "orig_file list
  all_list
}
# print("before foreach")
foreach (sub_folder = sub_folders, .packages=c("R.matlab")) %dopar% {
  # reading through the sub folder(s)  getting all the names of the files therein...
  print(sub_folder)
  fls <- files(sub_folder)
  cnt <- nrow(fls)
  # getting the cnt of the number of files in the folder.
  all_char_list <- NULL
  file <- fls[1,"file"]
  data <- readMat(file)[[1]]
  # I believe this is just taking the first record to get the columns.... [[1]] are the column names (I think)
  # for readMat need to make sure there are no files other than .mat files in the directory.
  channels <- as.character(data[[4]]) # channels
#}
# looping through the 84 .mat files.
  for (i in 1:cnt)
  {
    file <- fls[i,"file"]
    data <- readMat(file)[[1]]
    print("in foreach line 58")
    print(paste(file,":", i,"of",cnt)); flush.console()

    char_list <- chars(data[[1]][1,],channels[1])
    # data[[1]][1,] is getting the data values for the first channel. channels[1] is the first channel...
    # channel 1 and the data for channel 1 are passed to the chars() function...
    for (i2 in 2:length(channels))
      char_list <- cbind(char_list, chars(data[[1]][i2,],channels[i2]))
    # the rest of the data for the rest of the channels and the rest of the channel names are passed to the chars() function
  
    # adds "latency" not sure what that is... filename ("orig_file"), "type", "freq", and "sec" to each record...
    # one record represents one .mat file. 
    char_list[,"latency"] <- ifelse(length(data)==4,-1,data[[5]]) 
    char_list[,"orig_file"] <- fls[i,"orig_file"]
    char_list[,'type'] <- fls[i,"type"]
    char_list[,'freq'] <- data[[3]]
    char_list[,'sec'] <- data[[2]]
    char_list[,"ictal_ind"] <- ifelse(fls[i,"type"] == 'preictal', 1, 0)
    
    all_char_list <- rbind(all_char_list,char_list)
  }
  write.csv(all_char_list, paste(sub_folder,paste("csv",num,part1000,sep="_"),sep="."),row.names=F,quote=F)
}
# 
if (parallel)
{
  stopCluster(cl)
  rm(cl)
}
