---
article_id: 15671908709911
category: Financeiro - Contas a Receber - Comunicação Bancária Online
content_hash: 113abca140d303b8a13f4eab741d33aa8e12a842e30dc4e167f7fc066adf65de
fetched_at: '2026-06-28T22:37:49.177613+00:00'
product: protheus
section_id: 26656227629847
source: central-protheus
title: Cross Segmentos  - Backoffice Linha Protheus - SIGAFIN - FINA713 - Caminho
  padrão para a gravação dos certificados dos bancos
type: support-article
updated_at: '2026-03-25T14:40:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15671908709911-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Caminho-padr%C3%A3o-para-a-grava%C3%A7%C3%A3o-dos-certificados-dos-bancos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15671890409239) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Qual o caminho padrão para a gravação dos certificados dos bancos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

O sistema validará em sua pasta **protheus\_data** a existência dos arquivos dos certificados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15671595523863)

É necessária a criação das pastas **cert** e **ngf.**

Conforme o caminho a seguir: **PROTHEUS\_DATA\cert\ngf.**

Inserindo os certificados na **pasta NGF,**o sistema já irá validar o conteúdo dela.
