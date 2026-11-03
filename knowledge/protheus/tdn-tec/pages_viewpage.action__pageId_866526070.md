---
content_hash: 28085fd6640113d4f68558a87d7d2196b02bf1ed990855d59e321742d89d44fc
fetched_at: '2026-07-02T19:24:29.374551+00:00'
page_id: '866526070'
product: protheus
source: tdn-tec
title: Versão 01.04.07
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=866526070
version: 3
---

GreenAppserver 20.3.2.12

## Correção

* tlpp.PROBAT: #DTTLPP-2861 Correção na exportação de resultados para não quebrar mais o XML nos casos que não tinham dados de ini gravados na execução.

---

## Melhoria

* tlpp.REST: O callback  passa a entregar total controle sobre o tratamento da mensagem de erro de uma API REST ao desenvolvedor (inclusive sua impressão no console da aplicação).
* tlpp.DOC: Ajustes na impressão de erros na geração de documentação para facilitar entendimento dos eventos ocorridos.
* tlpp.REST: #DTTLPP-2785 - Criada a classe tlpp.http.uriNormalize para facilitar obter o retorno do decode dos PathParams.
* tlppCore: #DTTLPP-2761 A configuração do AppMonitor passa a utilizar a porta Multiprotocolo
