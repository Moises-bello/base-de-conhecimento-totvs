---
content_hash: 90f19e64b9284bbc4381d752555afe74869da3932e4d06be0d19dd29085da8a5
fetched_at: '2026-06-29T00:08:32.448553+00:00'
page_id: '273986221'
product: rm
source: tdn-rm
title: 699934 FOPROTINAS01-24 DT Mensagem de Pagamento de Férias em Dobro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273986221
version: 108
---

# CADASTRO DE FÉRIAS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projeto |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Cadastro de Férias |
| **Situação/Requisito:** | O sistema apresenta no grupo Informações Adicionais do Cadastro de Férias do Funcionário uma mensagem informando que deve-se pagar férias em dobro para o funcionário mesmo quando o período de gozo marcado inicia-se antes do limite para início de gozo informado pelo sistema. |
| **Solução/Implementação:** | Modificar a condição de teste antes da exibição da mensagem para considerar os casos em que não há período de gozo cadastrado, ou o período de gozo cadastrado ultrapassa total ou parcialmente o período concessivo ou restam dias a marcar ou sem abono. |
| **Tickets relacionados:** | FOPROTINAS01-24 |

divs
