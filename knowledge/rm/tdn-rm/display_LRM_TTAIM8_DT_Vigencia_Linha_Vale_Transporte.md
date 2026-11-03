---
content_hash: f40dd9fc576ccc7cc42d795e41fa68955922ed47ac31e0934f5ec81dddb58222
fetched_at: '2026-06-29T00:06:06.210288+00:00'
page_id: '201729304'
product: rm
source: tdn-rm
title: TTAIM8_DT_Vigencia_Linha_Vale_Transporte
type: documentation
url: https://tdn.totvs.com/display/LRM/TTAIM8_DT_Vigencia_Linha_Vale_Transporte
version: 4
---

# PERIODO DE VIGÊNCIA DAS LINHAS DE VT

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Vale Transporte* |
| **Situação/Requisito:** | *No cálculo do Total Entregue de Vale Transporte, CC 32,  não está considerando corretamente as datas de vigência da Linha que estão iniciando ou terminando durante o mês.* |
| **Solução/Implementação:** | *Ajustar no cálculo do evento de Vale Transporte (CC 32) para efetuar o lançamento do total entregue, considerando o dia correto das datas de vigência que estiverem iniciando e terminando durante o mês competência.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTAIM8* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
