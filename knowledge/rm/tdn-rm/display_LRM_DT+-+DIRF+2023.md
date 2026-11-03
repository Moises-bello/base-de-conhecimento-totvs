---
content_hash: 3261e2700df1843e46dad778f53a1a9cc4008492f907f3568d8e77f4aa6da585
fetched_at: '2026-06-29T00:11:28.790181+00:00'
page_id: '733193615'
product: rm
source: tdn-rm
title: DT - DIRF 2023
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+DIRF+2023
version: 21
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | DIRF-Ano Calendário 2022-2023 |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | DRHROTRM-5317 |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.34.269
* 12.1.2205.218
* 12.1.2209.164 ou superiores

## **03. SITUAÇÃO/REQUISITO**

Adequar o produto TOTVS Folha de Pagamento para geração do layout da DIRF 2023, conforme publicação da Receita Federal do Brasil.

## **04. SOLUÇÃO**

Adequação da folha de pagamento para tratar as seguintes alterações:

* Ano Referência: permitir informar '2023'
* Ano-Calendário: permitir informar '2022'
* Campo 'identificador de estrutura do leiaute, preencher o código **ARNZRXP**
* Dados dos Advogados: tratativa para considerar somente o último registro do advogado no histórico do RRA, quando é preenchido mais de um advogado, isso foi necessário, devido o eSocial permitir mais de um advogado, porém a DIRF permitir apenas um.
* Tratativa para considerar os novos códigos de calculo do RRA, sendo eles:

[459 - Diferença Salarial RRA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=715818471)

[460 - INSS de Diferença Salarial RRA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=715818516)

[461 - Diferença de Férias RRA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=725725439)

[462 - INSS de Diferença de Férias RRA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=725725460)

[463 - Diferença de 13º Salário RRA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=721007397)

[464 - INSS de Diferença de 13º Salário RRA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=721007638)

## **05. DEMAIS INFORMAÇÕES**

[DIRF/Informe de Rendimentos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719351)
