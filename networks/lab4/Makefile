FLAGS=-Ofast -O4

all: client server

client: client.c
	clang client.c -o client ${FLAGS}

server: server.c
	clang server.c -o server ${FLAGS}

clean:
	rm client server
