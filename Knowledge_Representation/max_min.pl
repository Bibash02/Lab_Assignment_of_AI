% Maximum 
max(X, Y, X) :- X >= Y. 
max(X, Y, Y) :- Y > X. 

% Minimum 
min(X, Y, X) :- X =< Y. 
min(X, Y, Y) :- Y < X.