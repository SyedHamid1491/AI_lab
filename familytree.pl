father(hussain,hashim).
father(hussain,ridwan).
father(hussain,adnan).
father(hussain,rakan).
father(hashim,razaq).
father(hashim,hamza).
father(ridwan,jaffer).
father(ridwan,mustafa).
father(adnan,hamid).
father(adnan,ghalib).
father(adnan,ghazi).
father(rakan,ryad).

sibling(hashim,ridwan).
sibling(hashim,adnan).
sibling(hashim,rakan).
sibling(ridwan,hashim).
sibling(ridwan,adnan).
sibling(ridwan,rakan).
sibling(adnan,hashim).
sibling(adnan,ridwan).
sibling(adnan,rakan).
sibling(rakan,hashim).
sibling(rakan,ridwan).
sibling(rakan,adnan).
sibling(razaq,hamza).
sibling(hamza,razaq).
sibling(jaffer,mustafa).
sibling(mustafa,jaffer).
sibling(hamid,ghalib).
sibling(hamid,ghazi).
sibling(ghalib,hamid).
sibling(ghalib,ghazi).
sibling(ghazi,hamid).
sibling(ghazi,ghalib).

grandfather(X,Y):-father(X,Z),father(Z,Y).

uncle(A,B):-father(X,A),father(X,Y),father(Y,B),sibling(A,Y).

cousin(X,Y):-father(M,X),father(N,Y),sibling(M,N).
