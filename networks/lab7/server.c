#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdlib.h>
int main()
{
	int sock, listener;
	struct sockaddr_in addr;
	char buf[1024];
	int bytes_read;

	listener = socket(AF_INET, SOCK_STREAM, 0);
	if(listener < 0)
	{
		perror("socket");
		exit(1);
	}

	addr.sin_family = AF_INET;
	addr.sin_port = htons(3425);
	addr.sin_addr.s_addr = INADDR_ANY;

	if (bind(listener, (struct sockaddr *)&addr, sizeof(addr)) < 0)
	{
		perror("bind");
		exit(2);
	}

	while(1)
	{
		switch(fork())
		{
			case -1:
				perror("fork");
				break;

			case 0:
				close(listener);
				while(1)
				{
					bytes_read = recv(sock, buf, 1024, 0);
					if(bytes_read <= 0) break;
					send(sock, buf, bytes_read, 0);
				}

				close(sock);
				_exit(0);

			default:
				close(sock);
		}
	}

	close(listener);

	return 0;
}
