---
content_hash: 7e6fb845a791f99ee18d2e5a6dcf9a4f8ec1b273bb56d5300416fc25755ab29b
fetched_at: '2026-06-29T00:08:48.498948+00:00'
page_id: '325849613'
product: rm
source: tdn-rm
title: 1523468 FINANCEIRO01-4094 DT Retorno de Pagamento
type: documentation
url: https://tdn.totvs.com/display/LRM/1523468+FINANCEIRO01-4094+DT+Retorno+de+Pagamento
version: 1
---

# Integração Bancária - Retorno de Pagamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Retorno de Pagamento |
| **Situação/Requisito:** | No retorno de pagamento do banco SAFRA, sistema não esta efetuando o registro quando o código de retorno é igual a "04" (Autorização Aceita), conforme o manual. Sistema estava rejeitando o título |
| **Solução/Implementação:** | Efetuar o registro do título no retorno de pagamento do banco Safra, quando o código de retorno for igual a "04" - Autorização Aceita. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000171 |
