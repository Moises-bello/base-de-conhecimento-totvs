---
article_id: 11645859436823
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 0f69aab875792b6c20b3585fa4b2488e8c9897f3105f2a4f841f1db6498c2c6e
fetched_at: '2026-06-28T22:38:57.157387+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA311 não transfere
  (destino) para Armazém de CQ (MV_CQ) como na MATA261
type: support-article
updated_at: '2023-01-13T13:52:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11645859436823-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA311-n%C3%A3o-transfere-destino-para-Armaz%C3%A9m-de-CQ-MV-CQ-como-na-MATA261
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Por que a rotina ***SOLICITAÇÃO DE TRANSFERÊNCIA (MATA311)*** não permite transferências com destino ao Armazém de Qualidade (MV\_CQ)? Ao tentar transferir para o Armazém de CQ apresenta o **Help: Armaz. Dest**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11645949704087)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**A rotina Solicitação de Transferências (MATA311) não foi concebida para realizar este tipo de operação. O objetivo da rotina é realizar transferência entre filiais e entre armazéns, ***excluindo o processo de CQ***.

Nesse cenário, quando precisa efetuar uma Transferência ao CQ deve utilizar a rotina **TRANSFERÊNCIAS MÚLTILPAS (MATA261)**. Veja também como utilizar a rotina MATA261, ***[clique aqui](https://www.youtube.com/watch?v=-C05diWV9D4)***

Veja também a FAQ com instruções padrões sobre envio ao CQ [***clique aqui***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025518774-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Rotina-MATA175-Instru%C3%A7%C3%B5es-padr%C3%B5es-sobre-Controle-de-Qualidade-no-Estoque)

***Saiba Mais:***  
*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
