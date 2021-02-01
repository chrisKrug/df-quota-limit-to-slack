import os,subprocess

dfResults = subprocess.check_output('df')
dfList =  dfResults.split('\n')
for fsInstance in dfList:
	if 'netapp-dataserver' in fsInstance:
		fsList = fsInstance.split()
		fs = fsList[0]
		percent = int(fsList[4][:-1])
		#print fsList
		if percent>80:
			message = "The "+fs+" filesystem is at "+str(percent)+"% of its quota."
			os.system("""curl -X POST -H 'Content-type: application/json' --data '{"text":" """+message+""" "}' https://hooks.slack.com/services/x/xx""")
			print message
