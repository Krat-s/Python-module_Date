import locale
import datetime
from datetime import datetime, timedelta

locale.setlocale(locale.LC_TIME, "pt_BR.utf8")

#arrumando datas
def formatar_data(data):
    dia = int(data.strftime('%d'))
    proximo_dia = int((data + timedelta(days=1)).strftime('%d'))
    proximo_dia_formatado = f"{proximo_dia}º" if proximo_dia == 1 else f"{proximo_dia}"
    dia_formatado = f"{dia}º" if dia == 1 else f"{dia}"
    mes_de_data = data.strftime('%B')
    proximo_mes = (data + timedelta(days=1)).strftime('%B')
    ano_de_data = data.strftime('%Y')
    virada = (data + timedelta(days=1)).strftime('%Y')
     
    formatos_marco_var = {
        1: lambda d: f"{terca_babugado}{dia_formatado} de {marco_babugado}{d.strftime(' de %Y')}",
        5: lambda d: f"fim de semana, {dia_formatado} e {proximo_dia_formatado} de {marco_babugado}{(d + timedelta(days=1)).strftime(' de %Y')}" if mes_de_data == proximo_mes else f"fim de semana, {dia_formatado} de {marco_babugado} e {proximo_dia_formatado} de abril de " + data.strftime('%Y')
    }

    formatos = {
        1: lambda d: f"{terca_babugado}{dia_formatado} de {d.strftime('%B %Y')}",  # Terça-feira
        5: lambda d: f"fim de semana, {dia_formatado} e {proximo_dia_formatado} de {(d + timedelta(days=1)).strftime('%B de %Y')}" # sabado
    }


    if ano_de_data != virada:
        return f"Fim de semana, {dia_formatado} de dezembro de {ano_de_data} e 1º de janeiro {virada}"      
       
    elif data.month == 3:  # Ajuste especial para março
        return f"{data.strftime('%A')}, {dia_formatado} de {marco_babugado} de {data.strftime('%Y')}" if data.weekday() not in formatos else formatos_marco_var[data.weekday()](data)   
   
    elif mes_de_data != proximo_mes and data.month != 3:    
        return f"fim de semana, {dia_formatado} de {mes_de_data} e {proximo_dia_formatado} de {proximo_mes} de {data.strftime('%Y')}" if data.weekday() in formatos else f"{data.strftime('%A')}, {dia_formatado} de {mes_de_data} de {data.strftime('%Y')}"
    
    else: 
        return formatos.get(data.weekday(), lambda d: f"{d.strftime('%A')}, {dia_formatado} de {d.strftime('%B de %Y')}")(data)

   
marco_babugado = r'março'
terca_babugado = r'terça-feira, '
hoje = datetime.now()
amanha = hoje + timedelta(days=1)
ontem = hoje - timedelta(days=1)


#TESTES
especifica = datetime(2029, 3, 31)
especifica_2 = datetime(2025, 5, 31)
teste = datetime(2028, 12, 31)
teste_2 = datetime(2025, 3, 15)


data_de_amanha = formatar_data(amanha)
ontem = formatar_data(ontem)
data_de_hoje = formatar_data(hoje)
data_especifica = formatar_data(especifica)
data_especifica_2 = formatar_data(especifica_2)
teste = formatar_data(teste)
teste_2 = formatar_data(teste_2)


# --------------------testes---------------------
# print("Ontem:", ontem)
# print("Hoje:", data_de_hoje)
# print("Amanhã:", data_de_amanha)
# print("virada de mar/abr:", data_especifica)
# print("virada de mês random:", data_especifica_2)
# print("tests", teste, teste_2)

