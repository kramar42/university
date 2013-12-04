#include <netdb.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define BUFF_SIZE 1024

int main() {
    int serverfd;
    int clientfd;
    socklen_t clilen;

    int optval;
    int portno;
    int n;

    struct sockaddr_in serv_addr;
    struct sockaddr_in cli_addr;

    char* buffer = malloc(BUFF_SIZE);

    /* create socket */
    serverfd = socket(AF_INET, SOCK_STREAM, 0);
    if (serverfd < 0) {
        perror("Could not open socket");
        exit(EXIT_FAILURE);
    }

    /* set socket options */
    optval = 1;
    setsockopt(serverfd, SOL_SOCKET, SO_REUSEADDR, &optval, sizeof optval);

    /* init serv_addr structure */
    memset(&serv_addr, 0, sizeof(serv_addr));
    portno = 4242;
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = INADDR_ANY;
    serv_addr.sin_port = htons(portno);

    /* bind socket to address */
    if (bind(serverfd, (struct sockaddr *) &serv_addr,
                sizeof(serv_addr)) < 0) {
        close(serverfd);
        perror("Could not bind socket");
        exit(EXIT_FAILURE);
    }

    /* listen to connections */
    listen(serverfd, 0);

    /* main socket loop */
    while (1) {
        clilen = sizeof(cli_addr);
        /* accept client connect */
        clientfd = accept(serverfd,
                (struct sockaddr *) &cli_addr,
                &clilen);
        if (clientfd < 0) {
            close(clientfd);
            perror("Could not accept socket");
            continue;
        }

        /* client connection loop */
        while (1) {
            memset(buffer, '\0', BUFF_SIZE);

            /* read client's input */
            n = read(clientfd, buffer, BUFF_SIZE);
            if (n < 0) {
                close(clientfd);
                perror("Could not read from client socket");
                break;
            }
            else if (n == 0)
                break;

            /* print input */
            fputs(buffer, stdout);

            /* echo input */
            n = write(clientfd, buffer, strlen(buffer));
            if (n < 0) {
                close(clientfd);
                perror("Could not write to client socket");
                break;
            }
        }
        close(clientfd);
    }
    free(buffer);
    exit(EXIT_SUCCESS);
}

