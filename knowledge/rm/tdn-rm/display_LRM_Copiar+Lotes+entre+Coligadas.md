---
content_hash: 0606aeb5eb54d616dc89e37823457c6638aa28db61217ea9330a6a532deb7e68
fetched_at: '2026-06-29T00:10:44.529777+00:00'
page_id: '553325412'
product: rm
source: tdn-rm
title: Copiar Lotes entre Coligadas
type: documentation
url: https://tdn.totvs.com/display/LRM/Copiar+Lotes+entre+Coligadas
version: 6
---

Para facilitar o cadastro de um lote é possível executar o processo de cópia de lotes entre coligadas, que tem como objetivo enviar para as coligadas de destino os lotes existentes na coligada de origem. Para que os lotes sejam copiados as coligadas de destino precisam ter definido o período contábil, existente na tela de parâmetros do módulo contábil.

**Considerações**

* O lote, que estiver com a opção Digitar Capa selecionada, não será copiado se suas datas estiverem fora do período contábil da coligada de destino.
* A s datas existentes na capa dos lotes serão alteradas para o período contábil da coligada de destino. Apenas os lotes em que a opção Digitar Capa está marcada irão permanecer com datas inalteradas.
* Os campos Valor, Total Débitos, Total Créditos e Valor da Soma serão enviados para as coligadas de destino com o valor zerado. A única exceção irá ocorrer para o campo Valor. Se na capa do lote a opção “Digitar Capa” estiver marcada o campo Valor será enviado para a coligada de destino sem alteração, pois com esta opção selecionada os valores dos lançamentos não poderão ultrapassar o valor fixado na capa do lote.
* Não será possível substituir registros (lotes) no destino.
