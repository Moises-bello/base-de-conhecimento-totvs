---
content_hash: 460a415b4477874cf8309c943de2d964959019ba5f91a37dd53b3d495e5f22cc
fetched_at: '2026-06-29T00:10:50.570819+00:00'
page_id: '561855747'
product: rm
source: tdn-rm
title: 8883139 FISCAL01-13265 DT - DANFE - Ajuste na descrição do Frete da NF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=561855747
version: 5
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | DANFE |
| Ticket: | 8883139 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13265 |

## **02. SITUAÇÃO/REQUISITO**

Atualizar a descrição do Frete da NF-e de acordo com a NT.

## **03. SOLUÇÃO**

Foi atualizado a descrição do frete no processo de impressão da DANFE visando atender a norma técnica

Para não haver quebra de linha, o RM está gerando as descrições do Frete da seguinte forma:

| NT 2018.005 | RM |
| --- | --- |
| 0 - Contratação do Frete por conta do Remetente (CIF) | 0 - Frete por conta do Remetente (CIF) |
| 1 - Contratação do Frete por conta do Destinatário (FOB) | 1 - Frete por conta do Destinatário (FOB) |
| 2 - Contratação do Frete por conta de Terceiros | 2 - Frete por conta de Terceiros |
| 3 - Transporte Próprio por conta do Remetente | 3 - Transporte Próprio do Remetente |
| 4 - Transporte Próprio por conta do Destinatário | 4 - Transporte Próprio do Destinatário |
| 9 - Sem Ocorrência de Transporte. | 9 - Sem Transporte |
