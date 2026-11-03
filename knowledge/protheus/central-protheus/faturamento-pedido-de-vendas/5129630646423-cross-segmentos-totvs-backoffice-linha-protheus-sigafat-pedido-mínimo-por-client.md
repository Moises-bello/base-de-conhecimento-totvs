---
article_id: 5129630646423
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: d7e16b6128c4f367ee3fd68da424a39db451fa08f6786bc66c636c49258cde9e
fetched_at: '2026-06-28T22:38:42.765350+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Pedido mínimo
  por cliente '
type: support-article
updated_at: '2022-10-19T18:36:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5129630646423-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pedido-m%C3%ADnimo-por-cliente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00** **min** **Dúvida**Como limitar o valor minimo para inclusão de um Pedido por cliente   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - Todas as versões  
  
**Solução**  
No pedido de venda não há parametrização para esta finalidade, teria que trabalhar com ponto de entrada na confirmação do pedido.  
  
No faturamento, você tem a pergunta do botão prep docs, Vl.Minimo p/Faturar, e nesta pergunta você coloca o valor mínimo para que a nota seja faturada, porém, não é possível tratar por cliente, cada vez que faturar teria que ajustar o valor.  
  
Caso opte por ponto de entrada na confirmação do pedido, segue os possíveis pontos abaixo:  
  
**mt410inc: <http://tdn.totvs.com.br/display/PROT/MT410INC>**  
**mt410tok:<http://tdn.totvs.com.br/pages/viewpage.action?pageId=6784353>**  
**m410inic:<http://tdn.totvs.com.br/pages/viewpage.action?pageId=6784147>**
