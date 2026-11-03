---
article_id: 360047552653
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 5d0e378045612594c875f8fd49d4502cf8dd15ea28cd080050770d096ada1c2f
fetched_at: '2026-06-28T22:39:56.281330+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - AGLUTINAÇÃO
  DE ITENS NFTS
type: support-article
updated_at: '2025-07-14T21:40:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047552653-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-AGLUTINA%C3%87%C3%83O-DE-ITENS-NFTS
---

**Dúvida**Ao transmitir uma NFTS (Nota de Entrada), as telas abaixo são apresentadas:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067860674/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067860854/mceclip2.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**A nota não é transmitida porque há mais de um item e esses itens não foram aglutinados.  
  
Conforme 1ª tela, a aglutinação dos itens no XML deve seguir as seguintes regras:  
  
- O parâmetro MV\_ITEMAGL deve ser igual a S.  
- O parâmetro MV\_NFSEMOD deve ser igual a .T.  
- Todos os itens devem ter a mesma alíquota de ISS.  
- Todos os itens devem ter o mesmo código de ISS.  
- Todos os itens devem ter o mesmo código de Tributação municipal.
