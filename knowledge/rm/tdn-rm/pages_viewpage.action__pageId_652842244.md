---
content_hash: 5f468e8ef0ba1f9a4812130491d343c4f51bb34df6021db53a108ea1b11fa707
fetched_at: '2026-06-29T00:11:12.431097+00:00'
page_id: '652842244'
product: rm
source: tdn-rm
title: S-2230 e S-2231- Como retificar a data inicial de um afastamento temporário?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=652842244
version: 12
---

false

**A partir das Versões:**

* **12.1.31.271**
* **12.1.32.216**
* **12.1.33.144**
* **e Superiores**

# Objetivo:

---

O objetivo deste documento é apresentar o novo processo de alteração da data inicial do afastamento no cadastro do histórico de afastamento do funcionário.

---

11ParametrizaçãoParametrização

1) Execute a atualização da base pelo aplicativo RM.Atualizador.exe

2) Acesse o menu Serviços Globais| Segurança | Perfis

Selecione o sistema Folha de pagamento, edite o perfil desejado, vá em acesso aos menus e permita o acesso 01.01.01.257 Histórico Afastamento: Alterar Data Início do Afastamento.

2Alteração do AfastamentoAlteração do Afastamento

1) Acesse o menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários, selecione o funcionário desejado e acesse Anexos | Históricos | Histórico de Afastamentos

2) Selecione o afastamento desejado para realizar a alteração e acesse Processos |  Alterar Data Início do Afastamento

3) Cadastre a nova data desejada e clique em executar

## **eSocial**

Após a execução da alteração da data do afastamento, o sistema irá verificar se existe evento o S-2230 ou S-2231 para este afastamento com com status "10-Aceito RET", caso tenha será gerado um gatilho de retificação para o evento e o campo "Data Início Afastamento" será ajustado nos dois gatilhos (Inclusão e Retificação)

Antes da execução do processo: 

Após a execução do processo:
