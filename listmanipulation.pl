append([], L, L).
append([H|T1], L2, [H|T3]) :- append(T1, L2, T3).
reverse_list([], []).
reverse_list([H|T], R) :- reverse_list(T, RT), append(RT, [H], R).