---
content_hash: 79906d41b78546701253f3083d2021dfc271eb7c0d023cba159cd9edd963e556
fetched_at: '2026-06-29T00:11:54.685731+00:00'
page_id: '856932581'
product: rm
source: tdn-rm
title: DT - Encargos por Dissídio - Base de INSS e Base INSS 13º
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=856932581
version: 9
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Geração de Encargos |
| País: | Brasil |
| Ticket: | [15320812](https://totvssuporte.zendesk.com/agent/tickets/15320812 "View ticket on the Zendesk portal"), [16222875](https://totvssuporte.zendesk.com/agent/tickets/16222875 "View ticket on the Zendesk portal"), [19411751](https://totvssuporte.zendesk.com/agent/tickets/19411751 "View ticket on the Zendesk portal"), [17876515](https://totvssuporte.zendesk.com/agent/tickets/17876515 "View ticket on the Zendesk portal"), [18133589](https://totvssuporte.zendesk.com/agent/tickets/18133589 "View ticket on the Zendesk portal"), [18248789](https://totvssuporte.zendesk.com/agent/tickets/18248789 "View ticket on the Zendesk portal"), [18243818](https://totvssuporte.zendesk.com/agent/tickets/18243818 "View ticket on the Zendesk portal"), [15262911](https://totvssuporte.zendesk.com/agent/tickets/15262911 "View ticket on the Zendesk portal") |

## **02. VERSÃO**

Versão disponível a partir de:

* 12.1.2310.235
* 12.1.2402.182
* 12.1.2406.116
* 12.1.2410

## **03. SITUAÇÃO/REQUISITO**

Ao gerar os encargos tipo **R - Base: incidência de INSS Dissídio** e **S - Base: incidência de INSS de 13º salário Dissídio** os mesmos considera todos os eventos com incidência somente para segurados, onde o mesmo deveria considerar para a base de cálculo os eventos que compõe a parte empresa.

E para o encargo  **R - Base: incidência de INSS Dissídio** não está sendo considerado os valores de diferença de férias por dissídio.

## **04. SOLUÇÃO**

Foi alterado os encargos conforme abaixo:

**R - Base: incidência de INSS Dissídio:** valores lançados na PFVERBASDIS e PFVERBASDISFER onde no evento está configurado com incidência em INSS e não está marcado Incidência exclusiva segurado ou o evento está configurado com incidência exclusiva empregador.  E foi desconsiderado os valores de férias lançados na PFVERBASDIS, sendo considerado os valores lançados na PFVERBASDISFER.

**S - Base: incidência de INSS de 13º salário Dissídio** valores lançados na PFVERBASDIS  onde no evento está configurado com incidência em INSS 13º Salário e não está marcado Incidência exclusiva segurado ou o evento está configurado com incidência exclusiva empregador.

## **05. EXEMPLO DE UTILIZAÇÃO**

Encargo R - Base: incidência de INSS Dissídio, Encargo S - Base: incidência de INSS de 13º salário, Passo 03, Passo 04passo1,passo2yespasso1

Foi configurado as incidências dos eventos conforme abaixo:

| Código do Evento | Inc. INSS | Exclusiva segurado | Exclusiva empregador | Compõe base |
| --- | --- | --- | --- | --- |
| 0002 | Sim | Não | Não | Sim |
| 0082 | Sim | Sim | Não | Não |
| 0083 | Não | Não | Sim | Sim |
| 0104 | Sim | Não | Não | Sim |
| 0159 | Sim | Sim | Não | Não |
| 0008 \* | Sim | Não | Não | Sim |
| 0041 | Sim | Não | Não | Sim |
| 0076 | Sim | Não | Não | Sim |

Obs.: O evento 0008 é um desconto, logo ele estorna da base.

Na competência 12/2022 foi calculada a diferença salarial e de Férias retroativa as competência 10 e 11 de 2022, com a opção dissídio Sim marcada. Os valores abaixo foram lançados na aba Verbas geradas por diferença (tabela PFVERBASDIS) e Detalhamento verbas geradas pela diferença de Férias (Envelope) (Tabela PFVERBASDISFER)

Ao gerar o encargo será somado os valores dos eventos conforme a configuração de incidência acima: 1027,96

| Mês | Ano | Evento | Valor |
| --- | --- | --- | --- |
| 10 | 2022 | 0002 | 413,15 |
| 10 | 2022 | 0083 | 9,89 |
| 10 | 2022 | 0104 | 82,63 |
| 11 | 2022 | 0002 | 230,21 |
| 11 | 2022 | 0083 | 30,90 |
| 11 | 2022 | 0104 | 72,70 |
| 11 | 2022 | 0041 | 159,54 |
| 11 | 2022 | 0076 | 53,18 |
| 11 | 2022 | 0008\* | 24,24 |

nopasso2

Foi configurado as incidências dos eventos conforme abaixo:

| Código do Evento | Inc. INSS 13º | Exclusiva segurado | Exclusiva empregador | Compõe base |
| --- | --- | --- | --- | --- |
| 0129 | Sim | Não | Não | Sim |
| 0133 | Não | Não | Sim | Sim |

 Na competência 12 de 2022 foi calculada a diferença de 13º Salário retroativa ao ano de 2021. Os valores abaixo foram lançados na aba Verbas geradas por diferença (tabela PFVERBASDIS). Repare que no exemplo abaixo existe mais de uma diferença de 13º Calculada para o mesmo ano de 2021, porém em meses diferentes. Como estou gerando os encargos relativo a competência 12 de 2022, será considerado somente os eventos que foram pagas na comp. 12/2022:

Ao gerar o encargo será somado os valores dos eventos conforme a configuração de incidência acima: 376,07

| Mês | Ano | Evento | Valor |
| --- | --- | --- | --- |
| 12 | 2021 | 0129 | 349,88 |
| 12 | 2021 | 0133 | 26,19 |

## **06. DEMAIS INFORMAÇÕES**

* Em ambos encargos é verificado se o evento lançado nas tabelas PFVERBASDIS e PFVERBASDISFER está com o campo dissídio = Sim e o mês e ano de referência é o mesmo informado no processo de geração de encargos

## **07. ASSUNTOS RELACIONADOS**

* [Encargos - Folha de Pagamento](https://tdn.totvs.com.br/display/public/LRM/Encargos+-+Folha+de+Pagamento)
