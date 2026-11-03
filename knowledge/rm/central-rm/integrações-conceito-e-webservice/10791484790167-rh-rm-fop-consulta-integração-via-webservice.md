---
article_id: 10791484790167
category: Integrações - Conceito e WebService
content_hash: 88e806b2f13311c4a652cc14921761dfd88cc151a0a2cb02a08ce4c966253872
fetched_at: '2026-06-28T22:46:44.922765+00:00'
product: rm
section_id: 1500000834721
source: central-rm
title: RH - RM - FOP - Consulta integração via Webservice
type: support-article
updated_at: '2025-02-03T16:11:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10791484790167-RH-RM-FOP-Consulta-integra%C3%A7%C3%A3o-via-Webservice
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:20 min****Dúvida**Como realizar a consulta de integração via Webservice?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**

A Adaptação do DATASERVER **FopLancExternoData** para permitir inclusão/edição de dados, possibilitando inclusões, exclusões e edições externamente via webservice e permitindo também segurança via **Perfil de acesso** do sistema.

Foi implementada a permissão para a inclusão/ edição e Exclusão de eventos utilizando o DATASERVER **FopLancExternoData** via webservice.

E para melhor visualização da integração dos eventos importados foi criado a Origem de Evento 7  **Sistemas Externos**

![](https://tdn.totvs.com/download/attachments/484689756/image2019-4-16_13-3-2.png?version=1&modificationDate=1555430583043&api=v2&effects=drop-shadow)

Para o lançamento dos eventos importados via webservice em folha, deverá utilizar o tipo de lançamento conforme abaixo:

![image2020-5-20_10-41-23.png](https://tdn.totvs.com/download/attachments/484689756/image2020-5-20_10-41-23.png?version=1&modificationDate=1589982084237&api=v2)

Para exemplo de utilização e formato do XML, acessar o link: <https://api.totvs.com.br/legado/devrm/bo_rm/FopLancExternoData.html?Objeto=FopLancExternoData>

**Saiba mais**  
[Consulta integração via Webservice](https://tdn.totvs.com/pages/releaseview.action?pageId=484689756)
