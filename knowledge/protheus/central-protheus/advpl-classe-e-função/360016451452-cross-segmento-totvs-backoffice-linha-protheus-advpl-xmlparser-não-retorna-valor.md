---
article_id: 360016451452
category: ADVPL - Classe e Função
content_hash: dfb722686409a3f6fbcf1d78871c56308ab2ac5b46e1c4ab5748227b7fbafcd0
fetched_at: '2026-06-28T22:40:18.245977+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - XMLPARSER não retorna
  valores do XML '
type: support-article
updated_at: '2022-01-06T19:13:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016451452-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-XMLPARSER-n%C3%A3o-retorna-valores-do-XML
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:10:00 min  
  
Ocorrência**Cliente deseja efetuar a leitura de um arquivo \*.XML por meio de funções ADVPL, e utilizar a função [XMLParser()](http://tdn.totvs.com/display/tec/XmlParser) não é retornado os nós do XML.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – 11.80  
  
**Causa**Quando efetuada a leitura de um arquivo por meio de outras funções ADVPL, algumas vezes o mesmo retorna com a formatação incorreta, não sendo possível o seu envio para a função [XMLParser()](http://tdn.totvs.com/display/tec/XmlParser).  
  
**Solução**Utilizar a função **[XMLParserFile()](http://tdn.totvs.com/display/tec/XmlParserFile).**  
  
EVIDÊNCIA  
[XMLPARSERFILE.7Z](https://totvssuporte.zendesk.com/attachments/token/ZSFtAojVAFCX6dC4FAlCjQHk8/?name=XMLPARSERFILE.7z)
