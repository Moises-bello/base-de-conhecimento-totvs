---
content_hash: cc3fa2312ea92e517a4f8e91e637ab53a06ef74928d6cf4a2dc09d942857a8f6
fetched_at: '2026-06-29T00:06:10.506880+00:00'
page_id: '203763548'
product: rm
source: tdn-rm
title: DT_Solicitar_Login_e_Senha_ao_Criar_Requisição_de_Estoque
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=203763548
version: 2
---

# Solicitar login/senha ao criar uma requisição de estoque

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Estoque |
| **Rotina:** | |  | | --- | | **Rotina** | | Movimentação de estoque |  |  | | --- | | **Rotina(s) envolvida(s)** | | Parâmetros gerais | | Parâmetros por estação de trabalho | |
| **Parâmetro(s):** | Parâmetros gerais/Estoques II/Solicita Login/Senha ao criar uma nova requisição  Parâmetros por estação de trabalho/Não exige login ao criar nova requisição |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e ORACLE |
| **Sistema(s) operacional(is):** | Windows |
| **Versões/Release:** | 12.1.8 |

## Descrição

 

Foi realizada a criação de dois parâmetros:

* ****Solicita login/senha ao criar uma nova requisição**** em**Opções/Parâmetros/Parâmetros Gerais/Estoques II.**
* **Não exige login ao criar nova requisição** em **Opções/Parâmetros/Parâmetros por estação de trabalho**.

Ao criar uma nova requisição de estoque, no momento de salvar, o sistema realizará a validação dos parâmetros acima e solicitará (ou não, dependendo da configuração dos parâmetros) um login/senha para prosseguir. O usuário informado no login, ficará salvo na tabela da requisição de estoque e na tabela dos itens da requisição na coluna RECCREATEDBY.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação da release 12.1.8

1. Aplique o pacote da release 12.1.8 e execute o agendamento de exames pela assistente

## Procedimento para Utilização

       1.            Na tela de Parâmetros gerais **Opções/Parâmetros/Parâmetros Gerais/Estoques II** marque o parâmetro chamado "**Solicita login/senha ao criar uma nova requisição**".

       2.            Na tela de Parâmetros por estação de trabalho **Opções/Parâmetros/Parâmetros por estação de trabalho** marque o parâmetro chamado "**Não exige login ao criar nova requisição**".

       3.            Na tela de movimentação de estoque **Estoque/Movimentação de estoque** crie uma nova requisição.

       4.            Preencher os dados da requisição e ao sair do campo **Requisitado por** o sistema salva a requisição. Neste momento, caso os parâmetros acima estejam marcados, será exibida uma tela para informar o login e senha do usuário que está criando a requisição.
