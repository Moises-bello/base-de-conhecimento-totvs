---
content_hash: 9bbaf6731abb973a4ad7326411bf8f0672409c4cc556eb03057fd64eaaad8764
fetched_at: '2026-06-29T00:08:28.675793+00:00'
page_id: '271843873'
product: rm
source: tdn-rm
title: 451171 MRH-7416 DT Valor Zerado Dependente Assistência Saúde
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271843873
version: 113
---

# ASSISTÊNCIA SAÚDE DIRF

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *DIRF | Assistência Saúde* |
| **Situação/Requisito:** | Ao gerar a DIRF para um dependente que possui valor de assistência saúde zerado, o sistema estava  gerando o registro DTPSE , com as informações do dependente porém levando o valor zero, desta forma ao validar o arquivo no validador da DIRF era apresentado erro informando que não era permitido importar dependente com valor de assistência zerado. |
| **Solução/Implementação:** | Foi ajustado o sistema para que não seja levado o registro DTPSE quando o valor do dependente de assistência saúde ficar zerado. |
| **Tickets relacionados:** | * + [451171](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%22451171%22 "451171") |

divs
