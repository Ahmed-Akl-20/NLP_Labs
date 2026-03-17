def viterbi(sentence, states, start_p, trans_p, emit_p):

    V = [{}]
    path = {}

    for state in states:
        V[0][state] = start_p.get(state,0) * emit_p[state].get(sentence[0],1e-6)
        path[state] = [state]

    for t in range(1,len(sentence)):
        V.append({})
        new_path = {}

        for curr_state in states:

            max_prob, prev_state = max(
                (V[t-1][y0] *
                 trans_p[y0].get(curr_state,1e-6) *
                 emit_p[curr_state].get(sentence[t],1e-6), y0)
                for y0 in states
            )

            V[t][curr_state] = max_prob
            new_path[curr_state] = path[prev_state] + [curr_state]

        path = new_path

    n = len(sentence)-1
    prob, final_state = max((V[n][y],y) for y in states)

    return path[final_state]


# مثال بسيط
states = ["DET","NOUN","VERB"]

start_prob = {"DET":0.8,"NOUN":0.2}

transition = {
"DET":{"NOUN":0.9},
"NOUN":{"VERB":0.8},
"VERB":{"NOUN":0.2}
}

emission = {
"DET":{"a":0.5,"the":0.5},
"NOUN":{"cat":0.5,"dog":0.5},
"VERB":{"barked":0.5,"ran":0.5}
}

test_sentence = ["a","cat","barked"]

result = viterbi(test_sentence,states,start_prob,transition,emission)

print("Sentence:",test_sentence)
print("Predicted Tags:",result)