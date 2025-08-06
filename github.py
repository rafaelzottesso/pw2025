import os

email = "rafael.zottesso@ifpr.edu.br"

msg_commit = ""
while(len(msg_commit)<10):
    msg_commit = input("Mensagem do commit (maior que 10 caracateres): ")

print("\n\nConfigurando email...")
comando = f"git config user.email \"{email}\""
os.system(comando)

print("\nAdicionando mudanças e realizando commit...")
comando = "git add *"
os.system(comando)
comando = f"git commit -m \"{msg_commit}\""
os.system(comando)

print("\nEnviando ao GitHub. Abra a outra janela para se autenticar...")
comando = "git push"
os.system(comando)

print("\nEnvio realizado com sucesso...")
