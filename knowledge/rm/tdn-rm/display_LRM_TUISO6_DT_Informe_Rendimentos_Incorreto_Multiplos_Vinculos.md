---
content_hash: 1ab0e9b42826d2764002cd31b8e455a82ac7b39f4ee7637ae5d736b847099da6
fetched_at: '2026-06-29T00:06:28.162260+00:00'
page_id: '233750080'
product: rm
source: tdn-rm
title: TUISO6_DT_Informe_Rendimentos_Incorreto_Multiplos_Vinculos
type: documentation
url: https://tdn.totvs.com/display/LRM/TUISO6_DT_Informe_Rendimentos_Incorreto_Multiplos_Vinculos
version: 116
---

# DIRF/INFORME DE RENDIMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *DIRF/Informe de Rendimentos* |
| **Situação/Requisito:** | O funcionário possui dois registros um com vínculo empregatício e outro sem ao gerar o informe para todos os funcionários o sistema traz o valor de PLR para os dois informes, mesmo que exista a informação da PLR somente na chapa com vínculo empregatício.     Quando o informe é gerado separado para as duas chapas o valor de PLR sai somente para uma das chapas. |
| **Solução/Implementação:** | *Ajustado informe de rendimentos quando o funcionário tem mais de um vínculo e PLR em apenas um registro.* |
| **Chamados relacionados:** | *TUISO6 e TUKXY4* |

divs
