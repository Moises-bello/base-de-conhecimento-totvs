---
article_id: 360022273672
category: ADVPL - Classe e Função
content_hash: dbc301c4ba3758fa495ae616809081c17167692cce7658677e1199cc53f7d339
fetched_at: '2026-06-28T22:40:17.986168+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - SaveToPng salvar
  imagem no servidor '
type: support-article
updated_at: '2022-06-13T21:30:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022273672-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-SaveToPng-salvar-imagem-no-servidor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min****Dúvida**Estou utilizando o método saveToPng da classe FWChartBar, e o mesmo não me permite salvar no servidor, somente local. É preciso que seja salvo no servidor. Qual o procedimento?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**A classe [FWCHART](http://tdn.totvs.com/display/public/PROT/FwChart) herda o método SAVETOPNG da classe [TPAINTPANEL](http://tdn.totvs.com/display/tec/TPaintPanel) e não é possível utilizar o método SaveToPng para salvar diretamente no servidor.  
Recomendamos o uso da função **[CpyT2S](http://tdn.totvs.com/display/tec/CpyT2S)** para a cópia do arquivo do Client para o Server.
