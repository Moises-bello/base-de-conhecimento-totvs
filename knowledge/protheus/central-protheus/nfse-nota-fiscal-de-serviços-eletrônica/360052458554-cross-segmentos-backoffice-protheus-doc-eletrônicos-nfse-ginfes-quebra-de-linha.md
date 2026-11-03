---
article_id: 360052458554
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 9deb7019875a0339790eb8878dbd486bb630f49d570b864367ea71bf681e0737
fetched_at: '2026-06-28T22:39:57.463311+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - GINFES:
  QUEBRA DE LINHA NA DISCRIMINAÇÃO'
type: support-article
updated_at: '2025-07-08T19:41:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052458554-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-GINFES-QUEBRA-DE-LINHA-NA-DISCRIMINA%C3%87%C3%83O
---

**Dúvida**Qual é a configuração de quebra de linha na discriminação dos serviços para municípios Ginfes?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**O layout GINFES respeita a configuração de quebra de linha do ERP, sem a necessidade de caracteres para indicar a quebra de linha.

Exemplo de preenchimento do campo memo no Protheus:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086327533/mceclip0.png)  
  
Exemplo do xml gerado respeitando a quebra de linha do Protheus:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086327653/mceclip1.png)  
  
**Observação:**Para utilização do campo tipo memo, é preciso realizar a parametrização abaixo:  
MV\_NFSEMOD=.T.  
MV\_NFEDESC=.F.  
MV\_NFESERV=1  
MV\_CMPUSR= (Informar o campo criado na tabela SC5 como do tipo: MEMO)
