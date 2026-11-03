---
content_hash: 4acf364409d9c1114f5e43f71219c51739590d7fc46783d54b5889dbfe5c9d37
fetched_at: '2026-06-29T00:08:34.690212+00:00'
page_id: '274833883'
product: rm
source: tdn-rm
title: 657373 FINANCEIRO01-334 DT BAIXA PARCIAL DÉBITO AUTOMÁTICO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274833883
version: 94
---

# Geração de Boleto via Baixa parcial de Débito Automático

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Baixa |
| **Situação/Requisito:** | Ao realizar baixa parcial de Boleto do tipo "Débito Automático" o sistema está criando outro boleto com valor restante com o tipo "Boleto de Cobrança". |
| **Solução/Implementação:** | Agora o sistema carrega o tipo do Boleto que está em processo de baixa parcial e transfere seu tipo para o novo boleto que será gerado. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 657373 |
| **Requisito:** | FIN000040 |

divs
