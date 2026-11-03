---
content_hash: 6fd903a5a8fd24a0a23f5fa115c3890958502d0b7810e6130705914f7dc39f51
fetched_at: '2026-06-29T00:06:08.507780+00:00'
page_id: '201748776'
product: rm
source: tdn-rm
title: TTFTUT_DT_Importacao_Eventos_Ferias_DtPagto_Meses_Anteriores
type: documentation
url: https://tdn.totvs.com/display/LRM/TTFTUT_DT_Importacao_Eventos_Ferias_DtPagto_Meses_Anteriores
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
| **Chamados relacionados:** | *TTFTUT* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
