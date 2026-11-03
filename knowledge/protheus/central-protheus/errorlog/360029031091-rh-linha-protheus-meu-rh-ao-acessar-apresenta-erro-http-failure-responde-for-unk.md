---
article_id: 360029031091
category: ERRORLOG
content_hash: fda7408327fd3a230c53c97cfd52f1efd68f4ab17cc78ca2679bee6af635f9ac
fetched_at: '2026-06-28T22:44:39.509940+00:00'
product: protheus
section_id: 10299583475863
source: central-protheus
title: RH - Linha Protheus - MEU RH - Ao acessar apresenta erro  http failure responde
  for unknown url
type: support-article
updated_at: '2026-06-18T19:47:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029031091-RH-Linha-Protheus-MEU-RH-Ao-acessar-apresenta-erro-http-failure-responde-for-unknown-url
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24768645286807)Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Como corrigir o erro:   
Servidor não está respondendo. *Http failure responde for (unknown url): 0 unknown Error*  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029902272)  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**Verifique e ajuste o arquivo **properties.json,** onde consta a chave **"ERP"**O correto é "ERP": 3  (sem aspas duplas) e não "ERP": "3" (com aspas duplas), o valor 3 é numérico portanto não deve conter aspas.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360064509333)  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
