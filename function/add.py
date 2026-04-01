from datetime import date
current_year = date.today().year
error = 0

def reset_error():
    global error
    error = 0

def error_function():
    return error

def line_divider():
    print('-=' * 30)

def age_calculator(date_said):
    global error

    date_said = str(date_said)

    if not date_said.isdigit() or len(date_said) != 4:
        error -= 1
        return 'Digite sua data de nascimento corretamente com 4 números.'

    date_said = int(date_said)
    real_age = current_year - date_said

    return real_age

def registration_verification_holder(registration_verification_value_holder):
    global error

    if registration_verification_value_holder.isalpha():
        return registration_verification_value_holder
    else:
        error -= 1
        print('Digite corretamente!')

def registration_verification_age(registration_verification_value_age):
    global error
    registration_verification_value_age = str(registration_verification_value_age)
    if registration_verification_value_age.isdigit():
        registration_verification_value_age = int(registration_verification_value_age)
        
    
        if registration_verification_value_age >= 12 and registration_verification_value_age < 18:
            return 'Você tem condições de entrar ao AirBank jovem'
        
        elif registration_verification_value_age <= 11:
            return 'Você é menor de idade, Você não se encaicha ao AirBank jovem.'

        else:
            return registration_verification_value_age

    else:
        error -= 1
        print("Digite apenas números!")

def registration_verification_cpf(registration_verification_value_cpf):
    if registration_verification_value_cpf.isdigit():
        return registration_verification_value_cpf
    else:
        return "Digite corretamente o CPF!"
