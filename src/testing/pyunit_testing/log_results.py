## write the results to a file 


def record(test_name, test_input, test_output, test_result):
	try:
		with open("testResults.txt","a") as outputFile:
			result = "{} {} {} RESULT: {}\n".format(test_name, test_input, test_output, test_result)
			outputFile.write(result) 
		return "Success!"
	except:
		return "Failure" 
	
