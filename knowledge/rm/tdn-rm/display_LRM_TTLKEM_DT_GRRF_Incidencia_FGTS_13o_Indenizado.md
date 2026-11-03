---
content_hash: 68dd3ce9402fd4950e441650ca2df6d42e42f556a0eb86996828ad13595e221c
fetched_at: '2026-06-29T00:06:23.095690+00:00'
page_id: '223932731'
product: rm
source: tdn-rm
title: TTLKEM_DT_GRRF_Incidencia_FGTS_13o_Indenizado
type: documentation
url: https://tdn.totvs.com/display/LRM/TTLKEM_DT_GRRF_Incidencia_FGTS_13o_Indenizado
version: 1
---

# GRRF NÃO ESTÁ RESPEITANDO INCIDÊNCIA DE FGTS NO 13o.INDENIZADO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *GRRF* |
| **Situação/Requisito:** | *Na geração da GRRF não está respeitando a incidência de FGTS do evento de CC 71, 13o. Indenizado.*  *Independente de estar marcada ou não a incidência, o valor do CC 71 está sendo considerado na Base de FGTS de 13o.*  *O cliente possui Liminar para não recolher FGTS sobre as verbas indenizatórias, Aviso Prévio Indenizado e 13º Salário Indenizado.* |
| **Solução/Implementação:** | *Ajuste na geração da GRRF para respeitar a incidência de FGTS do evento de CC 71, 13o. Indenizado.*  *Ou seja, só haverá recolhimento de FGTS sobre o valor do 13o. Indenizado, se no evento estiver marcada a incidência em FGTS.* |
| **Chamados   relacionados:** | *TTLKEM, TUAMV3* |
| **Versões/Release:** | *11.82.43, 12.1.10* |
