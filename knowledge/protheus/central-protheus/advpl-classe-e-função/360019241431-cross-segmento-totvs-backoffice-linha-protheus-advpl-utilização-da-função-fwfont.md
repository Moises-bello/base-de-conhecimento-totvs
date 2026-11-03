---
article_id: 360019241431
category: ADVPL - Classe e Função
content_hash: 7dbe5749dd2b634a7b1aaacb9f2c9e6e3cca0870a49c177b78d2511428e429d8
fetched_at: '2026-06-28T22:40:18.170147+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Utilização da função
  Fwfontsize
type: support-article
updated_at: '2022-06-14T18:06:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019241431-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Utiliza%C3%A7%C3%A3o-da-fun%C3%A7%C3%A3o-Fwfontsize
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Temos um relatório feito em casa que exporta para superar o resultado. Na v11 funciona bem e a janela que solicita o nome do arquivo a ser gerado mostra a caixa de texto; mas em v12 não. Mesmo quando aumentamos o tamanho da janela, pensamos que não era suficiente mostrar a caixa de texto.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Após a migração para o Protheus 12 onde os botões de ação foram para o Cabeçalho das rotinas, algumas rotinas customizadas tiveram os primeiros campos da tela sobrepostos pela barra de botões padrão (do cabeçalho).

![image2017-10-11_11-33-9.png](http://tdn.totvs.com/download/attachments/306841356/image2017-10-11_11-33-9.png?version=1&modificationDate=1507732389000&api=v2)![image2017-10-11_11-33-33.png](http://tdn.totvs.com/download/attachments/306841356/image2017-10-11_11-33-33.png?version=1&modificationDate=1507732413000&api=v2)

É necessário utilizar a classe FWDefSize pois o posicionamento da sua customização devem está chumbados.  
Na MSDIalog basta manipular os valores do posicionamento " @ 05,005 " ou utilizar a classe FWDefSize

**Saiba mais**[FwDefSize](http://tdn.totvs.com/display/framework/FWDefSize)
