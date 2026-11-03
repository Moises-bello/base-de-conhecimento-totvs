---
content_hash: 7ec31a87f2470eb14323b08d782dae98ff04b089ee4926320bf5e525756bd69d
fetched_at: '2026-06-29T00:10:23.135951+00:00'
page_id: '499113383'
product: rm
source: tdn-rm
title: FISCAL01-7848 DT Apuração da CPRB Regime de Caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=499113383
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão fiscal |
| Função: | Apuração do Tributo Contribuição Previdenciária |
| Requisito/Story/Issue (informe o requisito relacionado) : | FIS000407 |

## **02. SITUAÇÃO/REQUISITO**

Apurar o tributo contribuição previdenciária por regime de caixa.

## **03. SOLUÇÃO**

* O Tributo será calculado automaticamente com o Valor Baixado (Recebido) retornado pelo Gestão Financeira.
* Os lançamentos financeiros provenientes da Gestão Fiscal também estarão com o campo Código de Atividade vazio. Nestes casos o Fiscal irá buscar os respectivos lançamentos fiscais através do relacionamento entre IDLAF e IDLAN e, consequentemente, os itens e seus respectivos Códigos de Atividade.
* Os lançamentos financeiros provenientes do SGI ou incluídos manualmente no Financeiro devem ser retornados com os Códigos de Atividade.
* O serviço deve considerar os **Lançamentos Financeiros a Receber** que foram baixados dentro do Período considerando as Filiais e os Tipos de Documentos que foram passados como parâmetro.
* Para os Tipos de Documentos que tenham a Classificação de “**Devolução**” devem ser selecionados os **Lançamentos Financeiros a Pagar**. Esses valores representarão cancelamentos de recebimentos (devoluções) que serão considerados como Exclusão da receita.
* As considerações para a Apuração do Tributo devem ser iguais às apresentadas na Documentação do Bloco P da Rotina EFD Contribuições.
* A Base de Cálculo do Tributo corresponderá ao Valor Baixado no período por Código de Atividade. Durante o rastreamento do Movimento para identificação dos Itens, se forem encontrados mais de um item no Movimento com Códigos de Atividades diferentes, o valor baixado precisará ser proporcionalizado para cada item do movimento em relação ao total do movimento.
* A alíquota do tributo será carregada a partir do Cadastro de Código de Atividade.
* No cadastro da filial em dados fiscais na aba Tributo poderá ser selecionado o tipo de apuração da contribuição previdenciária se é Regime Caixa ou Competência.

Observação: Quando o Lançamento Financeiro tem como origem Lançamento Fiscal ou Movimento  é necessário informar o tributo Contribuição Previdenciária nos Itens para que seja possível recuperar o código da receita.
