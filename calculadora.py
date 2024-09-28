print ("Calculadora")
numero1 = float(input("Olá, digite o primeiro número que deseja calcular: "))
operacao = input("Digite a operação que deseja realizar (+, -, *, /):")
numero2 = float(input("Digite o segundo número: "))
if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    resultado = numero1 / numero2
print(f"Esse é o seu resultado: {resultado}")
