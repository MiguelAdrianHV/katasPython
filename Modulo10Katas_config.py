def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print('El archivo congfig.txt no se encontro')
    except IsADirectoryError:
        print('config.txt se encontro pero es una direccion')
    except PermissionError:
        print('config.txt se encontro pero no se puede leer')
    except (BlockingIOError, TimeoutError):
        print("archivo con carga pesada, no se puede leer")


if __name__ == '__main__':
    main()
