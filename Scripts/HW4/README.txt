Elias Muche 
11/17/16
CSS-390: HW4


Special Notes: 
	-runScripts is an uberscript that runs part 1 for each type of link simultaneously. It also runs part 2 simulataneously
	-part 1's --dur should be the same as part 2's --dur

Part 1:
	-Associated Files:
		-trafficgen.py

	-Assumptions: 
		-timeserver.py is running

	-Arguments:
		--url, the url desired 
		--rps, number of requests per second
		--jitter, the number used to calculate the offset of rps
		--dur the desired duration for which you want the program to run

Part 2:
	-Associated Files:
		-collector.py
		-data.tsv

	-Assumptions: 
		-timeserver.py is running

	-Arguments
		--url, the url of the stats page
		--interval, the interval for which you want to collect data 
		--dur, the desired duration for which you want the program to run		

Part 3:
	-Associated Files:
		-processData.py 
		-makeGraph.gnu
		-alteredData.tsv
		-output.png

	-Assumptions:
		-the scripts from part 1 and part 2 will be finished runnning before you run the part 3 script
		-there will be a filled tsv file to read from

	-Running Part 3:
		-bash runPart3.sh

	