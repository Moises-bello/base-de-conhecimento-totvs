---
article_id: 360050521854
category: RH - Folha de Pagamento
content_hash: 66a9240be8e6269bb5158c834939590bf1ebee085c3eda4e6523fc40b34358e7
fetched_at: '2026-06-28T22:44:17.150078+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: 'RH - Linha Protheus - GPE - Mnemônico P_CATINSSF '
type: support-article
updated_at: '2025-06-16T19:42:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050521854-RH-Linha-Protheus-GPE-Mnem%C3%B4nico-P-CATINSSF
---

**Dúvida**Mnemônico P\_CATINSSF para dizer qual categoria e-social de freteiro irá descontar o INSS da base do IR.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

Criado mnemônico **P\_CATINSSF** para dizer qual categoria e-social de freteiro irá descontar o INSS da base do IR.

O valor padrão do mnemônico é "711/712" com isso o sistema permanece descontando o INSS, caso não queira descontar o INSS de determinada categoria deve se retirar ela do mnemônico.

O mnemônico *P\_LINSSIR foi descontinuado*.

**Exemplos**:

As categorias contidas nesse mnemônico irão deduzir INSS do calculo de IR

![](https://tdn.totvs.com/download/attachments/546680179/image2020-5-28_12-47-8.png?version=1&modificationDate=1590680828543&api=v2)

Dessa forma só a categoria 712 ira descontar o INSS do calculo do IR

![](https://tdn.totvs.com/download/attachments/546680179/image2020-5-28_12-46-51.png?version=1&modificationDate=1590680811660&api=v2)

Dessa forma nenhuma categoria ira descontar o INSS do calculo do IR

![](https://tdn.totvs.com/download/attachments/546680179/image2020-5-28_12-46-18.png?version=1&modificationDate=1590680778707&api=v2)
