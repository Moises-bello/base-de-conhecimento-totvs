---
content_hash: 2f81604805268f45ed41460d8e77dc261543fad9573bbe5034b905eb0c5758f5
fetched_at: '2026-06-29T00:08:47.849779+00:00'
page_id: '321290607'
product: rm
source: tdn-rm
title: 1786353 FINANCEIRO01-4220 DT Inclusão de Borderô de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=321290607
version: 1
---

# Erro na geração do item de baixa do borderô de pagamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão e Financeira |
| **Função:** | Inclusão de Borderô de Pagamento |
| **Situação/Requisito:** | Ao incluir vários lançamentos em borderôs de pagamento o sistema gera os itens de baixa com data de baixa incorretamente. |
| **Solução/Implementação:** | Ajustado serviço de geração de borderô de pagamento para poder gerar o item de baixa respeitando a data informada como data base de cumulatividade. |
| **Conversores e Parâmetros:** | N/A |
| **Requisito:** | FIN000170 |
