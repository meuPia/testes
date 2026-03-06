# meuPia-testes/meupia_testes/plugin_testes.py

def esperar_igual(recebido, esperado, mensagem=""):
    prefixo = f" - {mensagem}" if mensagem else ""
    if recebido == esperado:
        print(f"[TESTE_OK] Sucesso: {recebido} é igual a {esperado}{prefixo}")
        return True
    else:
        print(f"[TESTE_FALHA] Falhou: Esperava '{esperado}', mas recebeu '{recebido}'{prefixo}")
        return False

def esperar_diferente(recebido, esperado, mensagem=""):
    prefixo = f" - {mensagem}" if mensagem else ""
    if recebido != esperado:
        print(f"[TESTE_OK] Sucesso: {recebido} é diferente de {esperado}{prefixo}")
        return True
    else:
        print(f"[TESTE_FALHA] Falhou: Esperava algo diferente de '{esperado}', mas recebeu exatamente isso{prefixo}")
        return False

def esperar_verdadeiro(condicao, mensagem=""):
    prefixo = f" - {mensagem}" if mensagem else ""
    if condicao:
        print(f"[TESTE_OK] Sucesso: Condição é verdadeira{prefixo}")
        return True
    else:
        print(f"[TESTE_FALHA] Falhou: Esperava verdadeiro, mas recebeu falso{prefixo}")
        return False

def esperar_falso(condicao, mensagem=""):
    prefixo = f" - {mensagem}" if mensagem else ""
    if not condicao:
        print(f"[TESTE_OK] Sucesso: Condição é falsa{prefixo}")
        return True
    else:
        print(f"[TESTE_FALHA] Falhou: Esperava falso, mas recebeu verdadeiro{prefixo}")
        return False

def esperar_maior(recebido, limite, mensagem=""):
    prefixo = f" - {mensagem}" if mensagem else ""
    if recebido > limite:
        print(f"[TESTE_OK] Sucesso: {recebido} é maior que {limite}{prefixo}")
        return True
    else:
        print(f"[TESTE_FALHA] Falhou: Esperava um valor maior que {limite}, mas recebeu {recebido}{prefixo}")
        return False

def esperar_menor(recebido, limite, mensagem=""):
    prefixo = f" - {mensagem}" if mensagem else ""
    if recebido < limite:
        print(f"[TESTE_OK] Sucesso: {recebido} é menor que {limite}{prefixo}")
        return True
    else:
        print(f"[TESTE_FALHA] Falhou: Esperava um valor menor que {limite}, mas recebeu {recebido}{prefixo}")
        return False

def esperar_contem(colecao, item, mensagem=""):
    prefixo = f" - {mensagem}" if mensagem else ""
    if item in colecao:
        print(f"[TESTE_OK] Sucesso: O item '{item}' foi encontrado na coleção{prefixo}")
        return True
    else:
        print(f"[TESTE_FALHA] Falhou: O item '{item}' não existe em {colecao}{prefixo}")
        return False