---
content_hash: 480426fc80ba3dfc9dc66489864cff1a66c3174cd700c571a168696a8efe5be9
fetched_at: '2026-06-29T00:08:28.252843+00:00'
page_id: '271674272'
product: rm
source: tdn-rm
title: 514895 MRH-7202 Subtrair Valores Informe Rendimentos
type: documentation
url: https://tdn.totvs.com/display/LRM/514895+MRH-7202+Subtrair+Valores+Informe+Rendimentos
version: 115
---

# DIRF/INFORME DE RENDIMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *DIRF/Informe de Rendimentos* |
| **Situação/Requisito:** | Ao gerar o Informe de Rendimentos, incluindo um evento de desconto na aba “Campo 4 – Rend. Isentos e não tribut” marcando para subtrair valor, o sistema não grava a marcação de “Subtrair valor” e ao invés de subtrair está somando.  Campo 4 linha 7 do informe de rendimentos. |
| **Solução/Implementação:** | *Ajustado para gravar corretamente quando seleciona a opção Subtrair.*  *Os eventos marcados devem ser do tipo Desconto.* |
| **Tickets relacionados:** | *514895* |

divs
