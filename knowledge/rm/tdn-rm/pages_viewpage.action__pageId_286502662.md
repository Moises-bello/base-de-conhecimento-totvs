---
content_hash: b594c388d7692b2383044c923bd85dd41a1343559f08e80015c51740467a8a7f
fetched_at: '2026-06-29T00:08:40.756669+00:00'
page_id: '286502662'
product: rm
source: tdn-rm
title: DT Ajuste de transação Cielo CheckOut
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286502662
version: 105
---

# juste de transação para pagamentos feitos na Cielo-Checkout

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Cadastros Iniciais:** | *Relacione os cadastros necessários que precisam ser preenchidos antes da utilização desse requisito.* |
| **Parâmetro(s):** | *Informe os parâmetros utilizados.* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5FINANCEIRO01-1890 |
| **País(es):** | *BRA* |
| **Banco(s) de Dados:** | *SQL e ORACLE* |
| **Tabelas Utilizadas:** | *FINTEGRACAOCARTAO, FINTEGRACAOHISTORICO* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Implementada melhoria no sistema para que o "Ajuste de Transações" consiga realizar a comunicação com o módulo de pagamento Checkout e realizar as atualizações necessárias no Financeiro.

## Procedimento para Configuração

1. Nos parâmetros do TOTVS Gestão Financeira acesse, **[02.02]** **Contas a Receber | [02.02.02] Baixas | **[02.02.02.03]**Cartão de Crédito/Débito.**

* + Em Configurações Gerais 1/2 marque a opção "Checkout Cielo"

* + Em Configurações Gerais 2/2 configure os campos "Merchantid" e "URL de Post"

**Obs.:**

* Lembrando que o MerchantId será um para cada cliente.
* A opção do Parâmetro "Gravar arquivo de log quando ocorrer erro  no processamento de notificação e mudança de status" é opcional.

2. Acesse **Serviços Globais | Segurança | Perfis,**edite o perfil do usuário logado e localize a permissão **[03.05.02] Ajuste de Transações,** em seguida de permissão ao usuário.

## Procedimento para Utilização

       1.            Acesse o Menu Movimentações Bancárias | Cartão de Crédito/Débito, clique na opção **'Ajuste de Transações'**e execute o processo de ajuste para verificar junto ao site da Cielo o status da transação e atualiza-lo no sistema.

Veja o Menu Movimentações Bancárias | Cartão de Crédito/Débito | Ajuste de Transações

divs
