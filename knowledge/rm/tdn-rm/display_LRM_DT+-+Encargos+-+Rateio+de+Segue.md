---
content_hash: dbc5d41d52c3dace376c6de9f534d35e2b889ddc9dc1608042fb88c4b5e5597b
fetched_at: '2026-06-29T00:11:54.796701+00:00'
page_id: '857915600'
product: rm
source: tdn-rm
title: DT - Encargos - Rateio de Segue
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Encargos+-+Rateio+de+Segue
version: 8
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
| Ticket: | [16134176](https://totvssuporte.zendesk.com/agent/tickets/16134176 "View ticket on the Zendesk portal"), [15644482](https://totvssuporte.zendesk.com/agent/tickets/15644482 "View ticket on the Zendesk portal"), [15380172](https://totvssuporte.zendesk.com/agent/tickets/15380172 "View ticket on the Zendesk portal"), [19234618](https://totvssuporte.zendesk.com/agent/tickets/19234618 "View ticket on the Zendesk portal") |
| Issue | [DRHCALCRM-3570](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-3570) |

## **02. VERSÃO**

Versão disponível a partir de:

* 12.1.2406.119
* 12.1.2410

## **03. SITUAÇÃO/REQUISITO**

Quando o funcionário possui somente eventos com valores zerados lançados na ficha financeira e os mesmo estão configurados no Rateio de eventos e este rateio está vinculado ao encargo no campo Rateio que o encargo segue, ao gerar os encargos os valores não são rateados para os centros de custo,

## **04. SOLUÇÃO**

Foi criado um parâmetro no cadastro de encargos, para que, quando utilizando Rateio que o encargo segue e os eventos que compõe este rateio estiverem zerados na ficha financeira, o processo preencha o rateio de Encargos por Centro de custo considerando os centros de custos cadastrado no rateio fixo do funcionário.

Parâmetro Marcado, Parâmetro Desmarcadopasso1,passo2

Cadastro rateio de eventos com os eventos que compõe o rateio:

Na Ficha financeira do Funcionário possui o evento 0084 lançado com valor 0:

Rateio Fixo do Funcionário:

yespasso1

Exemplificando com o encargo Tipo 6, com o parâmetro marcado:

O Encargo foi gerado e no log está indicando que foi feito o rateio:

O encargo foi rateado considerando o centro de custo do funcionário, conforme a indicação do parâmetro:

nopasso2

Exemplificando com o encargo Tipo 6, com o parâmetro desmarcado:

O Encargo foi gerado e no log está indicando que não foi feito o rateio:

O encargo foi gerado, porém não foi feito rateio:

## **05. DEMAIS INFORMAÇÕES**

A situação ocorre para qualquer tipo de encargo que segue rateio e o período informado tem eventos que compõe o rateio com valor zerado na ficha financeira.

Caso algum evento que compõe rateio esteja com valor maior que zero, o processo irá gerar o rateio considerando a distribuição por centro de custo da ficha financeira, independente do parâmetro.

Caso não exista nenhum evento que compõe o rateio lançado na ficha financeira, o processo irá gerar o rateio considerando o rateio fixo do funcionário, independente do parâmetro.

falseAtenção

**É necessário executar o atualizador para que o parâmetro 'Considerar rateio fixo quando eventos do rateio que segue for zero' seja exibido a partir do patch da versão 12.1.2406**

## **06. ASSUNTOS RELACIONADOS**

* [Encargos - Folha de Pagamento](https://tdn.totvs.com.br/display/public/LRM/Encargos+-+Folha+de+Pagamento?draft=true)
