---
content_hash: 6dc0a8afe143cddf9edd34be8a5f73d82e6d3798306b48a1c7dded9576a193e0
fetched_at: '2026-06-29T00:05:51.791247+00:00'
page_id: '1056118083'
product: rm
source: tdn-rm
title: DT - Arredonda INSS teto quando funcionário possui outro vínculo de terceiros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056118083
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Parametrizador |
| País: | Brasil |
| Ticket: | [#23184373](https://totvssuporte.zendesk.com/agent/tickets/23184373) |
| Issue: | [DRHCALCRM-8456](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-8456) |

## **02.****VERSÕES**

A partir dos patches:

* + 12.1.2506.285
  + 12.1.2510.206
  + 12.1.2602.126
  + 12.1.2606 e superiores

## **03. SITUAÇÃO/REQUISITO**

Ao calcular folha da competência 03/2025 para um funcionário que tenha outro vínculo externo e a soma das bases dos dois vínculos é atingido o teto do limite de contribuição de INSS, o RM está arredondando a 4 faixa do cálculo do INSS, causando diferença de valores com o governo, visto que o eSocial trunca todas as faixas de cálculo.

## **04. SOLUÇÃO**

Realizada a alteração conforme orientação da conclusão da Consultoria com o cálculo sendo feito sobre cada faixa e o truncamento ocorrerá após a segunda casa decimal.  
Link: [https://tdn.totvs.com/pages/viewpage.action?pageId=525805955&amp;preview=/525805955/714235525/Orienta%C3%A7%C3%A3o%20Consultoria%20de%20Segmentos%20%E2%80%93%207495069%20-%20Novo%20C%C3%A1lculo%20de%20INSS%20com%20a%20Reforma%20da%20Previd%C3%AAncia%20-%20V.9.docx.pdf](https://tdn.totvs.com/pages/viewpage.action?pageId=525805955&preview=/525805955/714235525/Orienta%C3%A7%C3%A3o%20Consultoria%20de%20Segmentos%20%E2%80%93%207495069%20-%20Novo%20C%C3%A1lculo%20de%20INSS%20com%20a%20Reforma%20da%20Previd%C3%AAncia%20-%20V.9.docx.pdf "Follow link")

Realizada a criação do parâmetro "Arredonda INSS teto quando funcionário possui outro vínculo de terceiros" em Folha Normal / Encargos Sociais para o caso de entendimento que o arredondamento deve continuar sendo realizado.

## **05. ASSUNTOS RELACIONADOS**

* [Encargos Sociais](https://tdn.totvs.com.br/display/public/LRM/Encargos+Sociais)
