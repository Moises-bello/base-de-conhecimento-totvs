---
article_id: 360042507314
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: f7bd4b6a3efdb36e07d8026e6a2e49ac962730bf6a2e1826734174d91d26e7f1
fetched_at: '2026-06-28T22:39:58.589355+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - TSS: SÃO
  PAULO: 1204 : Valor Total de Serviços não confere com o enviado (0)'
type: support-article
updated_at: '2021-10-06T19:09:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042507314-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-TSS-S%C3%83O-PAULO-1204-Valor-Total-de-Servi%C3%A7os-n%C3%A3o-confere-com-o-enviado-0
---

**Dúvida**Rejeição na transmissão da nfse de São Paulo-SP:  
1204 : Valor Total de Serviços não confere com o enviado (0)  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.

**Solução**A tag <ValorTotalServicos> compõe o cabeçalho do lote, esse conteúdo pode ser coletado no campo XML\_LOTE da tabela SPED053.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057725933/mceclip0.png)

A tag <ValorTotalServicos> carrega o mesmo conteúdo da tag <ValorServicos> do corpo do XML.  
Normalmente a prefeitura apresenta essa rejeição quando ocorre alguma falha no processamento das notas.  
Nesse caso a solução é retransmitir a mesma nota após alguns minutos.
