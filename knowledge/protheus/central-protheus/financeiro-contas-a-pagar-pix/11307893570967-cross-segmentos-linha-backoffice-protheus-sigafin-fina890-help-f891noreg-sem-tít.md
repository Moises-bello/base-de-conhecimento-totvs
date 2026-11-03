---
article_id: 11307893570967
category: Financeiro - Contas a Pagar - PIX
content_hash: b8b1637c1a9dc3129d631e92585a042c4a3236ac85b78dbddca4f0114197fb53
fetched_at: '2026-06-28T22:38:11.348643+00:00'
product: protheus
section_id: 1500001550462
source: central-protheus
title: 'Cross Segmentos - Linha Backoffice Protheus - SIGAFIN - FINA890 - Help: F891NOREG
  - Sem Títulos para Seleção '
type: support-article
updated_at: '2022-12-29T21:02:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11307893570967-Cross-Segmentos-Linha-Backoffice-Protheus-SIGAFIN-FINA890-Help-F891NOREG-Sem-T%C3%ADtulos-para-Sele%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar (A geração da remessa PIX via FINA890) é apresentado o HELP: **F891NOREG - Sem Títulos para Seleção**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11307643741975)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da Release 12.1.33  
  
**Causa**Esse incidente ocorre, pois o parâmetro **MV\_BCOPIX** está igual a 1 ou 2, com isso já grava a informação do banco no campo **F71\_CODBAN**, onde para gerar a remessa as informações de banco devem estar em branco na tabela F71.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Ajustar o parâmetro **MV\_BCOPIX** para "3"   
2. Ajustar os registros já gravados na tabela **F71**  
3. Realizar novamente a geração da remessa  
  
**Saiba mais:**  
[Pagamentos instantâneos - PIX](https://tdn.totvs.com/pages/releaseview.action?pageId=569478747)
