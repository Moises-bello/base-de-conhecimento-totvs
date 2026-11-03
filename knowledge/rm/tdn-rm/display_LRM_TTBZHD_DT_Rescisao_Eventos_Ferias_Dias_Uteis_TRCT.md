---
content_hash: 77d53f2bcda6d484c8fbccb1d37d2d1d45eef57c941da80d34314309595126cc
fetched_at: '2026-06-29T00:06:06.840633+00:00'
page_id: '201732169'
product: rm
source: tdn-rm
title: TTBZHD_DT_Rescisao_Eventos_Ferias_Dias_Uteis_TRCT
type: documentation
url: https://tdn.totvs.com/display/LRM/TTBZHD_DT_Rescisao_Eventos_Ferias_Dias_Uteis_TRCT
version: 1
---

# RESCISÃO EVENTOS TRCT FÉRIAS DIAS UTEIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão* |
| **Situação/Requisito:** | *Quando é utilizado o parâmetro de férias com dias úteis, no cálculo dos eventos de férias para o TRCT na rescisão, CC's 329 e 330, o número de dias corridos está considerando o mesmo feriado nos dois eventos.* |
| **Solução/Implementação:** | *No cálculo do evento de CC 329 - FÉRIAS INDENIZADAS SOBRE AVISO PRÉVIO, quando é utilizado o recurso de férias com dias úteis, fazer a contagem dos dias corridos considerando o número encontrado no CC 330 - FÉRIAS PROPORCIONAIS SEM AVISO PRÉVIO.*  *Se a prioridade do evento de CC 329 estiver anterior ao CC 330, ele deverá ser recalculado novamente após o cálculo do evento de CC 330.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTBZHD* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
