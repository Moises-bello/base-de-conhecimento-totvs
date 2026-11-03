---
content_hash: 1d7185ecd77eab1f63240b5ac9af3c0e12fe2e399be6e7667020efff23defca7
fetched_at: '2026-06-29T00:06:26.295293+00:00'
page_id: '224458107'
product: rm
source: tdn-rm
title: TUFHSC_DT_DIRF_INFORME_RENDIMENTOS
type: documentation
url: https://tdn.totvs.com/display/LRM/TUFHSC_DT_DIRF_INFORME_RENDIMENTOS
version: 118
---

# DIRF - Informe de Rendimentos

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *DIRF - Informe de Rendimentos* |
| **Situação/Requisito:** | Em casos com funcionários com chapas de muitos caracteres, o limite de 50 caracteres estava estourando no nome do log da dirf para conferência, não salvando o log em banco. |
| **Solução/Implementação:** | *Foi alterado o nome do log para não incluir a chapa do funcionário, uma vez que a mesma já está presente no conteúdo do log* |
| **Chamados relacionados:** | TUFHSC, TUGYB7 |

divs
