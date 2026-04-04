from function.add import age_calculator, line_divider, registration_verification_holder, registration_verification_age, registration_verification_cpf
import createBank

class User:
    def __init__(self, titular="", idade=0, withdrawal_deposit_available=1000, cpf=00000000000):
        self.titular = titular
        self.idade = idade
        self.saldo = withdrawal_deposit_available
        self.cpf = cpf

    def sacar(self, withdrawal_amount):
        withdrawal_amount = self.saldo - withdrawal_amount
        return withdrawal_amount

    def deposito(self, available_deposit, amount_to_deposit):
        available_deposit = available_deposit + amount_to_deposit
        return available_deposit

line_divider()
print('- AIR BANK -')
while True:
    AdminRespost = input('Quer cadastrar uma nova conta[S/N]: ').upper()
    if AdminRespost == "S":
        while True:
            
            titular = input('Cadastre um usuario: ')
            titular = registration_verification_holder(titular)

            while True:
                idade = str(input('Digite o ano de nascimento do usuario: '))    
                idade_real, errorAge = age_calculator(idade)
                if errorAge == True:
                    print(idade_real)
                else:
                    idade_real, condicion, insufficientAgeError = registration_verification_age(idade_real)
                    if insufficientAgeError == True:
                        print(condicion)
                    else:
                        print(condicion)
                        break    

            cpf = str(input('Digite seu CPF: '))
            cpf = registration_verification_cpf(cpf)
            saldo = 1000

            

            
            if insufficientAgeError == True:
                print(idade_real)

            else:
                user = User(titular, idade_real, saldo, cpf)
                break
        break
    
    if AdminRespost == "N":
        print('Ok você esta logado na conta Admin do banco!')
        break
    elif AdminRespost != "S" and AdminRespost != "N":
        print('Erro digite corretamente!')
        

print('Seu saldo é de R$ 1,000.00 reais \n')
line_divider()
print("""
      Oque você quer fazer com seu dinheiro?

        1 - Sacar
        2 - Depositar
        3 - Manter
        4 - Deletar usuario já existente
        5 - Atualizar o saldo
     """)
line_divider()
response = int(input('digite sua escolha: '))
withdrawal_deposit_available = 1000
if response == 1:
    withdrawal_amount = float(input('Quanto você deseja Sacar?: '))
    withdrawal_deposit_available = user.sacar(withdrawal_amount)
 
elif response == 2:
    
    print('Você tem disponivel R$ 1,000.00 reais')
    amount_to_deposit = float(input('Quanto deseja depositar?: '))
    if amount_to_deposit > withdrawal_deposit_available:
        print(f'Você tem {withdrawal_deposit_available} disponivel para deposito, valor não valido.')
    else:
        withdrawal_deposit_available = user.deposito(withdrawal_deposit_available, amount_to_deposit)

elif response == 4:
    if AdminRespost == "N":
        print('Este são os dados das contas: \n')
        createBank.encapsulating_data()
        while True:
            try:
                userToBeDeleted = int(input('Qual usuário você deseja deletar?(COM BASE NO ID DOS USUÁRIOS QUE FOI MOSTRADO A CIMA): '))
                updateDelete = createBank.deleteUsers(userToBeDeleted)
                print(f'Você deletou o usuario \n {updateDelete}')
                break
            except ValueError:
                print('[ERROR: Valor Invalido] Não é possivel digitar um número quebrado, se só é possivel números inteiros')
    else:
        print('Você não esta logado na conta Admin, você não tem acesso a esta opção!')

elif response == 5:
    if AdminRespost == "N":
        print('Este são as contas: \n')
        createBank.encapsulating_data()        
        while True:
            try:
                userToBeUpdated = int(input('Qual usuário você deseja aualizar o saldo?(COM BASE NO ID DOS USUÁRIOS QUE FOI MOSTRADO A CIMA): '))
                UserBalanceValueToBeUpdated = float(input('Para quanto você deseja alterar?: '))
                newBalance = createBank.updatingBalance(userToBeUpdated, UserBalanceValueToBeUpdated)
                print('O novo(s) usuário(s) atualizado(s):')
                print(newBalance)
                break 
            except ValueError:
                print('[ERROR: Valor Invalido] Não é possivel digitar este valor!')
                
elif response != 1 and response != 2 and response != 3 and response != 4 and response != 5:
    print('Digite corretamentea sua escolha!')
else:
     print('Terminando programa')
if AdminRespost == 'S':
    user = User(titular, idade_real, withdrawal_deposit_available, cpf)
    createBank.inserir_usuario(user.titular, user.idade, user.saldo, user.cpf)
