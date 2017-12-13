# Usage of pytools

## choseLeader.py
The script is used to calculate the probility of leader chosing in the first step of MSIG protocol.
The choseLeader  script have three input parameters:
* The first parameter "--plot" is used to decide whether the program will draw the plot or not
* The second parameter is the number of faulty nodes in the system
* The third parameter is the total number of nodes in the system
#### Example
	chmod +x choseLeader.py
	#./choseLeader paramer1 int int
	./choseLeader --plot 3 10
