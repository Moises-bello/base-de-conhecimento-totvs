---
content_hash: 808d02cb6f2ca58d485bcd1bdc8e9c7683d9c1cfd9ab6db97631d5a4d4a14d00
fetched_at: '2026-06-29T00:09:12.210903+00:00'
page_id: '416842135'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-3377 DT Evento contábil para lançamentos de bolsa de crédito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=416842135
version: 2
---

# EVENTO CONTÁBIL PARA LANÇAMENTOS DE BOLSA DE CRÉDITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Gestão Educacional* |
| **Módulo:** | **TOTVS Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Geração de Lançamentos* | *Geração de Lançamentos* | |
| **Cadastros Iniciais:** | *Contrato, Parcela, Bolsa de Crédito* |
| **Parâmetro(s):** | **Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin - Geral 2/4 | Evento p/ inclusão de bolsa de crédito** |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | **DEDUINTEGRACOES-3377** |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *N/A* |
| **Tabelas Utilizadas:** | *N/A* |
| **Sistema(s) Operacional(is):** | *N/A.* |

**Objetivo**

Com o objetivo de flexibilizar a contabilização dos lançamentos de bolsa de crédito, foi criado o parâmetro "Evento p/ inclusão de bolsa de crédito" em Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin - Geral 2/4. Isso dá mais liberdade para contabilização desses lançamentos utilizando o regime de caixa já que podemos ter eventos específicos para a contabilização dos lançamentos do aluno e lançamentos de bolsa de crédito o que possibilita a simplificação dos eventos contábeis e melhoria de performance pois as diferentes condições de contabilização não precisam ser tratadas via fórmula.

**Parâmetro**

**Descrição**

Anteriormente, o evento contábil do lançamento de bolsa de crédito era o mesmo evento contábil do lançamento do aluno conforme o parâmetro "Evento p/ inclusão do lançamento".

As diferentes regras para se contabilizar os lançamentos dos alunos e lançamentos de bolsa de crédito eram feitas, muitas das vezes, via fórmula o que prejudicava a performance de contabilização da geração de lançamentos como um todo pois, a geração de qualquer lançamento contábil, executava todas as contabilizações parametrizadas no evento contábil de inclusão do lançamento do aluno (lançamento principal).

Com a criação do parâmetro "Evento p/ inclusão de bolsa de crédito", os lançamentos de bolsa de crédito serão gerados com o evento contábil selecionado nesse parâmetro. Caso o mesmo não tenha um valor selecionado, o evento contábil do lançamento de bolsa de crédito será o mesmo evento contábil do lançamento do aluno.

ATENÇÃO

O evento contábil considerado é o evento contábil de inclusão. Caso o usuário queira utilizar esse evento contábil na baixa do lançamento de bolsa de crédito, deverá parametrizar a utilização do mesmo nos parâmetros do TOTVS Gestão Financeira.

Para mais informações sobre como configurar o evento contábil de baixa, acesse o link: <http://wikihelp.totvs.com.br/WikiHelp/FIN/FIN.IntegracaoContabilParam.aspx>
