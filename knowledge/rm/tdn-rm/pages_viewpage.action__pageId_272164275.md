---
content_hash: 5e15a9d76d44f35fec0a14f91144b6e5d8b6ddda68e3e81ee2b51c2adc470dd1
fetched_at: '2026-06-29T00:08:29.766213+00:00'
page_id: '272164275'
product: rm
source: tdn-rm
title: 327780 MEDU-1886 Baixa Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272164275
version: 115
---

# Baixa Lançamentos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Financeira. |
| **Função:** | Baixa Lançamentos. |
| **Situação/Requisito:** | Ao baixar parcialmente um lançamento informando um valor de desconto na hora da baixa, caso o modo de cálculo for proporção, o sistema proporcionaliza esse valor de desconto, persistindo o valor restante de desconto para as próximas baixas. |
| **Solução/Implementação:** | Conceitualmente o valor informado no momento da baixa, pertence exclusivamente aquela baixa que está sendo realizada, caso o valor informado não for considerado totalmente na baixa, seu valor restante não deve ser armazenado para ser utilizado em baixas posteriores.  - Será acrescentado no formulário de baixa a Flag (Aplicar Desconto Total) para o campo de valor de desconto.  - Esta Flag estará disponível para ser marcada, somente se o modo de cálculo da baixa for proporção.  - Se marcada, o valor de desconto será aplicado total, independente se o valor de desconto está informado no lançamento, foi calculado por fórmula ou se o usuário digitou no formulário um valor de desconto, os restantes dos valores serão proporcionalizados.  - Se não marcado, o valor do desconto será proporcional ao valor baixado e não será salvo o valor restante de desconto. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | FIN000040 |

divs
