---
content_hash: 062597b95d75e5af2353ba203a54ddf2d14a8c6f770c6ad00398f9aa85f96fb6
fetched_at: '2026-06-29T00:09:18.462643+00:00'
page_id: '421388699'
product: rm
source: tdn-rm
title: Contabilizar Lançamento Baixados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388699
version: 8
---

Este recurso será normalmente utilizado na baixa de um elevado volume de lançamentos, pois dependendo das regras contábeis o processo demandará maior tempo para processamento. Desta forma, para garantir maior agilidade, a contabilização da baixa poderá ser realizada em outro momento.  
Com a opção marcada, o processo de baixa de Lançamentos financeiros que possuem o Tipo Contábil "Contábil" ou "Baixa Contábil", é realizado sem a exigência das informações contábeis, que podem ser incluídas posteriormente. A funcionalidade "Contabilizar posteriormente" está disponível na baixa manual e nos  processos de baixa por importação de retornos de Cobrança de Pagamento eletrônicos.

**Pré-requisito**

É necessário utilizar defaults para Eventos Contábeis para que a contabilização seja realizada de forma automática. Durante o processo de Baixa, se for ativada a opção "Contabilizar posteriormente"  a baixa será realizada sem  a contabilização e o tipo contábil do Lançamento será alterado:

* Se o tipo contábil for "Contábil", após a baixa realizada com a opção "Contabilizar posteriormente" ativa, o tipo contábil será alterado para "Contábil com Baixa a Contabilizar".

* Se o tipo contábil for "Baixa Contábil", após a baixa realizada com a opção "Contabilizar posteriormente" ativa, o tipo contábil será alterado para "Baixa a Contabilizar".  
  Para contabilizar posteriormente, selecione os lançamentos e acesse Processos/Baixa/Contabilizar Lançamentos Baixados.

**Resultado**

A contabilização será gerada no item de baixa do lançamento e gravada no respectivo lote contábil. Nas baixas parciais, o tipo contábil do lançamento será alterado somente após a baixa total do título.

Veja Também
