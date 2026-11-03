---
content_hash: 352a302440e25a903d41815284fc8adeec1fa22be8c57f541cb2ef1c25f17591
fetched_at: '2026-06-29T00:09:01.031556+00:00'
page_id: '370621616'
product: rm
source: tdn-rm
title: 2898144 DSAUGHCOM-286 DT Erro ao liberar prescrição de procedimentos (item
  de débito com data futura)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=370621616
version: 1
---

# Erro ao liberar prescrição de procedimentos (item de débito com data futura)

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Integração PEP 2.0 |
| **Situação/Requisito:** | Quando existe uma diferença de tempo (minutos/segundos) entre o servidor de aplicação do PEP 2.0 e do banco de dados do RM, o sistema não permitia o lançamento dos itens de débito. |
| **Solução/Implementação:** | Ajustado para permitir o lançamento dos itens de débito dentro do mesmo dia. |
| **Documento de Referência:** | Ticket #2898144 |
