---
content_hash: e5577066408ce721e192e496ba22ddcc4bb2ed785b4455ec794e6ef3d202fd18
fetched_at: '2026-06-29T00:08:19.948428+00:00'
page_id: '267800060'
product: rm
source: tdn-rm
title: TVWWEL_DT_Erro_Data_Pagamento_Lançamento_Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267800060
version: 116
---

# LANÇAMENTO FINANCEIRO - FÉRIAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *LANÇAMENTO FINANCEIRO* |
| **Situação/Requisito:** | *Ao gerar lançamento financeiro o sistema está lançando a data de pagamento de forma errada.*  *Dentro do mesmo período aquisitivo cadastrou férias futuras de 15 dias a ser gozada em outro período. A data de pagamento deste período é posterior ao da competência atual.*  *- Com parâmetro Usar data de pagamento para vencimento do lançamento MARCADO. Este parâmetro está disponível na parametrização do lançamento financeiro 003 (Liquido de Férias)*  *- Ao lançar as férias do período de gozo atual o sistema carregou a data de pagamento futura e não atual. Esta data é referente ao segundo período de gozo (Férias Futuras).* |
| **Solução/Implementação:** | *No caso do parâmetro estar MARCADO a Data de Pagamento do Lançamento Financeiro usará como valor a Data de Pagamento do Período de Gozo em aberto com Data de Pagamento compreendendo dentro do mês da competência atual.* |
| **Chamados relacionados:** | *TVWWEL* |

divs
