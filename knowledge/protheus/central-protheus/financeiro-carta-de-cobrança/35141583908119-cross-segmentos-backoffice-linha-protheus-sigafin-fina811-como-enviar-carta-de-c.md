---
article_id: 35141583908119
category: Financeiro - Carta de Cobrança
content_hash: 16f4c0b921ead0afc7f1fa888515fe0dc714b095682833639d76b46769929f13
fetched_at: '2026-06-28T22:37:28.980778+00:00'
product: protheus
section_id: 35058223754903
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA811 - Como enviar
  carta de cobrança para mais de um e-mail
type: support-article
updated_at: '2025-09-23T17:03:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35141583908119-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA811-Como-enviar-carta-de-cobran%C3%A7a-para-mais-de-um-e-mail
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35141539456407) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como enviar carta de cobrança para mais de um e-mail?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

Neste caso, é necessário ajustar o campo **AI0\_EMAIL** no cadastro de clientes, aonde é possível adicionar mais e-mails, separando os mesmos por ponto e virgula. Desta forma também servira como uma forma de comprovar que o e-mail foi enviado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35141583880343)  
  
Existe o ponto de entrada a seguir, caso queira customizar, porém ele só funcionara para o processo de cartas de cobranças em si, não funcionara para o processo de boletos via API.  
  
[F811MAILTO](https://tdn.totvs.com/pages/releaseview.action?pageId=730064536) - Permite definir outro e-mail para envio da carta de cobrança
