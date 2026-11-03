---
content_hash: 2c88ec7b90574eab399f46f70013bacf33c0427d0d22eb43e02c51f2ea8d5fb7
fetched_at: '2026-06-29T00:11:29.247774+00:00'
page_id: '735439697'
product: rm
source: tdn-rm
title: DT - Informe de Rendimentos - Usar Responsável da DIRF em Arquivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=735439697
version: 17
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Informe de Rendimentos |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-232](https://jiraproducao.totvs.com.br/browse/DRHROTRM-232) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2209.169 ou superiores

## **03. SITUAÇÃO/REQUISITO**

Adequar o produto de acordo com a INSTRUÇÃO NORMATIVA RFB Nº 1682, DE 28 DE DEZEMBRO DE 2016, para gerar o campo "8-Responsável pelas Informações" do informe de rendimentos com os dados do responsável informado no parâmetro "DIRF em Arquivo" ao invés de buscar as informações da Coligada.

## **04. SOLUÇÃO**

Disponibilizado o parâmetro "Usar Responsável (DIRF arquivo) na geração do Informe de Rendimentos", nas "Opções de Seleção" da Geração da DIRF e Informe de Rendimentos, conforme print abaixo:

Com este parâmetro marcado, o campo "8-Responsável pelas Informações" do Informe de Rendimentos passa a gerar as informações cadastradas na aba "Responsável" da DIRF em arquivo, caso contrário serão geradas as informações preenchidas na Coligada.

   Informe de Rendimentos

## **05. DEMAIS INFORMAÇÕES**

[DIRF/Informe de Rendimentos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719351)
