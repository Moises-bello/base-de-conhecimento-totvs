---
article_id: 360021479292
category: Materiais - Compras (SIGACOM)
content_hash: 04247f8c21dd1047fa41282f487c15fae1b0d9acec3c7c0fd6713aa794d0f65e
fetched_at: '2026-06-28T22:41:08.964792+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Inconsistência na geração
  de título do Contas a Pagar a partir do MATA103 ao alterar o parâmetro MV_2DUPREF
type: support-article
updated_at: '2022-05-12T21:24:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021479292-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Inconsist%C3%AAncia-na-gera%C3%A7%C3%A3o-de-t%C3%ADtulo-do-Contas-a-Pagar-a-partir-do-MATA103-ao-alterar-o-par%C3%A2metro-MV-2DUPREF
---

**Dúvida**

Inconsistência na geração de título do Contas a Pagar a partir do MATA103 ao alterar o parâmetro MV\_2DUPREF

**Ambiente**  
Protheus – Compras – A partir da versão 12  
  
  
**Solução**

A alteração equivocada do parâmetro MV\_2DUPREF, utilizado para gravar a tabela SE2, pode acarretar em error.log nos processos de geração de título, inclusive por duplicidade de registros por regras inconsistentes.

Por isso foi criada a documentação abaixo com detalhes para que possa ser avaliada a adequação do parâmetro conforme a necessidade do cliente.

***Saiba mais:***

[Alteração MV\_2DUPREF](http://tdn.totvs.com/pages/releaseview.action?pageId=417696345)
