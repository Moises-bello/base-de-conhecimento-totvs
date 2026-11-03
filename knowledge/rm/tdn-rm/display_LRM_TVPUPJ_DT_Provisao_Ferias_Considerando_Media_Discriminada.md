---
content_hash: 60cb0b8438bfe9734c06e65ee8183a3538d21f60bc3f9f05276e2ea9e2f246fc
fetched_at: '2026-06-29T00:08:19.482633+00:00'
page_id: '267788274'
product: rm
source: tdn-rm
title: TVPUPJ_DT_Provisao_Ferias_Considerando_Media_Discriminada
type: documentation
url: https://tdn.totvs.com/display/LRM/TVPUPJ_DT_Provisao_Ferias_Considerando_Media_Discriminada
version: 113
---

# PROVISÃO DE FÉRIAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Provisão de Férias* |
| **Situação/Requisito:** | Ao gerar o Histórico de Provisão de Férias marcando o flag Abate o valor da diferença de férias do mês para um funcionário que teve diferença de férias e médias, o sistema está considerando o valor do evento de base cálculo de medias de férias no envelope 2 vezes, fazendo com o que o valor do campo Valor pago de férias no mês da provisão de férias fique maior do que o correto. |
| **Solução/Implementação:** | Ajustado cálculo da provisão de férias quando há diferença de férias e evento de discriminação de média de férias. |
| **Chamados relacionados:** | *TVPUPJ* |

divs
