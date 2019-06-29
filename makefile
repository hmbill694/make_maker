CC = g++ #CC is a variable containing the compiler we are using
CFlAGS = -g -c -Wall # -c means compile, -Wall is a necessary warning, -g is debug data
all:	run
run:	main.o	$(CC) -o main.o
main.o:	BST.h main.cpp
	$(CC) $(CFLAGS) main.cpp
clean:
	rm *.o run