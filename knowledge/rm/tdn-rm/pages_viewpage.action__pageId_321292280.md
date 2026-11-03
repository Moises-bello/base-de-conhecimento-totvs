---
content_hash: c9e3db51ad40ad96f79ae12635f2b4a16f3083194058840368a8d32f31a7973b
fetched_at: '2026-06-29T00:08:47.860513+00:00'
page_id: '321292280'
product: rm
source: tdn-rm
title: 1778100 EDUCACIONAL01-3353 DT Regra de Empréstimo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=321292280
version: 95
---

# REGRA DE EMPRÉSTIMO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Realizar empréstimo de exemplar* |
| **Situação/Requisito:** | *Na parametrização, é configurado para o sistema contar sábado, domingos e feriados como dias normais, para que as multas e prazos sejam calculados de acordo com as regras institucionais. Porém o sistema não deve realizar marcações de devoluções para estes dias.*  *Por exemplo, uma revista, que possui dois dias de prazo, se emprestada na quinta, deveria ter sua data de devolução para segunda, mas o sistema coloca sábado por causa do parâmetro informando que sábado é dia útil.*  *Se a mesma revista for emprestada na Quarta, o prazo sairá corretamente na sexta, mas se for devolvida na segunda, o sistema deverá calcular multa de todo o fim de semana.*  *Não existe meios de parametrizar dessa maneira no qual a data prevista não seja marcada para um dia não útil.* |
| **Solução/Implementação:** | *Foi incluído o parâmetro "Considera dia não útil para cálculo da data prevista de entrega" que tem a função de considerar dias não uteis no cálculo para data prevista da entrega porém se a data devolução for em um dia não útil, será respeitada a regra parametrizada no vencimento em dias não uteis (Manter data, buscar próximo dia útil ou buscar dia útil anterior).* |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
