---
content_hash: a8ae12a76c5f60a3234b07b78dde956d3f551f03cc35f344a24ca3042b8d4fe4
fetched_at: '2026-06-29T00:08:16.542624+00:00'
page_id: '247924834'
product: rm
source: tdn-rm
title: TUVOT6_DT_Criacao_NovoCC_Salario_Maternidade_Complementar
type: documentation
url: https://tdn.totvs.com/display/LRM/TUVOT6_DT_Criacao_NovoCC_Salario_Maternidade_Complementar
version: 1
---

# CRIAÇÃO DE NOVO CÓDIGO DE CÁLCULO PARA SALÁRIO MATERNIDADE COMPLEMENTAR

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Afastamento* | *Histórico de Afastamento* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Afastamento** | *Histórico de Afastamento* | | **Férias**  *Folha Mensal* | **Lançamento das Férias**  *Cálculo da Folha Mensal* | |
| **Cadastros Iniciais:** | *Cadastro de Evento* |
| **Parâmetro(s):** | *Tipo do Afastamento* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *TUVOT6* |
| **Requisito (ISSUE):** | *Folha* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server, Oracle* |
| **Tabelas Utilizadas:** | *PCODSITUACAO, PCODAFAST, PEVENTO* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Durante o período de afastamento do tipo W - Licença Maternidade Complementar, a funcionária estava recebendo o salário através dos Códigos de Cálculo 1 ou 2.

Conforme a Lei, "A pessoa jurídica tributada com base no lucro real poderá deduzir do imposto devido, em cada período de apuração, o total da remuneração integral da empregada pago nos 60 (sessenta) dias de prorrogação de sua licença-maternidade, vedada a dedução como despesa operacional".

Com o cálculo sendo feito nos eventos de CC's 1 ou 2 ficava complicado de separar o valor para fazer a dedução.

Foi implementado o novo CC 352 - SALÁRIO MATERNIDADE COMPLEMENTAR, para lançar somente o valor referente ao período de afastamento tipo W.

Este evento terá as mesmas características do eventos de remuneração, CC's 1 e 2.
