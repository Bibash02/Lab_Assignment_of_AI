% Facts: Students who studied 
studied(radha). 
studied(rakesh). 
studied(anish). 

% Facts: Students who did not study 
not_studied(rekha). 
not_studied(bibek). 

% Rule: If a student studies, they pass the exam 
pass(X) :- 
    studied(X). 

% Rule: If a student passes, they are happy 
happy(X) :- 
    pass(X).