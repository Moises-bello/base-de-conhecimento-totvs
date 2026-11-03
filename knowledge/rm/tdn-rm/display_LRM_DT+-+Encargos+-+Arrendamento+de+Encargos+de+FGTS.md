---
content_hash: 2d5fb69268ba696e94dadb9bc45ca1fc01eb05d06fbd3d99482c04c3c2905512
fetched_at: '2026-06-29T00:11:54.566387+00:00'
page_id: '853929811'
product: rm
source: tdn-rm
title: DT - Encargos - Arrendamento de Encargos de FGTS
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Encargos+-+Arrendamento+de+Encargos+de+FGTS
version: 4
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Geração de Encargos |
| País: | Brasil |
| Story: | [DRHCALCRM-6591](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-6591) |

## **02. VERSÃO**

A solução estará disponível a partir dos patchs/releases abaixo:

* 12.1.2310.229
* 12.1.2402.172
* 12.1.2406.104
* 12.1.2410

## **03. SITUAÇÃO/REQUISITO**

Quando é gerado os encargos de FGTS (tipo 2 e M) os mesmo não estão verificando a marcação do parâmetro 'Aplicar o arredondamento sobre o valor total do encargo' e com isto fazendo com que os valores fiquei divergentes com o FGTS Digital.

## **04. SOLUÇÃO**

Foi adequado os encargos de FGTS para considerar a a flag "Aplicar arredondamento sobre o valor total" na tela de cadastro de Encargos. Também foi validado o parâmetro geral 'Truca valores de FGTS/INSS' localizado em Parametrizador | Folha Normal | Encargos Sociais.

## **05. DEMAIS INFORMAÇÕES**

[Encargos - Folha de Pagamento](https://tdn.totvs.com.br/display/LRM/Encargos+-+Folha+de+Pagamento)
