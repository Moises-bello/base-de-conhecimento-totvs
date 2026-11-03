---
article_id: 360026445694
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: d87e986b9aa3955c8a7cabc589b0787d9eb1c9ee8213fb2beb8a657123c1dcf5
fetched_at: '2026-06-28T22:39:58.422765+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Rejeição
  1057: Assinatura difere do calculado'
type: support-article
updated_at: '2025-06-25T21:04:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026445694-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Rejei%C3%A7%C3%A3o-1057-Assinatura-difere-do-calculado
---

**Dúvida**Ao transmitir uma NFTS para prefeitura de São Paulo-SP, ocorre a rejeição:  
1057: Assinatura difere do calculado  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**Esse erro ocorre quando há carácter especial no conteúdo da nota, portanto revise todos os cadastros envolvidos, inclusive a discriminação dos serviços.  
Remova os caracteres especiais, refaça a nota e transmita.  
Se a rejeição ainda persistir, abra um ticket junto ao suporte enviando a tabela SPED053 em dbf e fpt filtrada pela nota em questão.
