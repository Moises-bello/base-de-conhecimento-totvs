---
content_hash: 02ae35ae4bfef01fa1176b37adeaf7c87a8dc603379ac56d16044958ef9bb7a0
fetched_at: '2026-06-29T00:08:31.860130+00:00'
page_id: '273314830'
product: rm
source: tdn-rm
title: 722151 EDUCACIONAL01-85 DT Geracao Errada Do Faturamento
type: documentation
url: https://tdn.totvs.com/display/LRM/722151+EDUCACIONAL01-85+DT+Geracao+Errada+Do+Faturamento
version: 108
---

# GERAÇÃO DE LANÇAMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Geração de lançamentos* |
| **Situação/Requisito:** | *Ao gerar lançamentos financeiros para uma gama de lançamentos, onde nos contratos existam disciplinas com cancelamento total (não contam como créditos financeiros) e disciplinas com cancelamentos parciais (abatem após alteração do status), o sistema erroneamente passa a entender que em todos os contratos que possuem cancelamentos, existe cancelamento total em pelo menos uma das disciplinas e por isso, passa a calcular o valor a reter com base nas parcelas já pagas pelo aluno. Nesse sentido, caso algum contrato tenha todas as disciplinas com cancelamento parcial e também tenha tido o seu valor total de créditos aumentado, de forma que o sistema entenda que o aluno pagou a menor do que deveria ter pago com relação a fração ideal, um saldo positivo é gerado para uma parcela que deveria ter tido o seu valor calculado como zero, já que neste contrato todos os cancelamentos foram parciais.* |
| **Solução/Implementação:** | *Foi realizada otimização do processo de geração de lançamentos, de forma que o sistema não gere valor para parcelas calculadas por créditos financeiros quando todas as disciplinas do contrato do aluno possuírem as suas disciplinas canceladas.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.17* |
| **Versão Corrigida:** | *12.1.17* |
| **Versão Expedida:** | *12.1.17* |

divs
