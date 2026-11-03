---
article_id: 360049715914
category: Financeiro - Contas a Receber - LCDPR
content_hash: 3545ed1e317e5511edcb5bc8d6dc173113e5615e2705ee7ed5221b69a255d7dd
fetched_at: '2026-06-28T22:38:15.811380+00:00'
product: protheus
section_id: 1500001539361
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - FINA820 -   O
  Extrator do LCDPR traz informações de títulos emitidos em ano diferente do range
  informado
type: support-article
updated_at: '2022-03-24T20:15:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049715914-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FINA820-O-Extrator-do-LCDPR-traz-informa%C3%A7%C3%B5es-de-t%C3%ADtulos-emitidos-em-ano-diferente-do-range-informado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:02 min  
  
Dúvida**O Extrator do LCDPR está trazendo informações de títulos que foram emitidos em ano diferente do range informado na rotina FINA820?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – A partir da versão 12  
  
**Solução**Caso tenha títulos que foram gerados no ano de 2018 por exemplo, porém tiveram suas baixas efetuadas em 2019, e na geração do extrator do **LCDPR** esteja inserindo um range do ano de 2019, o mesmo irá ser apresentado, pois o **LCDPR** irá carregar as informações da **SE5**, e não irá considerar o ano de emissão do titulo.
