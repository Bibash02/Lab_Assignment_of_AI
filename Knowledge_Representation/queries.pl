% Facts 
animal(elephant). 
animal(horse). 
animal(tiger). 
bigger(elephant, horse). 
bigger(horse, dog). 
bigger(tiger, dog). 
% Rule 
larger(X,Y) :- 
    bigger(X,Y).