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
            if 57 < text[i][1] < 80:
                temp.append('2, %d, Note_on_c, 1, %d, 80\n' % (time, int(text[i][1])))
                time += int(text[i][0])
                temp.append('2, %d, Note_off_c, 1, %d, 0\n' % (time, int(text[i][1])))
                
            elif 10 < text[i+1][1] < 50:
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

