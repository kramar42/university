GCC=gcc-4.9
RM=rm
OBJ=lab.o print.o
TARGET=lab

all: $(OBJ)
	$(GCC) $(OBJ) -o $(TARGET)

%.o.c:
	$(GCC) -c $@

clean:
	$(RM) $(OBJ)

cleanall: clean
	$(RM) $(TARGET)
