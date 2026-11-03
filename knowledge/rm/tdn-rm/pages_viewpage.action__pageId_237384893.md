---
content_hash: 651350ec19266b2edd3637bb89d93b497f7d34c86b2bee6d1bc55079fb03a419
fetched_at: '2026-06-29T00:08:07.679105+00:00'
page_id: '237384893'
product: rm
source: tdn-rm
title: TTUWWW_DT_Movimento_Devolucao_Buscar_Pauta_No_Período_Do_Movimento_Devolvido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=237384893
version: 2
---

# Movimento Devolução Buscar Pauta No Período Do Movimento Devolvido

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Função:** | Inclusão de Movimento via Cópia por Referência. |
| **Situação/Requisito:** | Ao calcular base de cálculo de ICMS que utiliza pauta do produto, o sistema considera o período de vigência como sendo  do movimento incluído e não o do movimento devolvido. Assim, a base de cálculo do tributo difere do valor original na devolução. |
| **Solução/Implementação:** | Acerto na busca do preço da pauta do produto para calcular a base de cálculo do ICMS pautado. Se for um movimento de devolução o sistema  considera o período de vigência da pauta como sendo do movimento devolvido. |
| **Conversores e Parâmetros:** | *NA.* |
| **Chamados relacionados:** | *TVAG09* |
| **Requisito (ISSUE):** | *NA.* |
