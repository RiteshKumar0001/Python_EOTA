
################################################    Program to get Rf and Non-RF Joins for all the nodes  ################################################



##################       opening file to read data      ##################


f=open('EOTA_health_report_2013-10-04_demo.txt', 'r')
file_data=f.readlines()

#################     Get the Number of nodes seding UL DL data       #######################	


def getLiveNodesNum():
	strtcount=0
	temp_line=""
	target_line=[]
	for line in file_data:
		start_point=line.find("Total Number of Nodes sending UL/DL traffic")
		if(start_point!=-1):
			temp_line=line
			break
	target_line=temp_line.split()
	return int(target_line[-1])
	

#################     Get the line number for first entry in the table       #######################	

	
def getTargetLineNumber():
	start_point=0
	strtcount=0
	for line in file_data:
		start_point=line.find("Node Exit Reason UI AP Description")
		if(start_point!=-1):
			strtcount=file_data.index(line)
			break
		strtcount=strtcount+1
	return strtcount+1

##################   Get the node name and respective RF and Non-RF join type in the list   #################

	
def get_data():
	lineNumber=getTargetLineNumber()
	RF_non_RF=[]
	entry=[]
	count=0
	inc=0
	for line in file_data:
		if (count<lineNumber):
			count=count+1
		else:
			temp_data=file_data[lineNumber+inc]
			data=temp_data.split()
			entry.append([data[0], data[2]+data[3]+data[4]])
			count=count+1
			inc=inc+1	
				
	RF_non_RF=entry
	return RF_non_RF
	
	
##################   Sorting RF and Non-RF join type in the list   #################
	
	
def temp_data():
	RF_data=[]
	nonRF_data=[]
	RF_non_RF=get_data()	
	for element in RF_non_RF:
		if (element[1]=="PhyTrackingFail" or element[1]=="MacConsecBCH0" or element[1]=="ApMetricsEvery"):
			RF_data.append(element)
		else:
			nonRF_data.append(element)
	return RF_data, nonRF_data

	
##################   Counting nodes for  RF and Non-RF join type in the list   #################

	
def final_data():
	flag=False
	flag1=False
	RF_data,nonRF_data=temp_data()
	RF_count=[]
	nonRF_count=[]
	
	while RF_data!=[]:
		temp=RF_data.pop()
		for element in RF_count:
			if element==temp[0]:
				flag=True
				break
			flag=False
				
		if flag==False:
			RF_count.append(temp[0])
			
			
	while nonRF_data!=[]:
		temp1=nonRF_data.pop()
		if temp1[0]=="Node" :
			continue
		for element in nonRF_count:
			if element==temp1[0]:
				flag1=True
				break
			flag1=False
				
		if flag1==False:
			nonRF_count.append(temp1[0])		
			
	print ("Numnber of nodes with RF Join type:  "  + str(len(RF_count))) 			
	print ("Number of nodes with Non- RF Join type:  " + str(len(nonRF_count)))
	print ("RF Joins: " + str(len(RF_count)/getLiveNodesNum()))
	print ("Non-RF Joins: " + str(len(nonRF_count)/getLiveNodesNum()))
	
f.close()	