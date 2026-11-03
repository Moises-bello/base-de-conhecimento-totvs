---
content_hash: eeec527eebb7214f5a722a7e8a9b97ffbcc8217626937c8be92e50245997d689
fetched_at: '2026-06-29T00:09:26.121033+00:00'
page_id: '423938267'
product: rm
source: tdn-rm
title: Cancelar Contrato (Estoque, Compras e Faturamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938267
version: 8
---

O cancelamento de um contrato ou de itens do contrato será possível nas seguintes condições:

* Contratos/Itens que ainda não geraram faturamento;
* Contratos/Itens que ainda não geraram previsões financeiras;
* Contratos/Itens que ainda estão dentro do período de carência para o cancelamento.

A data limite para o cancelamento de um contrato (ou item de contrato) é dado pela data resultante da soma da data de Inicio da vigência do contrato mais a quantidade de dias informada no período de carência para cancelamento.   
Durante o cancelamento é necessário informar o motivo de cancelamento e o status que o contrato/item receberá após o cancelamento do mesmo.   
Os campos Motivo de Cancelamento e Status de Cancelamento são cadastrados através das suas respectivas Tabelas de Contratos.   
Após o cancelamento de um contrato (ou item de contrato) é possível reverter o cancelamento através do processo "Desfazer Cancelamento".

Informações

A partir da release 12.1.2306 será possível efetuar o cancelamento de mais de um contrato simultaneamente.

Ao realizar este tipo de operação o **status** e o **motivo de cancelamento** serão únicos para todos os contratos selecionados para o cancelamento.
