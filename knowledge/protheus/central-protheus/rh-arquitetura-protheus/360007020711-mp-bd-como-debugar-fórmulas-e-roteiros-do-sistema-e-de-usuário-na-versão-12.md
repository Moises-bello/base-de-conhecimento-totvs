---
article_id: 360007020711
category: RH - Arquitetura Protheus
content_hash: 911cd1a6af38b512700d5db93ef990cb5feb7ce2aed4fdc7ff665ceb0290db05
fetched_at: '2026-06-28T22:43:03.215384+00:00'
product: protheus
section_id: 206960847
source: central-protheus
title: MP - BD - Como debugar fórmulas e roteiros do sistema e de usuário na versão
  12
type: support-article
updated_at: '2020-12-05T13:00:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007020711-MP-BD-Como-debugar-f%C3%B3rmulas-e-roteiros-do-sistema-e-de-usu%C3%A1rio-na-vers%C3%A3o-12
---

**Dúvida**Como *debugar* **fórmulas** e **roteiros** do sistema e de usuário na versão 12?  
  
**Ambiente**Protheus – Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**Exemplo de **Fórmula** que queremos *debugar*:  
  
![](http://tdn.totvs.com/download/attachments/267811550/image2016-10-21%2012%3A13%3A44.png?version=1&modificationDate=1477059386000&api=v2)  
  
Na versão 12, existe a pasta **rpofrm01** (01 é o código da empresa), dentro da pasta **APO**:  
  
![](http://tdn.totvs.com/download/attachments/267811550/image2016-10-21%2012%3A4%3A20.png?version=1&modificationDate=1477059386000&api=v2)  
  
Nesta pasta, existe a pasta ***source***, onde o sistema guarda os fontes das **fórmulas** padrão - iniciam com s\_ e de usuário - iniciam com u:  
  
![](http://tdn.totvs.com/download/attachments/267811550/image2016-10-21%2012%3A5%3A9.png?version=1&modificationDate=1477059386000&api=v2)  
  
Para *debugar*, basta pegar o fonte correspondente a **fórmula**, colocar no ***Totvs Developer Studio*** e executar a rotina em modo *debug* inserindo os pontos de parada:  
  
**![](http://tdn.totvs.com/download/attachments/267811550/image2016-10-21%2012%3A1%3A44.png?version=1&modificationDate=1477059386000&api=v2)  
  
Saiba Mais**  
Para adquirir informações adicionais, acesse o *link*: [MP - BD0051 - Como debugar fórmulas e roteiros do sistema e de usuário na versão 12](http://tdn.totvs.com/pages/viewpage.action?pageId=267811550)
