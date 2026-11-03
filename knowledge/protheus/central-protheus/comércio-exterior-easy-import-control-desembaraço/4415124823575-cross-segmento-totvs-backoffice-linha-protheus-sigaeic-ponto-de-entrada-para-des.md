---
article_id: 4415124823575
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 9318f740fc496c7879024b2c4c41cf5afac87b57cca46ba352af94da1396e663
fetched_at: '2026-06-28T22:39:50.151058+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Ponto de entrada
  para desabilitar o botão altera adição
type: support-article
updated_at: '2021-12-15T13:34:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415124823575-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Ponto-de-entrada-para-desabilitar-o-bot%C3%A3o-altera-adi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Temos algum ponto de entrada para desabilitar o botão "altera adição"  da rotina recebimento de importação (EICDI154)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões

**Solução**Utilize o parâmetro **INICIA\_VARIAVEIS** e peça para alterar a variável **lAlteraAdicaoPE** para falso.  
Isso será o suficiente para que o botão Altera Adições fique desabilitado na rotina de recebimento de importação. Reforçando que este ponto de entrada é para o cenário o cliente que utiliza o parâmetro MV\_TEM\_DI = F .

**Saiba mais**  
[PE EICDI154 - Recebimento de Importação](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=574364993)
