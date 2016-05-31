##
## Made by Kevin Derome
## 
## Started on  Thu May 26 15:09:34 2016 Kevin Derome
## Last update Fri May 27 00:48:40 2016 Kevin Derome
##

CC = 		gcc

RM = 		rm -rf

SRC = 		

NAME = 		braille-ms

OBJ = 		$(SRC:.c=.o)

$(NAME):	$(OBJ)
		$(CC) $(OBJ) -o $(NAME)

all:		$(NAME)

install:
	@echo "Installing braille-ms"
	 cp -r modules /bin
	 cp -r mylib /bin
	 cp -r main /bin/braille-ms
	 @echo "installation réussie"
uninstall:
	@echo "uninstalling ..."
	 $(RM) /bin/modules
	 $(RM) /bin/mylib
	 $(RM) /bin/braille-ms
	 @echo "success uninstall"
clean:
clean:
		$(RM) $(OBJ)

fclean:		clean
		$(RM) $(NAME)

re:		clean fclean all
