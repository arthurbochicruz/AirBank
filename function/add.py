from datetime import date
current_year = date.today().year

def line_divider():
    print('-=' * 30)

def age_calculator(date_said):
    try:
        date_said = str(date_said)
        if not date_said.isdigit() or len(date_said) != 4:
            return 'Digite sua data de nascimento corretamente com 4 números.', True
        date_said = int(date_said)

        if date_said <= 1900:
            return 'Sua resposta não tem lógica, improvavel que o usuário tenha nascido em 1900!', True
        
        elif date_said > current_year:           
            return 'Não é possivel que a pessoa tenha nascdo depois do ano atual!', True

        else:
            real_age = current_year - date_said
            return real_age, False

    except ValueError:
        return 'ERRO valor inválido, digite corretamente o ano de nascimento do usuário.', True

def registration_verification_holder(registration_verification_value_holder):

    if registration_verification_value_holder.isalpha():
        return registration_verification_value_holder
    else:
        
        print('Digite corretamente!')

def registration_verification_age(registration_verification_value_age):
    registration_verification_value_age = str(registration_verification_value_age)

    if registration_verification_value_age.isdigit():
        registration_verification_value_age = int(registration_verification_value_age)
        
        if registration_verification_value_age >= 12 and registration_verification_value_age < 18:
            return registration_verification_value_age, 'Você tem condições de entrar ao AirBank jovem', False
        
        elif registration_verification_value_age <= 11:
            return registration_verification_value_age, 'Você é menor de idade, Você não se encaicha ao AirBank jovem.', True

        else:
            return registration_verification_value_age, 'Idade ok', False

    else:
        return "Digite apenas números!", 'Não digitou corretamente', False

def registration_verification_cpf(registration_verification_value_cpf):
    if registration_verification_value_cpf.isdigit():
        return registration_verification_value_cpf
    else:
        return "Digite corretamente o CPF!"
