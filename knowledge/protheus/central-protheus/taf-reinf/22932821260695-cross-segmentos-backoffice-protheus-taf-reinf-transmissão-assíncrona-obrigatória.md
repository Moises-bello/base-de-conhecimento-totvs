---
article_id: 22932821260695
category: TAF - REINF
content_hash: 7be367d054f3a7ee31792183da421c36dd07ab62f68142adab2dd1337f7215bf
fetched_at: '2026-06-28T22:41:34.880134+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Transmissão assíncrona
  obrigatória a partir de 07/2024
type: support-article
updated_at: '2024-06-19T17:26:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22932821260695-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Transmiss%C3%A3o-ass%C3%ADncrona-obrigat%C3%B3ria-a-partir-de-07-2024
---

**Dúvida**

  Quais serão as mudanças para as transmissões assíncrona da EFD - REINF a partir de 07/2024?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]  
  
**Solução**

Realizado ajustes conforme a nova NT disponibilizada da versão 2\_01\_02.

Para essa alteração é recomendado que estejam com os schemas atualizados, você pode realizar o download nos link abaixo:

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS?source=search)

**Observação:** a partir da data de entrada em produção, o sistema TSS realizará o envio dos eventos APENAS através do webservice em REST (ainda que os ambientes síncrono - Soap e assíncrono - REST irão coexistir por 06 meses após liberação do ambiente de produção).

Isso não irá afetar em nada os ERPs que utilizam o TSS, será apenas recomendado informar a VERSAOLOTE correta na requisição para envio dos eventos ou então, apenas não informar a VERSAOLOTE.
