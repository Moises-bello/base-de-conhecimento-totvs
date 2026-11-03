---
content_hash: ad2720345d4635b8315fee36e1e24ade966e0817978e51f9a3cb6542e4f3a054
fetched_at: '2026-06-29T00:06:20.089520+00:00'
page_id: '221548624'
product: rm
source: tdn-rm
title: TTUP95_DT_Relatorio_Espelho_Ponto
type: documentation
url: https://tdn.totvs.com/display/LRM/TTUP95_DT_Relatorio_Espelho_Ponto
version: 2
---

# RELATÓRIO ESPELHO DE PONTO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *TOTVS Automação de Ponto* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Geração do relatório de espelho do cartão.* | *Relatório do espelho do cartão.* | |
| **Parâmetro(s):** | *Informar no passo 3 da geração do relatório do espelho do cartão a opção de ordenação por 'Nome'.* |
| **Chamados Relacionados** | *TTUP95* |
| **País(es):** | *Todos países.* |
| **Tabelas Utilizadas:** | *ABATFUN, AHORARIO, AOCORRENCIACALCULADA, GCOLIGADA, PFUNC, AABONOCALCULADO, AEVECALC, AJORNADACALCULADA, AMOVFUN, AOCORRENCIACALCULADA, ASALDOBANCOHORFUNDETALHE* |
| **Versões/Release:** | *12.1.9* |

## Descrição

Foi implementada a opção de ordenação da impressão do relatório de espelho do cartão por nome.

## Procedimento para Utilização

* Passos para usufruir da implementação:

  1 - Acessar o contexto TOTVS Automação de Ponto através da MDI;

  2 - Deverá importar na base de dados a última versão do relatório de espelho PTOREL01.0001 - Espelho de Cartão de Ponto que já contemple a ordenação da impressão;

  3 - Acessar o menu "Relatórios->Espelho do cartão" e efetuar a geração do espelho com todas as possíveis ordenações inclusive com a nova opção 'NOME'.

divs
