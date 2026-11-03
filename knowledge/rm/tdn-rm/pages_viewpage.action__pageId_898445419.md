---
content_hash: 1fef5686add833ff8aab6fb78c3556e0061eb5feef77ae4b803fe1b6f14a831f
fetched_at: '2026-06-29T00:12:01.698713+00:00'
page_id: '898445419'
product: rm
source: tdn-rm
title: DT - CNAB240 - Pagamento Eletrônico Itaú
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=898445419
version: 8
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Gerador de Saídas - CNAB 240 - Banco Itaú |
| País: | Brasil |
| Epico: | [DRHCALCRM-7508](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-7508) |

## **02. SITUAÇÃO/REQUISITO**

Cliente solicita que na geração do arquivo bancário **FOPLAY0007 - 09.001.001 Pagamento Eletrônico Itaú.TotvsGen** seja considerado o valor do líquido rescisão após ter executado o processo de lançamento do líquido e zerado o valor do líquido na Ficha Financeira, referenciando o valor lançado no evento de código de cálculo 150.

Cliente solicita que na geração do arquivo bancário **FOPLAY0016 -** **09.001.009 Pagamento Eletrônico Itaú - Férias.TotvsGen** retorna o liquido de férias conforme a data de pagamento, sem a necessidade de cancelar outro período de gozo quando o colaborador tem mais de um período marcado.

## **03. SOLUÇÃO**

Foi alterado o layout Bancário **FOPLAY0007 - 09.001.001 Pagamento Eletrônico Itaú.TotvsGen** para verificar se o funcionário está demitido e existe o evento com código de cálculo 150 e do tipo desconto e considerar o mesmo na geração do arquivo bancário. Quando o funcionário estiver demitido e não existir o evento com código de cálculo 150 irá retornar o valor da função de fórmula L.

Foi alterado o layout Bancário **FOPLAY0016 -** **09.001.009 Pagamento Eletrônico Itaú - Férias.TotvsGen** para considerar a data prevista para pagamento informando no processo de geração que seja igual a data de pagamento de férias e assim o usuário poder cadastrar quantos períodos de gozo desejar, sem a necessidade de cancelar outros períodos de gozo para gerar o liquido bancário.

FOPLAY0007 - 09.001.001 Pagamento Eletrônico Itaú

Gerando arquivo para funcionário demitido com líquido rescisão lançado:

Gerando o arquivo para funcionário demitido sem liquido rescisão lançado:

Gerando para funcionário ativo

 FOPLAY0016 - 09.001.009 Pagamento Eletrônico Itaú - Férias

Colaborador com 2 período de gozo de férias com recibo calculado:

Gerando o líquido bancário e informando a data prevista para pagamento 27/11/2023, conforme o recibo abaixo:

No arquivo gerou o liquido conforme o recibo acima:

Gerando o líquido bancário e informando a data prevista para pagamento 18/12/2023, conforme o recibo abaixo:

No arquivo gerou o liquido conforme o recibo acima:

## **04. DEMAIS INFORMAÇÕES**

Para o arquivo bancário **FOPLAY0016 -** **09.001.009 Pagamento Eletrônico Itaú - Férias.TotvsGen** é considerando somente as férias na situação M ou P. Caso as mesmas já estejam finalizadas não será retornando o valor no arquivo, mesmo que a data prevista para pagamento seja a mesma do recibo de férias.

## **05. ASSUNTOS RELACIONADOS**
