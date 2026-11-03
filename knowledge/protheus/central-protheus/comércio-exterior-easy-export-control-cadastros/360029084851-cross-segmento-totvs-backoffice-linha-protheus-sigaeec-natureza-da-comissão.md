---
article_id: 360029084851
category: Comércio Exterior - Easy Export Control - Cadastros
content_hash: ceb9e6eb0ea7a42719ffcecbf5a7ce162b3a31e33dab638a183711aeff59ef88
fetched_at: '2026-06-28T22:36:57.370889+00:00'
product: protheus
section_id: 1500001549302
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Natureza da comissão
type: support-article
updated_at: '2022-06-09T18:50:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029084851-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Natureza-da-comiss%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Onde eu determino qual natureza financeira o título de agente de comissão ira utilizar?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – A partir da versão 11.80  
  
**Solução**Será verificado o fornecedor definido no campo Y5\_FORNECE do cadastro de Empresas (EECAC175), referente ao agente de comissão.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030019391/mceclip1.png)

No cadastro do Fornecedor utilizado será verificado o campo A2\_NATUREZ:   
![](https://totvssuporte.zendesk.com/attachments/token/Gry5H2h7GRcQtEqkQa67aswgy/?name=inline-1546804883.png)​  
Caso não esteja preenchido no cadastro de fornecedor, irá verificar o parâmetro **MV\_AVG0178**.
