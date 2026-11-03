---
content_hash: e2150ea21f2ae5249efb0c553b9025699282f2b5a4926b3af0d00f22ea14b5db
fetched_at: '2026-06-29T00:06:13.014196+00:00'
page_id: '207357153'
product: rm
source: tdn-rm
title: TTLCID_DT_Rescisao_Complementar_Nao_Zera_Valor_de_Base_Negativa
type: documentation
url: https://tdn.totvs.com/display/LRM/TTLCID_DT_Rescisao_Complementar_Nao_Zera_Valor_de_Base_Negativa
version: 2
---

# RESCISÃO COMPLEMENTAR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão Complementar* |
| **Situação/Requisito:** | *A gerar uma rescisão complementar por dissídio, o valor do evento de CC 69 não estava sendo composto da forma correta, pois os valores das verbas que o compoe estavam negativos, somando à base de FGTS. O comportamento correto é que, caso a verba de composição da base de FGTS seja um valor negativo, que não seja acumulado nenhum valor, ao invés de continuar negativo.* |
| **Solução/Implementação:** | *Zerar o valor do evento que se encontra negativo no momento de compor a base de FGTS da rescisão complementar para que esta não fique com valor negativo, causando o problema de não levar os valores corretos na SEFIP 650.* |
| **Chamados relacionados:** | TTLCID |
| **Versões/Release:** | *12.1.8* |
| **Versão Corrigida:** | *12.1.8* |
| **Versão Expedida:** | *12.1.8* |

1. [12.1.8](http://tdn.totvs.com/display/LRM/Release+12.1.8)
