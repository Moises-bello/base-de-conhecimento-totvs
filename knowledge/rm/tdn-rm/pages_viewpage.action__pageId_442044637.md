---
content_hash: 4e57aabbedebf8794ef61110ce0c917a3dffafdec47842bd3695995b9c7f377e
fetched_at: '2026-06-29T00:09:53.833742+00:00'
page_id: '442044637'
product: rm
source: tdn-rm
title: 4017804 FOPCALCULO01-5462 Função de Fórmula NDIASDESC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=442044637
version: 1
---

# Função de Fórmula

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Plataforma RH |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Função de Fórmula |
| **Situação/Requisito:** | Ao incluir uma jornada no horário por intervalo e na etapa Intervalo da jornada marcar a opção "Determinar ocorrência a ser gerada" setando o tipo de ocorrência a ser gerada "T - Trabalho" para todos os intervalos, o registro não é gravado na tabela ABATHOR. Isso está impactando no funcionamento da variável NDIASDESC do Labore, pois ela valida os registros da tabela ABATHOR. |
| **Solução/Implementação:** | Ajustado a Função de Fórmula NDIASDESC para retornar os dias de descanso quando é determinada a ocorrência gerada na jornada trabalhada. |
| **Tickets relacionados:** | 4017804 |
