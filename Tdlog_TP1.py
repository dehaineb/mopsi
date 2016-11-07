groups = {
    1: { "Den", "Eng", "France",      "Sweden" },
    2: { "CIS",     "Germany", "Netherlands", "Scotland" }
}

matches = [
    ("Sweden",      1, 1, "France"),
    ("Denmark",     0, 0, "England"),
    ("Netherlands", 1, 0, "Scotland"),
    ("CIS",         1, 1, "Germany"),
    ("France",      0, 0, "England"),
    ("Sweden",      1, 0, "Denmark"),
]


#affichage du classement
for i in range(1,len(groups)+1):
	print("")
	print("Group "+str(i))
	print("-------")
	classement={pays:[0,0,0] for pays in groups[i]}
	nombrecaractèremax=0
	for pays in groups[i]:	
		if(len(pays)>nombrecaractèremax):
			nombrecaractèremax=len(pays)
		for k in range(len(matches)):
			if (pays in matches[k]):
				if (matches[k][1]==matches[k][2]):
					classement[pays][0]+=1;
					classement[pays][2]+=matches[k][1];

				elif(pays==matches[k][0] and matches[k][1]>matches[k][2]):
					classement[pays][0]+=2;
					classement[pays][1]+=matches[k][1]-matches[k][2]
					classement[matches[k][3]][1]-=matches[k][1]-matches[k][2]
					classement[pays][2]+=matches[k][1];
					classement[matches[k][3]][2]+=matches[k][2]

				elif(pays==matches[k][3] and matches[k][2]>matches[k][1]):
					classement[pays][0]+=2;
					classement[pays][1]+=matches[k][2]-matches[k][1]
					classement[matches[k][3]][1]-=matches[k][2]-matches[k][1]
					classement[pays][2]+=matches[k][2];
					classement[matches[k][3]][2]+=matches[k][1]

	
	classementfinal={i:"" for i in range(1,len(groups[i])+1)}
	egalite={pays:0 for pays in groups[i]}
	for pays1 in groups[i]:
		a=1;
		for pays2 in groups[i]:
			if pays2!=pays1:
				if (classement[pays1][0]<classement[pays2][0]):
					a=a+1
				if ((classement[pays1][0]==classement[pays2][0]) and (classement[pays1][1]<classement[pays2][1])):
					a=a+1
				if((classement[pays1][0]==classement[pays2][0]) and (classement[pays1][1]==classement[pays2][1]) and (classement[pays1][2]<classement[pays2][2])):
					a=a+1
				if((classement[pays1][0]==classement[pays2][0]) and (classement[pays1][1]==classement[pays2][1]) and (classement[pays1][2]==classement[pays2][2]) and pays1!=pays2):
					a=a+egalite[pays1]
					egalite[pays1]+=1
					egalite[pays2]+=1
		classementfinal[a]=pays1;			

	
	for k in range(1,len(groups[i])+1):
		if(classement[classementfinal[k]][1]>=0):
			print(classementfinal[k]+"."*(3+nombrecaractèremax-len(classementfinal[k]))+" "+ str(classement[classementfinal[k]][0])+" pts "+ "+" +str(classement[classementfinal[k]][1]))
		else:
			print(classementfinal[k]+"."*(3+nombrecaractèremax-len(classementfinal[k]))+" "+ str(classement[classementfinal[k]][0])+" pts " +str(classement[classementfinal[k]][1]))

	print(" ")

	for k in range(len(matches)):	
		if(matches[k][0] in groups[i]):
			print(matches[k][0]+" "*(nombrecaractèremax+2-len(matches[k][0]))+ str(matches[k][1])+" - " + str(matches[k][2])+"  " +matches[k][3])
	
	print("")

	
	doublon=[]
	for pays1 in groups[i]:
		for pays2 in groups[i]:
			matchavenir=True
			for k in range(len(matches)):
				if((pays1 in matches[k]) and (pays2 in matches[k])):
					matchavenir=False
			if (matchavenir and {pays1,pays2} not in doublon):
				print(pays1+" "*(nombrecaractèremax+2-len(pays1))+"vs  "+pays2)
				doublon+=[{pays1,pays2}]
				

	








