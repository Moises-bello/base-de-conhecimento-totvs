---
content_hash: 8d77f3aa5da76f0bfab32ae34bca465cea3bd18892e431d8eb96e90086f4acca
fetched_at: '2026-06-29T00:08:19.400868+00:00'
page_id: '267784900'
product: rm
source: tdn-rm
title: TVWAM4_DT_Nao_Imprimir_Secoes_Liquido_Zerado_Guia_INSS
type: documentation
url: https://tdn.totvs.com/display/LRM/TVWAM4_DT_Nao_Imprimir_Secoes_Liquido_Zerado_Guia_INSS
version: 112
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Guia de INSS* |
| **Situação/Requisito:** | *Ao realizar o processo de geração da Guia de INSS, quando existe alguma seção que ficou com o valor líquido zerado, o sistema estava imprimindo também esta seção no relatório, porém na guia de INSS delphi quando existia esta situação, as seções que possuíam esta característica não era impressas no relatório da guia.* |
| **Solução/Implementação:** | *Foi ajustado o sistema para que no momento da geração do relatório da guia de INSS as seções que possuam liquido igual a zero, não serão impressas no relatório como era feito na guia em delphi.* |
| **Chamados relacionados:** | *TVWAM4* |

divs
