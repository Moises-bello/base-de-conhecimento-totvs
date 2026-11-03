---
article_id: 360034692573
category: RH - Dissídio
content_hash: 13ef1a68b86d277a1cefb23d727b1f6d99c8d1daafe11e2e3beea20f522bfdd7
fetched_at: '2026-06-28T22:43:44.260289+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - mensagem dissidio - Informe o código de pagamento
  em todas as verbas com incidência para dissidio
type: support-article
updated_at: '2025-08-20T14:30:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034692573-RH-Linha-Protheus-GPE-mensagem-dissidio-Informe-o-c%C3%B3digo-de-pagamento-em-todas-as-verbas-com-incid%C3%AAncia-para-dissidio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34317201714839) Tempo aproximado para leitura: 00:00:30 min**

**Dúvida**Ao acessar a rotina dissidio retroativo (GPEM690) sistema gera a seguinte mensagem: "Informe o código de pagamento em todas as verbas com incidência para dissidio... " conforme imagem abaixo:

![2019-08-21_11_05_35-LogMeIn_Rescue_Technician_Console.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045078873)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Existem verbas que estão configuradas com sim para dissidio porem sem o código correspondente conforme o exemplo abaixo

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044217694)

Para identificar quais verbas estão neste cenário solicite ao T.I para efetuar o seguinte filtro:

Acessar a tabela SRV e efetuar o seguinte filtro: RV\_COMPL\_ = S and RV\_CODCOM\_ = branco.

Após isso preencher o código da verba corresponde para dissidio para que a mensagem deixe de ser gerada.

Saiba Mais:  
[Página Centralizadora do Dissídio (GPEM690)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
