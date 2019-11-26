# Quectel BG96 GNSS plotter

Pair of scripts for plotting the GNSS results of the BG96.


Instructions:
1) adjust the settings at bg96-gps.py (COM port, baudrate)
2) connect the BG96 to the selected COM port, and turn it on
3) run the bg96-gps.py script, and capture the output into a text file
       	python bg96-gps.py > capture.log
4) drive, walk, stay quite, whatever, while the unit captures data
5) finish the data capture with Ctrl+C
6) run the bg96-gps-plotter.py script, using the capture text file as input
		python bg96-gps-plotter.py < capture.log
7) a new file should be generated, "map.html", with the movement path.


