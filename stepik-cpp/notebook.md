g++ -E square.cpp -o square_preprocessed.cpp
g++ -E main.cpp -o main_preprocessed.cpp

g++ -c square.cpp
g++ -c main.cpp

g++ square.o main.o -o program

g++ main.cpp square.cpp -o program

g++ -S square.cpp # assembler-view

c++filt -n _Z6squarei # -> square(int)