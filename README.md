# Explicação de como executar o arquivo .sh;

Para executar o arquivo `calculadora.sh`, siga os passos abaixo:

# Altere as permissões do arquivo para torná-lo executável. 
chmod +x calculadora.sh

# Defina as permissões da seguinte maneira: apenas o proprietário com permissão de escrita e os outros com permissão de leitura. 
chmod 644 calculadora.sh

# Execute o script da calculadora.
bash calculadora.sh

# Explicação do código em python da Calculadora.

# Imprime a mensagem "Calculadora"
print("Calculadora")

# Solicita ao usuário que insira o primeiro número a ser calculado
# Converte o valor inserido para float
numero1 = float(input("Olá, digite o primeiro número que deseja calcular: "))

# Solicita ao usuário que insira a operação desejada (+, -, *, /)
operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

# Solicita ao usuário que insira o segundo número a ser calculado
# Converte o valor inserido para float
numero2 = float(input("Digite o segundo número: "))

# Verifica se a operação escolhida é adição
if operacao == '+':
    # Calcula a soma e armazena o resultado
    resultado = numero1 + numero2

# Verifica se a operação escolhida é subtração
elif operacao == '-':
    # Calcula a diferença e armazena o resultado
    resultado = numero1 - numero2

# Verifica se a operação escolhida é multiplicação
elif operacao == '*':
    # Calcula o produto e armazena o resultado
    resultado = numero1 * numero2

# Verifica se a operação escolhida é divisão
elif operacao == '/':
    # Calcula a divisão e armazena o resultado
    resultado = numero1 / numero2

# Imprime o resultado da operação
print(f"Esse é o seu resultado: {resultado}")

# Indica que o script deve ser executado usando o interpretador Bash.
!/bin/bash

# Imprime a mensagem "Abrindo calculadora.py" no terminal
echo "Abrindo calculadora.py"

# Executa o script Python chamado calculadora.py usando o Python 3
python3 calculadora.py



