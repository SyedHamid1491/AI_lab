parent(john,jim).
parent(john,ann).
parent(jane,jim).
male(john).
female(jane).

father(X,Y):-parent(X,Y),male(X).
mother(X,Y):-parent(X,Y),female(X).