---
article_id: 11252374374807
category: Materiais - Compras (SIGACOM)
content_hash: 89fdc6fb2737d6a84bbb317e1798f547791ad96fe214dd0bd9116f240cf687c0
fetched_at: '2026-06-28T22:41:21.954480+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Novo parâmetro para
  validar aprovação de alçada com data do sistema inferior a data do documento - MV_DOCAPRV
type: support-article
updated_at: '2022-12-27T19:16:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11252374374807-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-par%C3%A2metro-para-validar-aprova%C3%A7%C3%A3o-de-al%C3%A7ada-com-data-do-sistema-inferior-a-data-do-documento-MV-DOCAPRV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Novo parâmetro para validar aprovação de alçada com data do sistema inferior a data do documento MV\_DOCAPRV.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus compras - Todas as versões  
  
**Solução**

* Para utilizar a funcionalidade, será necessário criar no ambiente o parâmetro MV\_DOCAPRV, onde nele será informado os tipos de documentos que não passarão por essa validação da data base do ambiente Protheus em relação a data do documento

* Para isso, no ambiente do SIGACFG, acesse Base de Dados,->Dicionário-> Base de Dados

![](https://tdn.totvs.com/download/attachments/708098505/image2022-9-8_17-33-37.png?version=1&modificationDate=1662670054397&api=v2)

* Na tela gerada, clique em parâmetros e em seguida em adicionar.

![](https://tdn.totvs.com/download/attachments/708098505/image2022-9-8_17-35-11.png?version=1&modificationDate=1662670054267&api=v2)

* No campo referente ao conteúdo do parâmetro pode-se informar os tipos de alçada que deseja que não passe pelo processo de validação da data.

![](https://tdn.totvs.com/download/attachments/708098505/image2022-9-8_17-45-31.png?version=1&modificationDate=1662670053983&api=v2)![](https://tdn.totvs.com/download/attachments/708098505/image2022-9-8_17-46-31.png?version=1&modificationDate=1662670053827&api=v2)

Os Tipos de Documentos, são os que, na tela de "Aprovação de Documentos" (MATA094), ficam na coluna "Tipo Docto" da imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11253222928663)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11253253469335)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11253280778647)

***Saiba Mais :***

[DT Novo parâmetro para validar aprovação de alçada com data do sistema inferior a data do documento](https://tdn.totvs.com/pages/releaseview.action?pageId=708098505)

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Help DTEMISSUP na rotina de Liberação de Documentos (MATA094)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7920950882071-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Help-DTEMISSUP-na-rotina-de-Libera%C3%A7%C3%A3o-de-Documentos-MATA094-?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
