---
content_hash: 2bd2e9985dee22a6cec6dd3cea37107b65a6cece93b3541adbd7d1baede53374
fetched_at: '2026-06-29T00:06:28.123849+00:00'
page_id: '233748205'
product: rm
source: tdn-rm
title: TUJVZJ_DT_Deducao_INSS_13_Nao_Aparece_O_Valor
type: documentation
url: https://tdn.totvs.com/display/LRM/TUJVZJ_DT_Deducao_INSS_13_Nao_Aparece_O_Valor
version: 116
---

# DIRF/INFORME DE RENDIMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *DIRF/Informe de Rendimentos* |
| **Situação/Requisito:** | Ao gerar a DIRF pela rotina .NET, identificamos que o sistema não apresenta o valor correto de R$ 113,47 no campo DED INSS13º, ele retorna o valor zerado neste campo. Neste campo o sistema deveria apresentar o valor de R$ 28,26, referente ao evento de código de cálculo 11 (INSS De 13ºSALARIO). |
| **Solução/Implementação:** | *Ajustado cálculo do INSS de 13º quando não há INSS de folha em dezembro.* |
| **Chamados relacionados:** | *TUJVZJ* |

divs
