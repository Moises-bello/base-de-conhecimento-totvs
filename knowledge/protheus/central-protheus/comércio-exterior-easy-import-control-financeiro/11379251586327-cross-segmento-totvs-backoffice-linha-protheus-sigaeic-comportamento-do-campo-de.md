---
article_id: 11379251586327
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: 909560c81aa37a2ce42ff76ab87a129061b01f6db72b04577581fd601dad36af
fetched_at: '2026-06-28T22:39:44.502656+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Comportamento
  do campo Desconto WB_DESCO durante a compensação do Título dentro do SIGAEIC
type: support-article
updated_at: '2024-04-03T19:22:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11379251586327-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Comportamento-do-campo-Desconto-WB-DESCO-durante-a-compensa%C3%A7%C3%A3o-do-T%C3%ADtulo-dentro-do-SIGAEIC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **02:00 min** **Dúvida**Ao vincularmos um Pagamento Antecipado ao Cambio, não está sendo possível visualizar dentro do Módulo Financeiro o desconto informado ao compensar um título de fechamento de câmbio.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**O campo desconto "**WB\_DESCO**", bem como os campos "**multa**" e "**juros**", são campos específicos da **baixa do título,** ou seja**,** não constam na **inclusão do título** (tabelas **SE1 e SE2**).  
O campo de desconto (**WB\_DESCO**) do câmbio de importação é enviado apenas na liquidação do título **visto que na operação de compensação não é possível enviar tal informação**.   
Como procedimento, após efetuar a compensação, o usuário deverá efetuar a liquidação do saldo residual da parcela de câmbio, onde o sistema irá enviar o desconto para baixar o que ficou de saldo do título.
