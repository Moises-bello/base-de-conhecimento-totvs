---
article_id: 360024609612
category: ADVPL - Classe e Função
content_hash: 5d132fa7cc03f69164976006d2fccc7da8fd5a17c650994397beb66669d1f302
fetched_at: '2026-06-28T22:40:17.111879+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Qual a função usar
  para ter a opção procura no relatório com TReport()
type: support-article
updated_at: '2023-05-18T14:59:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024609612-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Qual-a-fun%C3%A7%C3%A3o-usar-para-ter-a-op%C3%A7%C3%A3o-procura-no-relat%C3%B3rio-com-TReport
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Qual a função usar para ter a opção procura no relatório com TReport()?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Não é possível realizar este procedimento. A classe TREPORT é uma classe gráfica, quando gerado em TReport, a opção PESQUISAR  não existe devido o relatório esta montado em uma IMAGEM(JPEG, BMP...), diferente da classe SetPrint() - não gráfico que é montado em TXT, onde é possível fazer a pesquisa em um arquivo .TXT  
  
**Saiba Mais****[Treport](http://tdn.totvs.com/pages/viewpage.action?pageId=415715475)**
