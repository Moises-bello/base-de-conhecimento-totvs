---
content_hash: eead8bfb7988f38ce8d5bd84a89cdc36bba80f26616a0b9d8c87c0fde3a2efcb
fetched_at: '2026-06-29T00:08:45.338983+00:00'
page_id: '311625508'
product: rm
source: tdn-rm
title: DT Evolução do registro online de boletos para utilizar a parametrização definida
  no convênio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=311625508
version: 101
---

# Utilização das configurações definidas na parametrização associada ao convênio, para registro online de boletos.

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Registro Online* | *Registro Online de Boletos.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Banco** | *Banco* | | Agência | Agência | | Convênio | Convênio | | Registro Online | Registro Online | |
| **Cadastros Iniciais:** | *Bancos e, agências, conta corrente, conta caixa e convênio.* |
| ****Requisito/S****tory/Issue (informe o requisito relacionado):**** | *<http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-2945>* |
| **Banco(s) de Dados:** | *SQL e Oracle* |
| **Tabelas Utilizadas:** | *FCONVENIO, FBONCOLAYOUTONLINE, FCONVENIOCAMPOFORMULA* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Evolução no processo de registro online de boletos para que os bancos utilizem as configurações definidas na parametrização de associação de campos do convênio para a geração dos dados enviadas ao banco.

Obs.: A inclusão de uma TAG (Campo) já preenchida como default pelo sistema, irá apenas substituir o valor que será parametrizado.

## Procedimento para Utilização

* + Realize o cadastro de um novo campo de acordo com a documentação:  [DT Cadastro de Layout do Registro Online](http://tdn.totvs.com/display/LRM/DT+Cadastro+de+Layout+do+Registro+Online).
  + Realize o cadastro de um novo campo de acordo com a documentação: .  
    A tag deverá ser cadastrada conforme exemplo do banco itau :
* Seguindo a configuração do manual de cada banco, exemplo do banco Itaú:

Exemplo banco santander:

**Campo:**

**Layout:**

divs
