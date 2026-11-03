---
content_hash: 78c71743a57dce7cd995043d7a09fbde7cc73cc6af0ac697f84535539b07c0ad
fetched_at: '2026-06-29T00:10:01.962517+00:00'
page_id: '452718816'
product: rm
source: tdn-rm
title: Faixas de Item de Informação Clínica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718816
version: 2
---

**Faixas de Item de Informação Clínica**

Este anexo tem como objetivo a definição de faixas de valores para os Itens de Informação Clínica cujo o tipo de valor seja "Numérico". É possível definir, além da faixa de valores, um Nome e uma Cor para ser apresentada no lançamento do resultado de exames.

Além disso é possível informar uma Consulta SQL que será executada no momento do lançamento do resultado de exames e a faixa que tiver a Consulta SQL só será considerada válida se a consulta retornar um ou mais registros.

**Observação**

 Para ser vinculada a uma faixa de item de informação clínica, uma Consulta SQL precisa atender as seguintes regras:

* Conter no mínimo um parâmetro "código da pessoa" (Ex. "CODPESSOA = :CODPESSOA").
* Não existir nenhum outro parâmetro, senão o "código da pessoa", que pode ser adicionado em mais de uma condição, mantendo o mesmo nome.
* O parâmetro "código da pessoa" deve obrigatoriamente ter o nome "CODPESSOA".

**Exemplo de consulta SQL válida**

SELECT PPESSOA.SEXO FROM PPESSOA WHERE PPESSOA.SEXO = 'M' AND PPESSOA.CODIGO = :CODPESSOA
