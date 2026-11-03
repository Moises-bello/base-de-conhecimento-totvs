---
content_hash: 6aed1b22f8bea3fba310c1ebf04056b867aeb5c8d39d0d79e4477364d6b259a0
fetched_at: '2026-06-29T00:08:43.616218+00:00'
page_id: '305922844'
product: rm
source: tdn-rm
title: FINANCEIRO01-2398 Baixa Lançamentos com rateio remetidos ao banco
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=305922844
version: 94
---

# BAIXA DE LANÇAMENTOS REMETIDOS AO BANCO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Baixa de lançamentos financeiros. |
| **Situação/Requisito:** | Ao baixar lançamentos a pagar remetidos ao banco onde após a remessa as informações de rateio do lançamento foi alterada o serviço de baixa não conseguia encontrar o rateio do item de baixa gerado pela inclusão do borderô de pagamento e tentava incluir um novo registro utilizando uma chave já existente. |
| **Solução/Implementação:** | Corrigido o serviço de baixa para incluir um novo rateio por departamento com uma chave valida caso não consiga encontrar o rateio gerado na inclusão de borderô. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** |  |
| **Requisito:** | FINANCEIRO01-2398. |

divs
