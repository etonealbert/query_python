from query import *

if __name__ == '__main__':
	response = elastic_match_query( query = "university",
				index = "merged")
	print(response)
