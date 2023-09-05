mensagem = 'eu adoro comida Caseira'

print(mensagem)
print(mensagem.lower())  # Retorna toda a string com letras minúsculas
print(mensagem.upper())  # Retorna toda a string com letras maiúsculas
print(mensagem.capitalize())  # Retorna a primeira letra da string com maiúsculo
print(mensagem.find('aDoro'))  # -1 significa que não encontrou o que estávamos procurando
print(mensagem.replace('Caseira', 'feita em casa'))  # Substitui uma letra/palavra pela outra

print(mensagem.strip())  # Remove os espaços em branco no início e no final da string
