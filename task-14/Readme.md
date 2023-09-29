This task was fairly an easy task as it had a lot of resources on the web . The methods ( and passwords for the next level ) that I applied>

Level 0 :
Password : NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL

Level 1 :
Inorder to open the file named "-" i used cat ./- to access the password
Password : rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi

Level 2 :
Here the name of the file had spaces inbetween , so i used cat spaces\ in\ this\ filename to access the password
Password : aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG

Level 3 :
Here I have used cd to get into the directory and cat to access the password
Password :2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe

Level 4 :
From this task the complexity of the question started to increase systematically
Here I have used find .type -f | xargs file and got the info that the password is written in the file07
Password : lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR

Level 5 :
Here I have used find .type -f size 1033c ! -executable so that u could see the executable file in which the password is given
Password : P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU

Level 6 :
Here I have used find / -type f -user bandit7 -group bandit6  -size 33c to access the file in which the password is stored
Password : z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S

Level 7 :
Here I have used strings data.txt | grep "millonth" to access the password
Password : TESKZC0XvTetK0S9xNwm25STk5iWrBvP

Level 8 :
Here I have used sort data.txt | uniq -c  to access the password
Password :EN632PlfYiZbn3PhVK3XOGSlNInNE00t

Level 9 :
Here I have used strings data.txt | grep "="
Password : G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s

Level 10 :
Here I have used cat data.txt and base64 -d data.txt to get the password
Password : 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
