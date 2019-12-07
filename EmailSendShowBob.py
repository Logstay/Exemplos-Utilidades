# encode-UTF-8
# enviando emails com python
# esse modo precisa habilitar nas opções da conta google.

import smtplib, ssl

smtp_server = 'smtp.gmail.com'
port = 465
# colocar seu email de remetente
remetente = 'kaiquepng@gmail.com'
senha = input('Insira sua senha: ')
# colocar email de recptor
receptor = 'kaiquepng@hotmail.com'
mensagem = 'mensagem enviada de um app python1'
print(mensagem.encode('utf-8', errors='ignore'))

context = ssl.create_default_context()

# outro modo de envio
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(remetente, senha)
    server.sendmail(remetente, receptor, mensagem)




# outro modo de envio
'''try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(remetente, senha)
    # enviando
    print('Quebrou')
except Exception as e:
    print(e)
finally:
    server.quit()'''
