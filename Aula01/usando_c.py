#usar o comando de importação para a biblioteca criada
import ctypes

lib = ctypes.CDLL("./mensagem.so")
lib.mensagem()