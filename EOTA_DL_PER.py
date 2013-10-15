
################################################    Program to get DL PER count for all the nodes  ################################################



##################       opening file to read data      ##################

f=open('EOTA_health_report_2013-10-04_demo.txt', 'r')
file_data=f.readlines()


#################     Get the line number for first entry in the table       #######################	
	

def getTargetLineNumber_DL():
	start_point=0
	strtcount=0
	for line in file_data:
		start_point=line.find("Nodes with High Average DL PER ( above 10 )")
		if(start_point!=-1):
			strtcount=file_data.index(line)
			break
		strtcount=strtcount+1
	print ("start point is : " +str(strtcount+3))
	return strtcount+3


#################      Get the line number for last entry in the Table       #########################

def endPoint_DL():
	end_point=0
	endcount=0
	for line in file_data:
		end_point=line.find("Summary of DL SDU Stats")
		if(end_point!=-1):
			endcount=file_data.index(line)
			break
		endcount=endcount+1
	endcount=endcount
	return endcount	
	

##################   Get the node name and respective UL PER data in the list   #################
	
		
def get_data_DL():
	lineNumber=getTargetLineNumber_DL()
	#print (lineNumber)
	node_DL_PER_value=[]
	entry=[]
	count=0
	inc=0
	end_count=int(endPoint_DL())
	#print ("end count value is: " + str(end_count) )
	for line in file_data:
		if (count<lineNumber):
			count=count+1
		else:	
			if(count<end_count):
				temp_data=file_data[lineNumber+inc]
				data=temp_data.split()
				entry.append([data[0], data[5]])
				count=count+1
				inc=inc+1
	node_DL_PER_value=entry
	return node_DL_PER_value
	

###################   Final  Function to give the expected result    ####################
	
	
def final_data_DL():
	data_list=get_data_DL()	
	grtThanTen=0
	grtThanTwenty=0
	grtThanThirty=0
	grtThanForty=0
	
	last_data=[]
	for entry in data_list:
		temnode=entry[1]			
		last_data.append(temnode)
		
	for entry in last_data:
		if float(entry)>=10:
			grtThanTen=grtThanTen+1
		if float(entry)>=20:
			grtThanTwenty=grtThanTwenty+1
		if float(entry)>=30:
			grtThanThirty=grtThanThirty+1
		if float(entry)>=40:
			grtThanForty=grtThanForty+1
	print ("############")
	print(" ")
	print ("NodeCount for nodes having DL PER greater than 10 :  " +  str(grtThanTen))
	print ("NodeCount for nodes having DL PER greater than 20 :  " +  str(grtThanTwenty))
	print ("NodeCount for nodes having DL PER greater than 30 :  " +  str(grtThanThirty))
	print ("NodeCount for nodes having DL PER greater than 40 :  " +  str(grtThanForty))
	print (" ")
	print ("############")	
	
	
#final_data_DL()
f.close()
#done=input("Hit ENTER to exit")


######################    End of Program    ###########################
