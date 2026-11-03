---
content_hash: 10e201dfb3ce0b2103fb6625ed840b81c3ce7bd07864d83bf61cc1833025c313
fetched_at: '2026-06-29T00:10:50.769898+00:00'
page_id: '563421107'
product: rm
source: tdn-rm
title: 9456140 FISCAL01-13916 DT K030 - ECF Período A01/A00
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=563421107
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | ECF |
| Ticket: | 9456140 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13916 |

## **02. SITUAÇÃO/REQUISITO**

Ao validar a ECF foi apresentado a seguinte mensagem: "Período não permitido para esse registro" Registro K030 - Período A01.

## **03. SOLUÇÃO**

Foi realizado um ajuste para que no período de apuração a flag “Período Anual” esteja disponível para tributos IRPJ e CSLL, desde que os mesmos estejam parametrizados com a periodicidade anual. Quando a flag estiver marcada e se no período houver Cisão (Janeiro ou Dezembro) ela será tratada corretamente na rotina.
