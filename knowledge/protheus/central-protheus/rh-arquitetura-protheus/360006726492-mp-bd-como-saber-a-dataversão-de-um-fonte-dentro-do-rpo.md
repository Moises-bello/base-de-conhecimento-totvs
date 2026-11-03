---
article_id: 360006726492
category: RH - Arquitetura Protheus
content_hash: 8ef7aec2754746b9aa020b6661ef09c1c7f0fdab7f99eba702b3122f97c96e66
fetched_at: '2026-06-28T22:43:03.234581+00:00'
product: protheus
section_id: 206960847
source: central-protheus
title: MP - BD - Como saber a data/versão de um fonte dentro do RPO
type: support-article
updated_at: '2020-12-05T13:05:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006726492-MP-BD-Como-saber-a-data-vers%C3%A3o-de-um-fonte-dentro-do-RPO
---

**Dúvida**Como saber a versão de uma função dentro do RPO?  
  
**Ambiente**Protheus – Gestão de Pessoal – A partir da versão 11.80  
  
**Solução**Acesse o ***TotvsdevStudio*** - **Visualizar** - **Inspetor de Objetos:**![](http://tdn.totvs.com/download/attachments/269554327/image2016-12-14%2016%3A30%3A52.png?version=1&modificationDate=1481740317000&api=v2)![](http://tdn.totvs.com/download/attachments/269554327/image2016-12-14%2016%3A34%3A27.png?version=1&modificationDate=1481740532000&api=v2)  
  
Ou acesse***TOTVS Developer Studio,*** clicar no servidor que foi cadastrado, conforme a base de conhecimento: <http://tdn.totvs.com/x/aOFUE>   
  
![](http://tdn.totvs.com/download/attachments/269554327/image2017-6-20%209%3A11%3A29.png?version=1&modificationDate=1497960690000&api=v2)  
  
Acesse o **inspetor de objetos:**![](http://tdn.totvs.com/download/attachments/269554327/image2017-6-20%209%3A12%3A3.png?version=1&modificationDate=1497960725000&api=v2)![](http://tdn.totvs.com/download/attachments/269554327/image2017-6-20%209%3A12%3A34.png?version=1&modificationDate=1497960755000&api=v2)  
  
Acesse **Gestão de Pessoal/Atualizações/Cadastros/Lançamento Padrão** na aba **Entidades:**  
![](http://tdn.totvs.com/download/attachments/269554327/image2016-12-14%2016%3A35%3A9.png?version=1&modificationDate=1481740574000&api=v2)  
  
Digite o seguinte comando: *alert*(getapoinfo("gpexini.prx")[4])

**Observação:** No lugar de **gpexini.prx** informe o nome da função que deseja consultar. Depois, dê *enter* no campo para que data da função seja apresentada.  
  
![](http://tdn.totvs.com/download/attachments/269554327/image2016-12-14%2016%3A36%3A44.png?version=1&modificationDate=1481740668000&api=v2)  
  
**Saiba mais**  
Para adquirir informações adicionais, acesse o *link:*[MP - BD0057 - Como saber a versão de uma função dentro do RPO?](http://tdn.totvs.com/pages/viewpage.action?pageId=269554327)
