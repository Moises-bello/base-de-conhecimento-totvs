---
content_hash: 74542ab80059fa7f679bf8f8d83cdba148adaf70421b93235d52dd324c754939
fetched_at: '2026-06-29T00:12:02.644881+00:00'
page_id: '901968792'
product: rm
source: tdn-rm
title: DT - Encargos - Reoneração da Folha de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901968792
version: 10
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Geração de Encargos |
| País: | Brasil |
| Issue: | [DRHCALCRM-7565](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-7565) |

## **02. VERSÕES**

A solução está disponível a partir dos patchs/release abaixo:

* 12.1.2402.274
* 12.1.2406.234
* 12.1.2410.165
* 12.1.2502.100

## **03. SITUAÇÃO/REQUISITO**

A Lei nº 14.973, de 16 de setembro de 2024, introduz a reoneração progressiva, que visa a reversão gradual da desoneração da folha de pagamento, impactando 17 setores específicos da economia. Essa medida substitui a desoneração, permitindo que as empresas, após um período de transição, voltem a contribuir com alíquotas mais altas de contribuição previdenciária. 

No entanto, o processo de encargos não contemplam de forma nativa a reoneração progressiva da folha de pagamento, deixando para o usuário a responsabilidade de implementar essas mudanças de forma manual ou por meio de fórmulas de cálculo customizadas.

## **04. SOLUÇÃO**

Foi adequado a geração de encargos para contemplar de forma nativa o cálculo de recolhimento de INSS patronal conforme estabelecido pela **Lei nº 14.973, de 16 de setembro de 2024**, evitando erros, garantindo conformidade nos valores calculados e minimizando riscos operacionais.

A solução está disponível somente para os encargos abaixo:

* 3 - Base: incidência de INSS
* 6 - Provisão de encargos de férias
* R - Base: incidência de INSS Dissídio
* T - Base: incidência de INSS DCTFWeb (a partir da 12.1.2410)

Mais informações:   
  
**05. ASSUNTOS RELACIONADOS**

* [Encargos](https://tdn.totvs.com.br/display/public/LRM/Encargos+-+Folha+de+Pagamento?draft=true)
