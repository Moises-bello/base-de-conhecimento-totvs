---
article_id: 360036111734
category: ADVPL - Classe e Função
content_hash: a850edf2f6e61f97a9e00894bade3dc0aaac1b244e9c0723aab805726dc94b99
fetched_at: '2026-06-28T22:40:20.481737+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Leitura de arquivo
  XLS
type: support-article
updated_at: '2023-09-05T12:32:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036111734-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Leitura-de-arquivo-XLS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min****Dúvida**Existe uma função ADVPL para ler uma planilha em formato XLSX ou XLS?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) - ADVPL - A partir da versão 11.80  
  
**Solução**Não existe função que leia o arquivo XLS e XLSX.  
Você pode gerar um arquivo .xml e utilizar a classe [TXmlManager](https://tdn.totvs.com/display/tec/Classe+TXmlManager) para realizar a leitura segue abaixo o link com mais informações.  
Ou pode gerar um arquivo .csv e utilizar a função [FOPEN](https://tdn.totvs.com/pages/viewpage.action?pageId=24346906)() para leitura, conforme a documentação abaixo.
