---
content_hash: f5b380626dd6c91cb91883c3e05cb203aa5321b9641afa0a19a56c3ddadbc05c
fetched_at: '2026-07-02T19:24:25.682408+00:00'
page_id: '501129407'
product: protheus
source: tdn-tec
title: Correção - Diferenças de pintura entre SmartClient 131227A e Lobo Guara (Logix)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=501129407
version: 2
---

|  |  |
| --- | --- |
| Situação | Ao testar o SmartClient Lobo Guara no ERP Logix, algumas telas apresentaram diferenças de pintura/comportamento |
| Ocorrência | Desde o port feito para o Qt5 as telas do Logix não foram utilizadas, portanto faltaram alguns detalhes para compatibilizar as duas versões. |
| Correção | * Diferença de tamanho em dialog 4gl em comparação com a versão 131227A * QTabWidget (t4jsTab) não estava reconhecendo os eventos de mudança de aba * As bordas em telas 4gl estavam com uma pequena diferença na pintura entre as versões |
| Informações adicionais | * Referente à ocorrência: ITEC-434 * Disponível em builds superiores a 7.00.170117A - 17.3.0.9 |
