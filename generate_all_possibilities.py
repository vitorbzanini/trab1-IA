def generate_tic_tac_toe_states():
    states = []
    characters = ['x', 'o', 'b']
    for c1 in characters:
        for c2 in characters:
            for c3 in characters:
                for c4 in characters:
                    for c5 in characters:
                        for c6 in characters:
                            for c7 in characters:
                                for c8 in characters:
                                    for c9 in characters:
                                        state = f"{c1},{c2},{c3},{c4},{c5},{c6},{c7},{c8},{c9}\n"
                                        count_x = state.count('x')
                                        count_o = state.count('o')
                                        if abs(count_x - count_o) <= 1:
                                            states.append(state)
    return states

tic_tac_toe_states = generate_tic_tac_toe_states()

# Escrever as possibilidades em um arquivo
with open('tic_tac_toe_states2.txt', 'w') as file:
    file.writelines(tic_tac_toe_states)

print("Arquivo 'tic_tac_toe_states.txt' gerado com sucesso!")
