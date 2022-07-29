import py_midicsv as pm

notes = [[72.448166, 69, 4.305828], [52.95837, 69, 4.3259354],
 [46.933136, 69, 4.3311424], [61.006737, 72, 4.578083], [60.77861, 71, 4.931431],
 [63.47565,69, 5.2947235], [55.19062, 76, 5.714699], [52.65183, 64, 5.9247894],
 [73.04585, 64, 5.828499], [44.088512, 68, 6.5625916], [44.088512, 66, 6.5625916],
 [44.088512, 64, 6.5625916], [44.088512, 69, 6.5625916], [44.088512, 69, 6.5625916],
 [73.04585, 69, 5.828499], [73.04585, 72, 5.828499], [73.04585, 71, 5.828499],
 [73.04585, 69, 5.828499], [73.04585, 76, 5.828499], [73.04585, 64, 5.828499], 
 [72.448166, 69, 4.305828], [52.95837, 69, 4.3259354],
 [46.933136, 69, 4.3311424], [61.006737, 72, 4.578083], [60.77861, 71, 4.931431],
 [63.47565,69, 5.2947235], [55.19062, 76, 5.714699], [52.65183, 64, 5.9247894],
 [73.04585, 64, 5.828499], [44.088512, 68, 6.5625916], [44.088512, 66, 6.5625916],
 [44.088512, 64, 6.5625916], [44.088512, 69, 6.5625916], [44.088512, 69, 6.5625916],
 [73.04585, 69, 5.828499], [73.04585, 72, 5.828499], [73.04585, 71, 5.828499],
 [73.04585, 69, 5.828499], [73.04585, 76, 5.828499], [73.04585, 64, 5.828499],
 [72.448166, 81, 4.305828], [52.95837, 81, 4.3259354],
 [46.933136, 81, 4.3311424], [61.006737, 82, 4.578083], [60.77861, 81, 4.931431],
 [63.47565,79, 5.2947235], [55.19062, 77, 5.714699], [52.65183, 74, 5.9247894],
 [73.04585, 74, 5.828499], [44.088512, 77, 6.5625916], [44.088512, 76, 6.5625916],
 [44.088512, 74, 6.5625916], [44.088512, 79, 6.5625916], [44.088512, 79, 6.5625916],
 [73.04585, 79, 5.828499], [73.04585, 81, 5.828499], [73.04585, 79, 5.828499],
 [73.04585, 77, 5.828499], [73.04585, 76, 5.828499], [73.04585, 72, 5.828499],[73.04585, 72, 5.828499],
 [73.04585, 76, 5.828499],[73.04585, 74, 5.828499],[73.04585, 72, 5.828499],[73.04585, 77, 5.828499],
 [73.04585, 71, 5.828499],[73.04585, 71, 5.828499],[73.04585, 74, 5.828499],[73.04585, 72, 5.828499],[73.04585, 71, 5.828499],[73.04585, 76, 5.828499],
 [73.04585, 69, 5.828499],[73.04585, 69, 5.828499],[73.04585, 72, 5.828499],[73.04585, 71, 5.828499],[73.04585, 69, 5.828499],[73.04585, 65, 5.828499],
 [73.04585, 75, 5.828499],[73.04585, 64, 5.828499],[73.04585, 76, 5.828499],[73.04585, 74, 5.828499],[73.04585, 72, 5.828499],[73.04585, 69, 5.828499],]

def data_form(text):
    temp = ['0, 0, Header, 1, 3, 256\n', '1, 0, Start_track\n',  '1, 0, Title_t, "Computer Masterpiece"\n', '1, 0, Text_t, "Mr. Computer and Mason Choi"\n', '1, 0, Time_signature, 4, 4, 24, 8', '1, 0, Tempo, 500000', '1, 0, End_track\n', '2, 0, Start_track\n', '2, 0, Title_t, "Piano"\n', '2, 0, Program_c, 0, 0\n', '2, 0, Control_c, 0, 7, 85\n', '2, 0, Control_c, 0, 10, 76\n']
    # increase tempo value for slower song
    time = int(text[0][0])


    for i in range(len(text)):
        if i == 0:
            temp.append('2, %d, Note_on_c, 1, %d, 80\n' % (time, int(text[i][1]))) # Why text[i + 1] not just text[i]????
            time += int(text[i][0])
            temp.append('2, %d, Note_off_c, 1, %d, 0\n' % (time, int(text[i][1])))


        elif 0 < i <= (len(text)-4):
            if 10 < text[i][1] < 127:
                temp.append('2, %d, Note_on_c, 1, %d, 80\n' % (time, int(text[i][1])))
                time += int(text[i][0])
                temp.append('2, %d, Note_off_c, 1, %d, 0\n' % (time, int(text[i][1])))
                
            elif 57 < text[i+1][1] < 66:
                temp.append('2, %d, Note_on_c, 1, %d, 80\n' % (time, int(text[i][1])))
                temp.append('2, %d, Note_on_c, 1, %d, 80\n' % (time, int(text[i + 1][1])))
                time += int(text[i][0])
                temp.append('2, %d, Note_off_c, 1, %d, 0\n' % (time, int(text[i][1])))
                temp.append('2, %d, Note_off_c, 1, %d, 0\n' % (time, int(text[i + 1][1])))

            elif 57 < text[i+2][1] < 66:

                temp.append('2, %d, Note_on_c, 1, %d, 80\n' % (time, int(text[i][1])))
                temp.append('2, %d, Note_on_c, 1, %d, 80\n' % (time, int(text[i + 1][1])))
                temp.append('2, %d, Note_on_c, 1, %d, 80\n' % (time, int(text[i + 2][1])))
                time += int(text[i][0])
                temp.append('2, %d, Note_off_c, 1, %d, 0\n' % (time, int(text[i][1])))
                temp.append('2, %d, Note_off_c, 1, %d, 0\n' % (time, int(text[i+1][1])))
                temp.append('2, %d, Note_off_c, 1, %d, 0\n' % (time, int(text[i+2][1])))
            elif 57 < text[i+3][1] < 66:
                temp.append('2, %d, Note_on_c, 1, %d, 80\n' % (time, int(text[i][1])))
                temp.append('2, %d, Note_on_c, 1, %d, 80\n' % (time, int(text[i + 1][1])))
                temp.append('2, %d, Note_on_c, 1, %d, 80\n' % (time, int(text[i + 2][1])))
                temp.append('2, %d, Note_on_c, 1, %d, 80\n' % (time, int(text[i + 3][1])))
                time += int(text[i][0])
                temp.append('2, %d, Note_off_c, 1, %d, 0\n' % (time, int(text[i][1])))
                temp.append('2, %d, Note_off_c, 1, %d, 0\n' % (time, int(text[i+1][1])))
                temp.append('2, %d, Note_off_c, 1, %d, 0\n' % (time, int(text[i+2][1])))
                temp.append('2, %d, Note_off_c, 1, %d, 0\n' % (time, int(text[i+3][1])))

        else:
            temp.append('2, %d, Note_on_c, 1, %d, 80\n' % (time, int(text[i][1])))
            time += int(text[i][0])
            temp.append('2, %d, Note_off_c, 1, %d, 0\n' % (time, int(text[i][1])))

    temp.append('2, %d, Note_off_c, 1, %d, 0\n' % (time, int(text[len(text)-1][1])))
    temp.append('2, %s, End_track\n' % (str(time)))
    temp.append('0, 0, End_of_file')

    return temp


midi_data = data_form(notes)
midi_object = pm.csv_to_midi(midi_data)

if input('Save file? y/n:').lower().startswith('y'):
    file_name = input('File name: ')
    file_name += '.mid'
    with open(file_name, "wb") as output_file:
        midi_writer = pm.FileWriter(output_file)
        midi_writer.write(midi_object)

print('Done')
