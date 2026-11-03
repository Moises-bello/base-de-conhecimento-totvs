---
content_hash: bcb27f3b3f6a356c8a5b72a8808f6c1dcd07414cd6179bf3666539b811ecc04c
fetched_at: '2026-06-29T00:05:51.076102+00:00'
page_id: '1046824604'
product: rm
source: tdn-rm
title: DT - DIRF 2026 - Órgão Público Portaria RFB nº 632
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1046824604
version: 7
---

## **01. DADOS GERAIS**

| Produto: | TOTVS - Folha de Pagamento |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | DIRF 2026 - Órgão Público Portaria RFB nº 632 |
| País: | Brasil |
| Ticket: |  |
| Issue: | [DRHROTRM-17626](https://jiraproducao.totvs.com.br/browse/DRHROTRM-17626 "View this issue") |

## **02. VERSÕES**

A partir dos patches:

* 12.1.2502.294
* 12.1.2506.264
* 12.1.2510.185
* 12.1.2602.108e superiores

## **03. SITUAÇÃO/REQUISITO**

A Receita Federal do Brasil publicou a [Portaria RFB nº 632, de 30 de dezembro de 2025](https://www.totvs.com/blog/fiscal-clientes/esocial-instituido-programa-receita-social-autorregularizacao/), que institui o Programa Receita Social de Autorregularização, direcionado aos órgãos públicos da União, Estados e Municípios que enfrentam dificuldades técnicas para realizar a escrituração das informações no eSocial. Diante disso se faz necessário permitir a geração da DIRF o ano-base 2026 (ano-calendário 2025) para essa situação.

## **04. SOLUÇÃO**

O sistema passou a permitir a geração da DIRF ano-calendário 2025 para atender ao disposto na **Portaria RFB nº 632.**

Ao selecionar o ano **2025**, será apresentada a seguinte mensagem:

Para que a geração esteja em conformidade com a definição prevista na Portaria, após a geração do arquivo da DIRF será necessário realizar um ajuste manual no arquivo.

Deverá ser editada a **primeira linha do arquivo**, alterando o campo **“Identificador de estrutura do leiaute”**, informando o código específico fornecido pela Receita Federal, uma vez que esse código é **único por cliente**.

A alteração deve ser realizada nas **posições 7 a 13** do registro, conforme demonstrado abaixo:

## **05.****ASSUNTOS RELACIONADOS**
