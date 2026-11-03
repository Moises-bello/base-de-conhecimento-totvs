---
article_id: 17157968980247
category: Financeiro - Carta de Cobrança
content_hash: a64d4a6dae60226e372f2ea988c45dd4aa3d16ab5a25cdc11b0d1982dae44c9e
fetched_at: '2026-06-28T22:37:28.966374+00:00'
product: protheus
section_id: 35058223754903
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Diferença entre envio
  da carta de cobrança FINA713 e FINA811
type: support-article
updated_at: '2026-01-16T19:31:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17157968980247-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Diferen%C3%A7a-entre-envio-da-carta-de-cobran%C3%A7a-FINA713-e-FINA811
---

**Dúvida**  
Não é enviado no corpo do e-mail a informação dos títulos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

Na rotina **Job de Transmissão dos Boletos (FINA713)**, **o boleto gerado via API é enviado**, permitindo a personalização da mensagem padrão no corpo do e-mail. Contudo, essa mensagem não incluirá as informações referentes aos títulos.

De acordo com a documentação, para que o envio do boleto via API seja realizado, é imprescindível o preenchimento da carta de cobrança.

As informações serão extraídas do **"Layout configurado",** conforme o print abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32455179541015)  
   
**Saiba Mais**  
[Parametrização de Carta de Cobrança - FINA810](https://tdn.totvs.com/pages/releaseview.action?pageId=615384255)  
 

Na rotina **Envio de Carta de Cobrança (FINA811)**, é encaminhado apenas um comunicado ao cliente sobre os títulos em atraso com base no cadastro FINA810. Dessa forma, os detalhes dos títulos são especificados no corpo do e-mail, mas o boleto em si não é enviado. Conforme a documentação, a carta de cobrança destina-se exclusivamente a alertar o cliente quanto aos títulos em atraso, sem proceder com o envio do boleto.

Dispomos dos seguintes pontos de entrada na rotina **FINA713**, nos quais é possível personalizar o envio do boleto.

As informações serão extraídas da aba **"Dados dos Títulos"**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32455179546903)

**Saiba Mais**  
[JOB Transmissão e Envio de E-mail - FINA713](https://tdn.totvs.com/pages/releaseview.action?pageId=619130482)  
![](https://totvssuporte.zendesk.com/attachments/token/po20xDsXdIVGY1Y5GYWMkIQbT/?name=image.png)
