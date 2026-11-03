---
content_hash: 20eabe1160a26330a29f4842b494f2955568c72be6cd7511c026b211db3ca809
fetched_at: '2026-06-29T00:09:18.456051+00:00'
page_id: '421388696'
product: rm
source: tdn-rm
title: Contabilizar Posteriormente
type: documentation
url: https://tdn.totvs.com/display/LRM/Contabilizar+Posteriormente
version: 3
---

Este recurso será normalmente utilizado na baixa de um elevado volume de lançamentos, pois dependendo das regras contábeis o processo demandará maior tempo para processamento.

Desta forma, para garantir maior agilidade, a contabilização da baixa poderá ser realizada em outro momento. Com a opção marcada, o processo de baixa de Lançamentos financeiros que possuem o Tipo Contábil "Contábil" ou "Baixa Contábil", é realizado sem a exigência das informações contábeis, que podem ser incluídas posteriormente.

A funcionalidade "Contabilizar posteriormente" está disponível na baixa manual e nos processos de baixa por importação de retornos de Cobrança e Pagamento eletrônicos.

**Pré-requisito**

É necessário utilizar defaults para Eventos Contábeis para que a contabilização seja realizada de forma automática. Durante o processo de Baixa, se for ativada a opção "Contabilizar posteriormente"  a baixa será realizada sem  a contabilização e o tipo contábil do Lançamento será alterado:

* Se o tipo contábil for "Contábil", após a baixa realizada com a opção "Contabilizar posteriormente" ativa, o tipo contábil será alterado para "Contábil com Baixa a Contabilizar".
* Se o tipo contábil for "Baixa Contábil", após a baixa realizada com a opção "Contabilizar posteriormente" ativa, o tipo contábil será alterado para "Baixa a Contabilizar".

**Para contabilizar posteriormente**

Selecione os lançamentos e acesse Processos/Baixa/Contabilizar Lançamentos Baixados.

**Resultado**

A contabilização será gerada no item de baixa do lançamento e gravada no respectivo lote contábil.

**Observação:**

Nas baixas parciais, o tipo contábil do lançamento será alterado somente após a baixa total do título.
