---
article_id: 360020262791
category: ADVPL - Ponto de Entrada
content_hash: 86f8fc76ddb7414f0f62380f92b43aaa6a01c75bcf72ecf614e7d39462b679d0
fetched_at: '2026-06-28T22:40:12.905264+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Utilização do ponto
  de entrada FINA181
type: support-article
updated_at: '2021-12-30T18:07:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020262791-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Utiliza%C3%A7%C3%A3o-do-ponto-de-entrada-FINA181
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Estamos criando o PE F171RDMN, e observamos se o SEH->EH\_TIPO for igual CDI, o ponto de entrada nao chama. Como podemos fazer nesse caso, pois é necessário manipular o valor do rendimento do resgate, pois a diferença no calculado no sistema e no extrato bancário.   
<http://tdn.totvs.com/pages/releaseview.action?pageId=317316447>  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**O ponto de entrada foi criado para atender a aplicações por cotas (como  descrito na documentação do ponto de entrada).  Como o CDI não é uma aplicação por cotas mas uma aplicação indexada por índice definido por órgão oficial, que publica os valores do DI., o ponto de entrada não é executado.
