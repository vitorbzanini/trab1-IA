

file = open("tic_tac_toe_states.txt", "r")
new_file = open("new_tic-tac-toe.data", "w")

bool_o_win = False
bool_x_win = False

data = file.readline()
while data:
    print("before" + data)
    data_to_write = data[0:17] + ','
    data  = data[0:17].replace(",","")
    print("after = " + data)
    
    for i in range(0,9,3): #0,3,6
        if(data[0] + data[4] + data[8] == 'ooo'):
            bool_o_win = True

        if(data[2] + data[4] + data[6] == 'ooo'):
            bool_o_win = True
       
        if(data[i:i+3] == 'ooo'):
            bool_o_win = True
        
        if(data[int(i/3)] + data[int(i/3)+3] + data[int(i/3)+6] == 'ooo'):
            bool_o_win = True
        
        if(data[0] + data[4] + data[8] == 'xxx'):
            bool_x_win = True
        
        if(data[2] + data[4] + data[6] == 'xxx'):
            bool_x_win = True
        
        if(data[i:i+3] == 'xxx'):
            bool_x_win = True
        
        if(data[int(i/3)] + data[int(i/3)+3] + data[int(i/3)+6] == 'xxx'):
            bool_x_win = True

    if not(bool_o_win and bool_x_win):
        new_file.write(data_to_write)
        if bool_o_win: 
            new_file.write("Jogador O venceu\n")
        elif bool_x_win:
            new_file.write("Jogador X venceu\n")
        elif "b" in data:
            new_file.write("Tem jogo\n")
        else:
            new_file.write("Empate\n")    

    bool_o_win = False
    bool_x_win = False
    #a = input('').split(" ")[0]
    #print(a)
    data = file.readline()

