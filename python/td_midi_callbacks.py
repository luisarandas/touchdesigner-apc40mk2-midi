

# luis arandas 03-06-2023
# links akai apc40mk2 midi codes through DAT (Text) execute

def onReceiveMIDI(dat, rowIndex, message, channel, index, value, input, bytes):

	# print("dat = ", dat)
	# print("rowIndex = ", rowIndex)
	# print("message = ", message)
	# print("channel = ", channel)
	# print("index = ", index)
	# print("value = ", value)
	# print("input = ", input)
	# print("bytes = ", bytes)

	# top row, fixed knobs

	if channel == 1 and index == 49 and message == "Control Change":
		print("knob 1 -> ", value)
	
	if channel == 1 and index == 50 and message == "Control Change":
		print("knob 2 -> ", value)

	if channel == 1 and index == 51 and message == "Control Change":
		print("knob 3 -> ", value)

	if channel == 1 and index == 52 and message == "Control Change":
		print("knob 4 -> ", value)

	if channel == 1 and index == 53 and message == "Control Change":
		print("knob 5 -> ", value)
	
	if channel == 1 and index == 54 and message == "Control Change":
		print("knob 6 -> ", value)

	if channel == 1 and index == 55 and message == "Control Change":
		print("knob 7 -> ", value)

	if channel == 1 and index == 56 and message == "Control Change":
		print("knob 8 -> ", value)


	# ------------------------------
	# channel 1 static

	if channel == 1 and index == 33 and message == "Note On":
		print("pad 1 -> ", value)

	if channel == 1 and index == 25 and message == "Note On":
		print("pad 2 -> ", value)
	
	if channel == 1 and index == 17 and message == "Note On":
		print("pad 3 -> ", value)
	
	if channel == 1 and index == 9 and message == "Note On":
		print("pad 4 -> ", value)
	
	if channel == 1 and index == 1 and message == "Note On":
		print("pad 5 -> ", value)

	if channel == 1 and index == 53 and message == "Note On":
		print("pad 6 -> ", value)
	
	# selectors untriggered, will print knob panel state

	# if channel == 1 and index == 24 and message == "Control Change":
	#	print("selector 1 -> ", value)
	
	if channel == 1 and index == 51 and message == "Note On":
		print("pad 7 -> ", value)

	if channel == 1 and index == 67 and message == "Note On":
		print("pad 8 -> ", value)

	if channel == 1 and index == 50 and message == "Note On":
		print("pad 9 -> ", value)
	
	if channel == 1 and index == 49 and message == "Note On":
		print("pad 10 -> ", value)
	
	# ------------------------------
	# channel 2 static

	if channel == 1 and index == 34 and message == "Note On":
		print("pad 11 -> ", value)

	if channel == 1 and index == 26 and message == "Note On":
		print("pad 12 -> ", value)
	
	if channel == 1 and index == 18 and message == "Note On":
		print("pad 13 -> ", value)
	
	if channel == 1 and index == 10 and message == "Note On":
		print("pad 14 -> ", value)
	
	if channel == 1 and index == 2 and message == "Note On":
		print("pad 15 -> ", value)

	if channel == 2 and index == 53 and message == "Note On":
		print("pad 16 -> ", value)

	# selectors untriggered, will print knob panel state

	# if channel == 2 and index == 24 and message == "Control Change":
	#	print("selector 2 -> ", value)
	
	if channel == 2 and index == 51 and message == "Note On":
		print("pad 17 -> ", value)
	
	if channel == 2 and index == 67 and message == "Note On":
		print("pad 18 -> ", value)

	if channel == 2 and index == 50 and message == "Note On":
		print("pad 19 -> ", value)
	
	if channel == 2 and index == 49 and message == "Note On":
		print("pad 20 -> ", value)
	
	# ------------------------------
	# channel 3 static

	if channel == 1 and index == 35 and message == "Note On":
		print("pad 21 -> ", value)

	if channel == 1 and index == 27 and message == "Note On":
		print("pad 22 -> ", value)
	
	if channel == 1 and index == 19 and message == "Note On":
		print("pad 23 -> ", value)
	
	if channel == 1 and index == 11 and message == "Note On":
		print("pad 24 -> ", value)
	
	if channel == 1 and index == 3 and message == "Note On":
		print("pad 25 -> ", value)

	if channel == 3 and index == 53 and message == "Note On":
		print("pad 26 -> ", value)

	# selectors untriggered, will print knob panel state

	# if channel == 3 and index == 24 and message == "Control Change":
	#	print("selector 3 -> ", value)
	
	if channel == 3 and index == 51 and message == "Note On":
		print("pad 27 -> ", value)
	
	if channel == 3 and index == 67 and message == "Note On":
		print("pad 28 -> ", value)

	if channel == 3 and index == 50 and message == "Note On":
		print("pad 29 -> ", value)
	
	if channel == 3 and index == 49 and message == "Note On":
		print("pad 30 -> ", value)

	# ------------------------------
	# channel 4 static

	if channel == 1 and index == 36 and message == "Note On":
		print("pad 31 -> ", value)

	if channel == 1 and index == 28 and message == "Note On":
		print("pad 32 -> ", value)
	
	if channel == 1 and index == 20 and message == "Note On":
		print("pad 33 -> ", value)
	
	if channel == 1 and index == 12 and message == "Note On":
		print("pad 34 -> ", value)
	
	if channel == 1 and index == 4 and message == "Note On":
		print("pad 35 -> ", value)

	if channel == 4 and index == 53 and message == "Note On":
		print("pad 36 -> ", value)

	# selectors untriggered, will print knob panel state

	# if channel == 4 and index == 24 and message == "Control Change":
	#	print("selector 4 -> ", value)
	
	if channel == 4 and index == 51 and message == "Note On":
		print("pad 37 -> ", value)
	
	if channel == 4 and index == 67 and message == "Note On":
		print("pad 38 -> ", value)

	if channel == 4 and index == 50 and message == "Note On":
		print("pad 39 -> ", value)
	
	if channel == 4 and index == 49 and message == "Note On":
		print("pad 40 -> ", value)
	
	# ------------------------------
	# channel 5 static

	if channel == 1 and index == 37 and message == "Note On":
		print("pad 41 -> ", value)

	if channel == 1 and index == 29 and message == "Note On":
		print("pad 42 -> ", value)
	
	if channel == 1 and index == 21 and message == "Note On":
		print("pad 43 -> ", value)
	
	if channel == 1 and index == 13 and message == "Note On":
		print("pad 44 -> ", value)
	
	if channel == 1 and index == 5 and message == "Note On":
		print("pad 45 -> ", value)

	if channel == 5 and index == 53 and message == "Note On":
		print("pad 46 -> ", value)

	# selectors untriggered, will print knob panel state

	# if channel == 5 and index == 24 and message == "Control Change":
	#	print("selector 5 -> ", value)
	
	if channel == 5 and index == 51 and message == "Note On":
		print("pad 47 -> ", value)
	
	if channel == 5 and index == 67 and message == "Note On":
		print("pad 48 -> ", value)

	if channel == 5 and index == 50 and message == "Note On":
		print("pad 49 -> ", value)
	
	if channel == 5 and index == 49 and message == "Note On":
		print("pad 50 -> ", value)
	
	# ------------------------------
	# channel 6 static

	if channel == 1 and index == 38 and message == "Note On":
		print("pad 51 -> ", value)

	if channel == 1 and index == 30 and message == "Note On":
		print("pad 52 -> ", value)
	
	if channel == 1 and index == 22 and message == "Note On":
		print("pad 53 -> ", value)
	
	if channel == 1 and index == 14 and message == "Note On":
		print("pad 54 -> ", value)
	
	if channel == 1 and index == 6 and message == "Note On":
		print("pad 55 -> ", value)

	if channel == 6 and index == 53 and message == "Note On":
		print("pad 56 -> ", value)

	# selectors untriggered, will print knob panel state

	# if channel == 6 and index == 24 and message == "Control Change":
	#	print("selector 6 -> ", value)
	
	if channel == 6 and index == 51 and message == "Note On":
		print("pad 57 -> ", value)
	
	if channel == 6 and index == 67 and message == "Note On":
		print("pad 58 -> ", value)

	if channel == 6 and index == 50 and message == "Note On":
		print("pad 59 -> ", value)
	
	if channel == 6 and index == 49 and message == "Note On":
		print("pad 60 -> ", value)

	# ------------------------------
	# channel 7 static

	if channel == 1 and index == 39 and message == "Note On":
		print("pad 61 -> ", value)

	if channel == 1 and index == 31 and message == "Note On":
		print("pad 62 -> ", value)
	
	if channel == 1 and index == 23 and message == "Note On":
		print("pad 63 -> ", value)
	
	if channel == 1 and index == 15 and message == "Note On":
		print("pad 64 -> ", value)
	
	if channel == 1 and index == 7 and message == "Note On":
		print("pad 65 -> ", value)

	if channel == 7 and index == 53 and message == "Note On":
		print("pad 66 -> ", value)

	# selectors untriggered, will print knob panel state

	# if channel == 7 and index == 24 and message == "Control Change":
	#	print("selector 7 -> ", value)
	
	if channel == 7 and index == 51 and message == "Note On":
		print("pad 67 -> ", value)
	
	if channel == 7 and index == 67 and message == "Note On":
		print("pad 68 -> ", value)

	if channel == 7 and index == 50 and message == "Note On":
		print("pad 69 -> ", value)
	
	if channel == 7 and index == 49 and message == "Note On":
		print("pad 70 -> ", value)

	# ------------------------------
	# channel 8 static

	if channel == 1 and index == 40 and message == "Note On":
		print("pad 71 -> ", value)

	if channel == 1 and index == 32 and message == "Note On":
		print("pad 72 -> ", value)
	
	if channel == 1 and index == 24 and message == "Note On":
		print("pad 73 -> ", value)
	
	if channel == 1 and index == 16 and message == "Note On":
		print("pad 74 -> ", value)
	
	if channel == 1 and index == 8 and message == "Note On":
		print("pad 75 -> ", value)

	if channel == 8 and index == 53 and message == "Note On":
		print("pad 76 -> ", value)

	# selectors untriggered, will print knob panel state

	# if channel == 8 and index == 24 and message == "Control Change":
	#	print("selector 8 -> ", value)
	
	if channel == 8 and index == 51 and message == "Note On":
		print("pad 77 -> ", value)
	
	if channel == 8 and index == 67 and message == "Note On":
		print("pad 78 -> ", value)

	if channel == 8 and index == 50 and message == "Note On":
		print("pad 79 -> ", value)
	
	if channel == 8 and index == 49 and message == "Note On":
		print("pad 80 -> ", value)

	# ------------------------------
	# channel 9 static

	if channel == 1 and index == 83 and message == "Note On":
		print("pad 81 -> ", value)

	if channel == 1 and index == 84 and message == "Note On":
		print("pad 82 -> ", value)
	
	if channel == 1 and index == 85 and message == "Note On":
		print("pad 83 -> ", value)
	
	if channel == 1 and index == 86 and message == "Note On":
		print("pad 84 -> ", value)
	
	if channel == 1 and index == 87 and message == "Note On":
		print("pad 85 -> ", value)

	if channel == 1 and index == 82 and message == "Note On":
		print("pad 86 -> ", value)

	# selectors untriggered, will print knob panel state

	# if channel == 9 and index == 24 and message == "Control Change":
	#	print("selector 9 -> ", value)

	# bottom row, fixed sliders
	# ------------------------------

	if channel == 1 and index == 8 and message == "Control Change":
		print("slider 1 -> ", value)
	
	if channel == 2 and index == 8 and message == "Control Change":
		print("slider 2 -> ", value)
	
	if channel == 3 and index == 8 and message == "Control Change":
		print("slider 3 -> ", value)
	
	if channel == 4 and index == 8 and message == "Control Change":
		print("slider 4 -> ", value)
	
	if channel == 5 and index == 8 and message == "Control Change":
		print("slider 5 -> ", value)
	
	if channel == 6 and index == 8 and message == "Control Change":
		print("slider 6 -> ", value)
	
	if channel == 7 and index == 8 and message == "Control Change":
		print("slider 7 -> ", value)
	
	if channel == 8 and index == 8 and message == "Control Change":
		print("slider 8 -> ", value)
	
	if channel == 1 and index == 15 and message == "Control Change":
		print("slider 9 -> ", value)
	
	# top right panel, fixed buttons
	# ------------------------------

	if channel == 1 and index == 88 and message == "Note On":
		print("button 1, on -> ", value)
	if channel == 1 and index == 88 and message == "Note Off":
		print("button 1, off -> ", value)

	if channel == 1 and index == 92 and message == "Note On":
		print("button 2, play on -> ", value)
	if channel == 1 and index == 92 and message == "Note Off":
		print("button 2, play off -> ", value)

	if channel == 1 and index == 94 and message == "Note On":
		print("button 3, record on -> ", value)
	if channel == 1 and index == 94 and message == "Note Off":
		print("button 3, record off -> ", value)
	
	if channel == 1 and index == 103 and message == "Note On":
		print("button 4, session on -> ", value)
	if channel == 1 and index == 103 and message == "Note Off":
		print("button 4, session off -> ", value)
	
	if channel == 1 and index == 89 and message == "Note On":
		print("button 5, on -> ", value)
	if channel == 1 and index == 89 and message == "Note Off":
		print("button 5, off -> ", value)
	
	if channel == 1 and index == 91 and message == "Note On":
		print("button 6, metronome on -> ", value)
	if channel == 1 and index == 91 and message == "Note Off":
		print("button 6, metronome off -> ", value)

	if channel == 1 and index == 100 and message == "Note On":
		print("button 7, off -> ", value)

	if channel == 1 and index == 90 and message == "Note On":
		print("button 8, on -> ", value)
	if channel == 1 and index == 90 and message == "Note Off":
		print("button 8, off -> ", value)
	
	if channel == 1 and index == 101 and message == "Note On":
		print("button 9, on -> ", value)

	if channel == 1 and index == 102 and message == "Note On":
		print("button 10, on -> ", value)

	if channel == 1 and index == 14 and message == "Control Change":
		if value == 127:
			print("master knob esquerda, <- ", value)
		else:
			print("master knob direita, -> ", value)
		
	# bottom right panel, fixed buttons
	# ------------------------------

	# (arrows)

	if channel == 1 and index == 98 and message == "Note On":
		print("button 12, left : ", value)
	
	if channel == 1 and index == 95 and message == "Note On":
		print("button 13, top -> ", value)
	
	if channel == 1 and index == 96 and message == "Note On":
		print("button 14, bottom -> ", value)

	if channel == 1 and index == 97 and message == "Note On":
		print("button 15, right -> ", value)
	
	# (shift, bank, wheel)

	if channel == 1 and index == 99 and message == "Note On":
		print("button 16, shift -> ", value)
	
	if channel == 1 and index == 104 and message == "Note On":
		print("button 17, bank on -> ", value)
	if channel == 1 and index == 104 and message == "Note Off":
		print("button 17, bank off -> ", value)

	if channel == 1 and index == 16 and message == "Control Change":
		print("wheel -> ", value)

	# right panel, channel 1
	# ------------------------------
	# (all forward, stop at 126)

	if channel == 1 and index == 17 and message == "Control Change":
		if value != 127:
			print("knob 1_1 -> ", value)
	
	if channel == 1 and index == 18 and message == "Control Change":
		if value != 127:
			print("knob 1_2 -> ", value)
	
	if channel == 1 and index == 19 and message == "Control Change":
		if value != 127:
			print("knob 1_3 -> ", value)
	
	if channel == 1 and index == 20 and message == "Control Change":
		if value != 127:
			print("knob 1_4 -> ", value)
	
	if channel == 1 and index == 21 and message == "Control Change":
		if value != 127:
			print("knob 1_5 -> ", value)
	
	if channel == 1 and index == 22 and message == "Control Change":
		if value != 127:
			print("knob 1_6 -> ", value)
	
	if channel == 1 and index == 23 and message == "Control Change":
		if value != 127:
			print("knob 1_7 -> ", value)
	
	if channel == 1 and index == 24 and message == "Control Change":
		if value != 127:
			print("knob 1_8 -> ", value)
	
	# buttons

	if channel == 1 and index == 59 and message == "Note On":
		print("button 1_1, left on -> ", value)
	if channel == 1 and index == 59 and message == "Note Off":
		print("button 1_1, left off -> ", value)
	
	if channel == 1 and index == 60 and message == "Note On":
		print("button 1_2, right on -> ", value)
	if channel == 1 and index == 60 and message == "Note Off":
		print("button 1_2, right off -> ", value)

	if channel == 1 and index == 61 and message == "Note On":
		print("button 1_3, left on -> ", value)
	if channel == 1 and index == 61 and message == "Note Off":
		print("button 1_3, left off -> ", value)
	
	if channel == 1 and index == 62 and message == "Note On":
		print("button 1_4, right on -> ", value)
	if channel == 1 and index == 62 and message == "Note Off":
		print("button 1_4, right off -> ", value)
	
	if channel == 1 and index == 63 and message == "Note On":
		print("button 1_5, on -> ", value)
	
	if channel == 1 and index == 64 and message == "Note On":
		print("button 1_6, on -> ", value)
	
	if channel == 1 and index == 65 and message == "Note On":
		print("button 1_7, on -> ", value)
	
	if channel == 1 and index == 66 and message == "Note On":
		print("button 1_8, on -> ", value)

	# right panel, channel 2
	# ------------------------------
	# (all forward, stop at 126)

	if channel == 2 and index == 17 and message == "Control Change":
		if value != 127:
			print("knob 2_1 -> ", value)
	
	if channel == 2 and index == 18 and message == "Control Change":
		if value != 127:
			print("knob 2_2 -> ", value)
	
	if channel == 2 and index == 19 and message == "Control Change":
		if value != 127:
			print("knob 2_3 -> ", value)
	
	if channel == 2 and index == 20 and message == "Control Change":
		if value != 127:
			print("knob 2_4 -> ", value)
	
	if channel == 2 and index == 21 and message == "Control Change":
		if value != 127:
			print("knob 2_5 -> ", value)
	
	if channel == 2 and index == 22 and message == "Control Change":
		if value != 127:
			print("knob 2_6 -> ", value)
	
	if channel == 2 and index == 23 and message == "Control Change":
		if value != 127:
			print("knob 2_7 -> ", value)
	
	if channel == 2 and index == 24 and message == "Control Change":
		if value != 127:
			print("knob 2_8 -> ", value)

	# buttons

	if channel == 2 and index == 59 and message == "Note On":
		print("button 2_1, left on -> ", value)
	if channel == 2 and index == 59 and message == "Note Off":
		print("button 2_1, left off -> ", value)
	
	if channel == 2 and index == 60 and message == "Note On":
		print("button 2_2, right on -> ", value)
	if channel == 2 and index == 60 and message == "Note Off":
		print("button 2_2, right off -> ", value)

	if channel == 2 and index == 61 and message == "Note On":
		print("button 2_3, left on -> ", value)
	if channel == 2 and index == 61 and message == "Note Off":
		print("button 2_3, left off -> ", value)
	
	if channel == 2 and index == 62 and message == "Note On":
		print("button 2_4, right on -> ", value)
	if channel == 2 and index == 62 and message == "Note Off":
		print("button 2_4, right off -> ", value)
	
	if channel == 2 and index == 63 and message == "Note On":
		print("button 2_5, on -> ", value)
	
	if channel == 2 and index == 64 and message == "Note On":
		print("button 2_6, on -> ", value)
	
	if channel == 2 and index == 65 and message == "Note On":
		print("button 2_7, on -> ", value)
	
	if channel == 2 and index == 66 and message == "Note On":
		print("button 2_8, on -> ", value)

	# right panel, channel 3
	# ------------------------------
	# (all forward, stop at 126)

	if channel == 3 and index == 17 and message == "Control Change":
		if value != 127:
			print("knob 3_1 -> ", value)
	
	if channel == 3 and index == 18 and message == "Control Change":
		if value != 127:
			print("knob 3_2 -> ", value)
	
	if channel == 3 and index == 19 and message == "Control Change":
		if value != 127:
			print("knob 3_3 -> ", value)
	
	if channel == 3 and index == 20 and message == "Control Change":
		if value != 127:
			print("knob 3_4 -> ", value)
	
	if channel == 3 and index == 21 and message == "Control Change":
		if value != 127:
			print("knob 3_5 -> ", value)
	
	if channel == 3 and index == 22 and message == "Control Change":
		if value != 127:
			print("knob 3_6 -> ", value)
	
	if channel == 3 and index == 23 and message == "Control Change":
		if value != 127:
			print("knob 3_7 -> ", value)
	
	if channel == 3 and index == 24 and message == "Control Change":
		if value != 127:
			print("knob 3_8 -> ", value)

	# buttons

	if channel == 3 and index == 59 and message == "Note On":
		print("button 3_1, left on -> ", value)
	if channel == 3 and index == 59 and message == "Note Off":
		print("button 3_1, left off -> ", value)
	
	if channel == 3 and index == 60 and message == "Note On":
		print("button 3_2, right on -> ", value)
	if channel == 3 and index == 60 and message == "Note Off":
		print("button 3_2, right off -> ", value)

	if channel == 3 and index == 61 and message == "Note On":
		print("button 3_3, left on -> ", value)
	if channel == 3 and index == 61 and message == "Note Off":
		print("button 3_3, left off -> ", value)
	
	if channel == 3 and index == 62 and message == "Note On":
		print("button 3_4, right on -> ", value)
	if channel == 3 and index == 62 and message == "Note Off":
		print("button 3_4, right off -> ", value)
	
	if channel == 3 and index == 63 and message == "Note On":
		print("button 3_5, on -> ", value)
	
	if channel == 3 and index == 64 and message == "Note On":
		print("button 3_6, on -> ", value)
	
	if channel == 3 and index == 65 and message == "Note On":
		print("button 3_7, on -> ", value)
	
	if channel == 3 and index == 66 and message == "Note On":
		print("button 3_8, on -> ", value)
	
	# right panel, channel 4
	# ------------------------------
	# (all forward, stop at 126)

	if channel == 4 and index == 17 and message == "Control Change":
		if value != 127:
			print("knob 4_1 -> ", value)
	
	if channel == 4 and index == 18 and message == "Control Change":
		if value != 127:
			print("knob 4_2 -> ", value)
	
	if channel == 4 and index == 19 and message == "Control Change":
		if value != 127:
			print("knob 4_3 -> ", value)
	
	if channel == 4 and index == 20 and message == "Control Change":
		if value != 127:
			print("knob 4_4 -> ", value)
	
	if channel == 4 and index == 21 and message == "Control Change":
		if value != 127:
			print("knob 4_5 -> ", value)
	
	if channel == 4 and index == 22 and message == "Control Change":
		if value != 127:
			print("knob 4_6 -> ", value)
	
	if channel == 4 and index == 23 and message == "Control Change":
		if value != 127:
			print("knob 4_7 -> ", value)
	
	if channel == 4 and index == 24 and message == "Control Change":
		if value != 127:
			print("knob 4_8 -> ", value)

	# buttons

	if channel == 4 and index == 59 and message == "Note On":
		print("button 4_1, left on -> ", value)
	if channel == 4 and index == 59 and message == "Note Off":
		print("button 4_1, left off -> ", value)
	
	if channel == 4 and index == 60 and message == "Note On":
		print("button 4_2, right on -> ", value)
	if channel == 4 and index == 60 and message == "Note Off":
		print("button 4_2, right off -> ", value)

	if channel == 4 and index == 61 and message == "Note On":
		print("button 4_3, left on -> ", value)
	if channel == 4 and index == 61 and message == "Note Off":
		print("button 4_3, left off -> ", value)
	
	if channel == 4 and index == 62 and message == "Note On":
		print("button 4_4, right on -> ", value)
	if channel == 4 and index == 62 and message == "Note Off":
		print("button 4_4, right off -> ", value)
	
	if channel == 4 and index == 63 and message == "Note On":
		print("button 4_5, on -> ", value)
	
	if channel == 4 and index == 64 and message == "Note On":
		print("button 4_6, on -> ", value)
	
	if channel == 4 and index == 65 and message == "Note On":
		print("button 4_7, on -> ", value)
	
	if channel == 4 and index == 66 and message == "Note On":
		print("button 4_8, on -> ", value)
	
	# right panel, channel 5
	# ------------------------------
	# (all forward, stop at 126)

	if channel == 5 and index == 17 and message == "Control Change":
		if value != 127:
			print("knob 5_1 -> ", value)
	
	if channel == 5 and index == 18 and message == "Control Change":
		if value != 127:
			print("knob 5_2 -> ", value)
	
	if channel == 5 and index == 19 and message == "Control Change":
		if value != 127:
			print("knob 5_3 -> ", value)
	
	if channel == 5 and index == 20 and message == "Control Change":
		if value != 127:
			print("knob 5_4 -> ", value)
	
	if channel == 5 and index == 21 and message == "Control Change":
		if value != 127:
			print("knob 5_5 -> ", value)
	
	if channel == 5 and index == 22 and message == "Control Change":
		if value != 127:
			print("knob 5_6 -> ", value)
	
	if channel == 5 and index == 23 and message == "Control Change":
		if value != 127:
			print("knob 5_7 -> ", value)
	
	if channel == 5 and index == 24 and message == "Control Change":
		if value != 127:
			print("knob 5_8 -> ", value)

	# buttons

	if channel == 5 and index == 59 and message == "Note On":
		print("button 5_1, left on -> ", value)
	if channel == 5 and index == 59 and message == "Note Off":
		print("button 5_1, left off -> ", value)
	
	if channel == 5 and index == 60 and message == "Note On":
		print("button 5_2, right on -> ", value)
	if channel == 5 and index == 60 and message == "Note Off":
		print("button 5_2, right off -> ", value)

	if channel == 5 and index == 61 and message == "Note On":
		print("button 5_3, left on -> ", value)
	if channel == 5 and index == 61 and message == "Note Off":
		print("button 5_3, left off -> ", value)
	
	if channel == 5 and index == 62 and message == "Note On":
		print("button 5_4, right on -> ", value)
	if channel == 5 and index == 62 and message == "Note Off":
		print("button 5_4, right off -> ", value)
	
	if channel == 5 and index == 63 and message == "Note On":
		print("button 5_5, on -> ", value)
	
	if channel == 5 and index == 64 and message == "Note On":
		print("button 5_6, on -> ", value)
	
	if channel == 5 and index == 65 and message == "Note On":
		print("button 5_7, on -> ", value)
	
	if channel == 5 and index == 66 and message == "Note On":
		print("button 5_8, on -> ", value)

	# right panel, channel 6
	# ------------------------------
	# (all forward, stop at 126)

	if channel == 6 and index == 17 and message == "Control Change":
		if value != 127:
			print("knob 6_1 -> ", value)
	
	if channel == 6 and index == 18 and message == "Control Change":
		if value != 127:
			print("knob 6_2 -> ", value)
	
	if channel == 6 and index == 19 and message == "Control Change":
		if value != 127:
			print("knob 6_3 -> ", value)
	
	if channel == 6 and index == 20 and message == "Control Change":
		if value != 127:
			print("knob 6_4 -> ", value)
	
	if channel == 6 and index == 21 and message == "Control Change":
		if value != 127:
			print("knob 6_5 -> ", value)
	
	if channel == 6 and index == 22 and message == "Control Change":
		if value != 127:
			print("knob 6_6 -> ", value)
	
	if channel == 6 and index == 23 and message == "Control Change":
		if value != 127:
			print("knob 6_7 -> ", value)
	
	if channel == 6 and index == 24 and message == "Control Change":
		if value != 127:
			print("knob 6_8 -> ", value)

	# buttons

	if channel == 6 and index == 59 and message == "Note On":
		print("button 6_1, left on -> ", value)
	if channel == 6 and index == 59 and message == "Note Off":
		print("button 6_1, left off -> ", value)
	
	if channel == 6 and index == 60 and message == "Note On":
		print("button 6_2, right on -> ", value)
	if channel == 6 and index == 60 and message == "Note Off":
		print("button 6_2, right off -> ", value)

	if channel == 6 and index == 61 and message == "Note On":
		print("button 6_3, left on -> ", value)
	if channel == 6 and index == 61 and message == "Note Off":
		print("button 6_3, left off -> ", value)
	
	if channel == 6 and index == 62 and message == "Note On":
		print("button 6_4, right on -> ", value)
	if channel == 6 and index == 62 and message == "Note Off":
		print("button 6_4, right off -> ", value)
	
	if channel == 6 and index == 63 and message == "Note On":
		print("button 6_5, on -> ", value)
	
	if channel == 6 and index == 64 and message == "Note On":
		print("button 6_6, on -> ", value)
	
	if channel == 6 and index == 65 and message == "Note On":
		print("button 6_7, on -> ", value)
	
	if channel == 6 and index == 66 and message == "Note On":
		print("button 6_8, on -> ", value)

	# right panel, channel 7
	# ------------------------------
	# (all forward, stop at 126)

	if channel == 7 and index == 17 and message == "Control Change":
		if value != 127:
			print("knob 7_1 -> ", value)
	
	if channel == 7 and index == 18 and message == "Control Change":
		if value != 127:
			print("knob 7_2 -> ", value)
	
	if channel == 7 and index == 19 and message == "Control Change":
		if value != 127:
			print("knob 7_3 -> ", value)
	
	if channel == 7 and index == 20 and message == "Control Change":
		if value != 127:
			print("knob 7_4 -> ", value)
	
	if channel == 7 and index == 21 and message == "Control Change":
		if value != 127:
			print("knob 7_5 -> ", value)
	
	if channel == 7 and index == 22 and message == "Control Change":
		if value != 127:
			print("knob 7_6 -> ", value)
	
	if channel == 7 and index == 23 and message == "Control Change":
		if value != 127:
			print("knob 7_7 -> ", value)
	
	if channel == 7 and index == 24 and message == "Control Change":
		if value != 127:
			print("knob 7_8 -> ", value)

	# buttons

	if channel == 7 and index == 59 and message == "Note On":
		print("button 7_1, left on -> ", value)
	if channel == 7 and index == 59 and message == "Note Off":
		print("button 7_1, left off -> ", value)
	
	if channel == 7 and index == 60 and message == "Note On":
		print("button 7_2, right on -> ", value)
	if channel == 7 and index == 60 and message == "Note Off":
		print("button 7_2, right off -> ", value)

	if channel == 7 and index == 61 and message == "Note On":
		print("button 7_3, left on -> ", value)
	if channel == 7 and index == 61 and message == "Note Off":
		print("button 7_3, left off -> ", value)
	
	if channel == 7 and index == 62 and message == "Note On":
		print("button 7_4, right on -> ", value)
	if channel == 7 and index == 62 and message == "Note Off":
		print("button 7_4, right off -> ", value)
	
	if channel == 7 and index == 63 and message == "Note On":
		print("button 7_5, on -> ", value)
	
	if channel == 7 and index == 64 and message == "Note On":
		print("button 7_6, on -> ", value)
	
	if channel == 7 and index == 65 and message == "Note On":
		print("button 7_7, on -> ", value)
	
	if channel == 7 and index == 66 and message == "Note On":
		print("button 7_8, on -> ", value)

	# right panel, channel 8
	# ------------------------------
	# (all forward, stop at 126)

	if channel == 8 and index == 17 and message == "Control Change":
		if value != 127:
			print("knob 8_1 -> ", value)
	
	if channel == 8 and index == 18 and message == "Control Change":
		if value != 127:
			print("knob 8_2 -> ", value)
	
	if channel == 8 and index == 19 and message == "Control Change":
		if value != 127:
			print("knob 8_3 -> ", value)
	
	if channel == 8 and index == 20 and message == "Control Change":
		if value != 127:
			print("knob 8_4 -> ", value)
	
	if channel == 8 and index == 21 and message == "Control Change":
		if value != 127:
			print("knob 8_5 -> ", value)
	
	if channel == 8 and index == 22 and message == "Control Change":
		if value != 127:
			print("knob 8_6 -> ", value)
	
	if channel == 8 and index == 23 and message == "Control Change":
		if value != 127:
			print("knob 8_7 -> ", value)
	
	if channel == 8 and index == 24 and message == "Control Change":
		if value != 127:
			print("knob 8_8 -> ", value)

	# buttons

	if channel == 8 and index == 59 and message == "Note On":
		print("button 8_1, left on -> ", value)
	if channel == 8 and index == 59 and message == "Note Off":
		print("button 8_1, left off -> ", value)
	
	if channel == 8 and index == 60 and message == "Note On":
		print("button 8_2, right on -> ", value)
	if channel == 8 and index == 60 and message == "Note Off":
		print("button 8_2, right off -> ", value)

	if channel == 8 and index == 61 and message == "Note On":
		print("button 8_3, left on -> ", value)
	if channel == 8 and index == 61 and message == "Note Off":
		print("button 8_3, left off -> ", value)
	
	if channel == 8 and index == 62 and message == "Note On":
		print("button 8_4, right on -> ", value)
	if channel == 8 and index == 62 and message == "Note Off":
		print("button 8_4, right off -> ", value)
	
	if channel == 8 and index == 63 and message == "Note On":
		print("button 8_5, on -> ", value)
	
	if channel == 8 and index == 64 and message == "Note On":
		print("button 8_6, on -> ", value)
	
	if channel == 8 and index == 65 and message == "Note On":
		print("button 8_7, on -> ", value)
	
	if channel == 8 and index == 66 and message == "Note On":
		print("button 8_8, on -> ", value)

	# right panel, channel 9
	# ------------------------------
	# (all forward, stop at 126)

	if channel == 9 and index == 17 and message == "Control Change":
		if value != 127:
			print("knob 9_1 -> ", value)
	
	if channel == 9 and index == 18 and message == "Control Change":
		if value != 127:
			print("knob 9_2 -> ", value)
	
	if channel == 9 and index == 19 and message == "Control Change":
		if value != 127:
			print("knob 9_3 -> ", value)
	
	if channel == 9 and index == 20 and message == "Control Change":
		if value != 127:
			print("knob 9_4 -> ", value)
	
	if channel == 9 and index == 21 and message == "Control Change":
		if value != 127:
			print("knob 9_5 -> ", value)
	
	if channel == 9 and index == 22 and message == "Control Change":
		if value != 127:
			print("knob 9_6 -> ", value)
	
	if channel == 9 and index == 23 and message == "Control Change":
		if value != 127:
			print("knob 9_7 -> ", value)
	
	if channel == 9 and index == 24 and message == "Control Change":
		if value != 127:
			print("knob 9_8 -> ", value)

	# buttons

	if channel == 9 and index == 59 and message == "Note On":
		print("button 9_1, left on -> ", value)
	if channel == 9 and index == 59 and message == "Note Off":
		print("button 9_1, left off -> ", value)
	
	if channel == 9 and index == 60 and message == "Note On":
		print("button 9_2, right on -> ", value)
	if channel == 9 and index == 60 and message == "Note Off":
		print("button 9_2, right off -> ", value)

	if channel == 9 and index == 61 and message == "Note On":
		print("button 9_3, left on -> ", value)
	if channel == 9 and index == 61 and message == "Note Off":
		print("button 9_3, left off -> ", value)
	
	if channel == 9 and index == 62 and message == "Note On":
		print("button 9_4, right on -> ", value)
	if channel == 9 and index == 62 and message == "Note Off":
		print("button 9_4, right off -> ", value)
	
	if channel == 9 and index == 63 and message == "Note On":
		print("button 9_5, on -> ", value)
	
	if channel == 9 and index == 64 and message == "Note On":
		print("button 9_6, on -> ", value)
	
	if channel == 9 and index == 65 and message == "Note On":
		print("button 9_7, on -> ", value)
	
	if channel == 9 and index == 66 and message == "Note On":
		print("button 9_8, on -> ", value)

	return
