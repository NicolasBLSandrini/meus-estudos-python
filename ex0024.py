cidade=str(input('Digite o nome de uma cidade: '))
cidade=cidade.lower()
cidade=cidade.strip()

print('O nome da cidade começa com "Santo" {}'.format(cidade.startswith('santo')))
