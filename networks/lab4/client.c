#include <netdb.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define BUFF_SIZE 1024

int main (int argc, char* argv[]) {
    int n;
    int serverfd, portno;

    struct sockaddr_in serv_addr;
    struct hostent *server;

    char* buffer = malloc(BUFF_SIZE);

    /* create socket */
    portno = 4242;
    serverfd = socket(AF_INET, SOCK_STREAM, 0);
    if (serverfd < 0) {
        free(buffer);
        perror("Could not open socket");
        exit(EXIT_FAILURE);
    }

    /* get localhost */
    server = gethostbyname("localhost");
    if (server == NULL) {
        free(buffer);
        close(serverfd);
        perror("Could not find host");
    }

    /* init serv_addr structure */
    memset(&serv_addr, 0, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    memcpy(&serv_addr.sin_addr.s_addr,
            server->h_addr_list[0],
            server->h_length);
    serv_addr.sin_port = htons(portno);

    /* connect to server */
    if (connect(serverfd,
                (struct sockaddr *) &serv_addr,
                sizeof(serv_addr)) < 0) {
        free(buffer);
        close(serverfd);
        perror("Could not connect");
        exit(EXIT_FAILURE);
    }

    /* connection loop */
    while (1) {
        memset(buffer, '\0', BUFF_SIZE);

        /* read user's input */
        buffer = fgets(buffer, BUFF_SIZE, stdin);

        /* write to server socket */
        n = strlen(buffer);
        n = write(serverfd, buffer, n);
        if (n < 0) {
            free(buffer);
            close(serverfd);
            perror("Could not write to socket");
            exit(EXIT_FAILURE);
        }

        /* read from server socket */
        memset(buffer, '\0', BUFF_SIZE);
        n = read(serverfd, buffer, BUFF_SIZE);
        if (n < 0) {
            free(buffer);
            close(serverfd);
            perror("Could not read from socket");
            exit(EXIT_FAILURE);
        }
        fputs(buffer, stdout);
    }
    free(buffer);
    close(serverfd);
    exit(EXIT_SUCCESS);
}

