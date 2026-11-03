---
article_id: 4407666520087
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 4aff5beb1bd1b0cc43805c23b575da2f8561517d6d2282e04bc2e2d97038f9ff
fetched_at: '2026-06-28T22:39:50.068185+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Forçar estorno
  de NF com integração Logix
type: support-article
updated_at: '2021-09-02T20:26:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407666520087-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-For%C3%A7ar-estorno-de-NF-com-integra%C3%A7%C3%A3o-Logix
---

**Dúvida**Como posso realizar o estorno de uma nota fiscal no Protheus que não se encontra mais no Logix e é exibida a mensagem "Solicitação de estorno enviada ao ERP. Aguarde a autorização da SEFAZ e tente novamente o estorno da nota fiscal."?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Import Control* – Todas versões  
  
**Solução**Se de fato, for confirmado que no logix o estorno da nota já ocorreu e ficou desbalanceado, ou seja, com a informação da nota apenas no recebimento de importação (EICDI154) no protheus, com o nível de usuário igual ou superior a 7 é possível forçar o estorno.  
​​Ao acessar o módulo 17- SIGAEIC com o usuário igual ou superior a 7, aparecerá no recebimento de importação (EICDI154) a opção de "Forçar o Estorno".  
Acessar em Atualizações -> Desembaraço ->Recebimento de Importação (EICDI154), posicione na nota a ser estornada e selecione a mesma, será apresentada a opção "Forçar o Estorno":  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407690709527/mceclip0.png)  
  
​Isso excluirá a nota no SIGAEIC, sem enviar nenhum tipo de mensagem para o Logix.  
  
Observação:  
**Reforçando que esse procedimento só deve ser feito se tiver realmente certeza que a nota não se encontra no Logix.**

**Saiba mais**[Easy Import Control via Mensagem Única](TVFETN_DT_Integra%C3%A7%C3%A3o%20do%20Easy%20Import%20Control%20via%20Mensagem%20%C3%9Anica%20-%20EAI%20-%20Linha%20Microsiga%20Protheus%20-%20TDN)
