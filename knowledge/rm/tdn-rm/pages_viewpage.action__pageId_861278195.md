---
content_hash: aedad1c121f7ce3dcd433520a9db823b1dd8889f84ba3f46bd1fae5d309d7047
fetched_at: '2026-06-29T00:11:55.457643+00:00'
page_id: '861278195'
product: rm
source: tdn-rm
title: DT - Afastamento por serviço militar - Evento com natureza da rubrica 9905
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=861278195
version: 5
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Cálculo de Base de FGTS para afastado |
| País: | Brasil |
| Ticket: | [9343071](https://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%229343071%22 "9343071") |
| Issue | [DRHCALCRM-126](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-126) |

## **02. VERSÃO**

A solução estará disponível a partir dos patchs/releases abaixo:

* 12.1.2410
* 12.1.2406.125
* 12.1.2402.199
* 12.1.2310.239

## **03. SITUAÇÃO/REQUISITO**

Quando o funcionário possuir um afastamento por serviço militar não deverá ser lançado o CC 315, sendo separado o tipo de afastamento M do tipo T e O, agora o Serviço Militar (M) será lançado através do CC 471 e sua diferença será gerada através do CC 472, deixando de utilizar o CC 354. Se faz necessário para atender a Rubrica 9905 - Serviço Militar.

## **04. SOLUÇÃO**

Foram criados os CC 471 e 472, para que ocorra a separação correta dos tipos de afastamentos M. Agora sempre que existir o tipo de afastamento no cadastro do funcionário será gerado o CC 471 e sempre que houver diferença será lançado o 472.

Exemplo de utilização:  
  
  
  
No envelope de pagamento foi lançado então o CC 471:

## **05.****ASSUNTOS RELACIONADOS**

* [Código de Cálculo 315](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719616)
* [Código de Cálculo 354](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718375)
* [Código de Cálculo 471](https://tdn.totvs.com.br/pages/viewpage.action?pageId=860243474)
* [Código de Cálculo 472](https://tdn.totvs.com.br/pages/viewpage.action?pageId=860243650)
