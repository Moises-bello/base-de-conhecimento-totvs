---
content_hash: ca9ef6dffc5fb23b1c857589582c2b11c4bd248bc5dc16b1869556de2a318144
fetched_at: '2026-06-29T00:06:08.499594+00:00'
page_id: '201748600'
product: rm
source: tdn-rm
title: TTDPXA_DT_Importacao_Eventos_Ferias_DtPagto_Meses_Anteriores
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDPXA_DT_Importacao_Eventos_Ferias_DtPagto_Meses_Anteriores
version: 1
---

# IMPORTAÇÃO DE MOVIMENTO DE FÉRIAS COM DATA DE PAGAMENTO EM MESES ANTERIORES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Importação de Movimento* |
| **Situação/Requisito:** | *Importação de movimento não permite registros com data de pagamento anteriores ao mês anterior a competência atual.*  *Só é permitido data de pagamento na competência anterior, na competência atual, e na competência seguinte.*  *Cliente necessita importar eventos de férias com data de pagamento 2 meses antes do atual.* |
| **Solução/Implementação:** | *Tratar no processo de Importação de Movimento para, somente quando for evento de férias, permitir datas de pagamento anteriores.*  *O evento é identificado como sendo de férias quando na posição 81 está informado S. Qualquer outro conteúdo indica que não é evento de férias.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTDPXA* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
