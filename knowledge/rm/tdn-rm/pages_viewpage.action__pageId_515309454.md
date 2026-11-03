---
content_hash: 200e72bac35c3e55c66c0a767fc965b494fc643fa9c48aac23674695031aa30f
fetched_at: '2026-06-29T00:10:26.916054+00:00'
page_id: '515309454'
product: rm
source: tdn-rm
title: Registro 0600 - Geração do Registro 0600
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=515309454
version: 7
---

Para geração do Registro 0600 são feitas as seguintes consistências:

* Centro de Custo preenchido no item
* Natureza de Serviço (Flag Fiscal Desmarcada)
* Item do tipo Serviço
* Lançamento com Status Normal ou Cancelado
  + Se a data de cancelamento da nota for dentro do mês de geração da Rotina, o status dos lançamentos gerado no Registro A100 é igual a "Cancelado".
  + Se a data de cancelamento da nota diferente do mês de geração da Rotina, o status dos lançamentos gerado no Registro A100 é igual a "Normal".
* Na tela de Geração da Rotina o campo "Lucro Presumido" deve ser igual a "Não se aplica" ou "Regime de Competência - Escrituração detalhada"
* Se no item ou movimento há algum dos tributos PIS, COFINS ou PIS Importação

Para o município de Brasília além das regras citadas acima também vão ser feitas as seguintes consistências:

* Lançamento de Entrada ou Saída;
* Que o modelo do documento seja 55;
* Natureza com CFPS preenchido ;

O lançamento será considerado serviço, gerando assim o registro 0600 com o Centro de Custo informado nos itens do lançamento Fiscal.
