% Facts
male(ram).
male(shyam).
male(hari).

female(sita).
female(gita).
female(rina).

% Rules
student(X) :- male(X).
student(X) :- female(X).
Sample Queries
?- male(ram).
true.

?- female(gita).
true.

?- student(rina).
true.

?- student(hari).
true.