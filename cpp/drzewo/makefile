CXX=g++
CXXFLAGS=-Wall -I.
OBJS=drzewo2.o drzewo2_main.o

pong: drzewo2.o drzewo2_main.o	
	$(CXX) $(CXXFLAGS) $(OBJS) -o drzewo2_main.exe
	
.PHONY: clean

clean:
	rm -f *.o*~ core *~

