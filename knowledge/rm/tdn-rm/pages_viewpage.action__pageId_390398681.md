---
content_hash: 86adeb64421751bb8b9e33fc901ee00547be69f5c81cd7820d5c5445767334ef
fetched_at: '2026-06-29T00:09:08.607238+00:00'
page_id: '390398681'
product: rm
source: tdn-rm
title: 3346357 FINANCEIRO01-8151 DT Retorno de Cobrança não Registrada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=390398681
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Retorno de Cobrança não Registrada |
| **Situação/Requisito:** | Após conversão para patch 12.1.19, o processo de retorno de cobrança não registrada parou de funcionar. |
| **Solução/Implementação:** | Identificamos que o cliente utilizava um processo customizado, onde o código informado pelo banco como Nosso Número era atualizado diretamente no lançamento, no campo CNABNOSSONUMERO. O processo de retorno de cobrança não registrada foi flexibilizado para, além de buscar o Nosso Número do campo NOSSONUMERO da tabela FBOLETO, também fazê-lo direto no campo CNABNOSSONUMERO da tabela FLAN, mantendo assim o comportamento legado. |
| **Conversores e Parâmetros:** | Não se aplica |
| **Tickets relacionados:** | 3346357 |
| **Requisito:** | FIN000169 |
| **Documento de Referência:** | Não se aplica |
| **Pacote:** | Não se aplica |
