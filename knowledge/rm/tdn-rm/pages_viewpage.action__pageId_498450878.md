---
content_hash: 6181d434adc7002327975009c9426a6ebbe3023459d83882fa17d79c2a41cdca
fetched_at: '2026-06-29T00:10:22.655030+00:00'
page_id: '498450878'
product: rm
source: tdn-rm
title: 6212093 FISCAL01-9910 DT - Diferencial de Alíquota - vICMSUFDest
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=498450878
version: 2
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Inclusão de Movimento |
| Ticket: | 6212093 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-9910 |

**02. SITUAÇÃO/REQUISITO**

Este incidente ocorre quando informado a alíquota interestadual maior que a alíquota interna do estado de destino.  
OBS: A alíquota interna do estado de destino é menor devido ao NCM utilizado.

Alíquota Interestadual - 12%  
Alíquota Interna - 7%  
NCM - 84715020

**03. SOLUÇÃO**

Foi alterado a geração do valor da tag *vICMSUFDest* e *vICMSUFRem* que agora quando o valor do Diferencial de Alíquota (interestadual/interno)for negativo as tags serão zeradas.
