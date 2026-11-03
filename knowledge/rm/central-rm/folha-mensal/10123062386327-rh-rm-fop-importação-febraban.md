---
article_id: 10123062386327
category: Folha Mensal
content_hash: df7e8bfcc80773ec3d82ebccafdbe759bce672bef6e19e4d541751b20e76f458
fetched_at: '2026-06-28T22:46:58.329444+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Importação FEBRABAN
type: support-article
updated_at: '2024-09-16T19:40:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10123062386327-RH-RM-FOP-Importa%C3%A7%C3%A3o-FEBRABAN
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:39 min****Dúvida**Como realizar a importação do arquivo FEBRABAN?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões **Solução**  
Importação do arquivo de retorno do banco:1. É necessário criar o evento com [código de cálculo 194](https://tdn.totvs.com/pages/releaseview.action?pageId=452718651) e vincular na rotina de **Importação Empréstimo Consignado Febraban;  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10122931612311)**

2. Em seguida localize e importe o arquivo **layout CDC – Empréstimo Consignação em Folha – Padrão FEBRABAN** enviado pela Financeira para desconto do empréstimo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10122935044503)

Aqui você busca o arquivo e associa  o evento criado:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10122971045271)

**Observação:**A importação não gera histórico, somente o lançamento no envelope.  
  
Nesse caso, a extensão do arquivo **layout CDC – Empréstimo Consignação em Folha – Padrão FEBRABAN** deverá ser .RET.  
  
![](https://totvssuporte.zendesk.com/attachments/token/bLIOV0XftVHHmu9yMsgW3IbOZ/?name=image.png)  
  
**Saiba Mais:**

[Importação de Empréstimo Consignado FEBRABAN](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719677)
