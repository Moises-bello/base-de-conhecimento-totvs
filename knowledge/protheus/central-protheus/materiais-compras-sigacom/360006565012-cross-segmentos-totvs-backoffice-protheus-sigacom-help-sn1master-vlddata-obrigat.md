---
article_id: 360006565012
category: Materiais - Compras (SIGACOM)
content_hash: d744651db4e9761a884edc5901029c6df2037a95fae0027c5d0834f66efa4d13
fetched_at: '2026-06-28T22:41:07.387006+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM -  HELP SN1MASTER  VLDDATA_OBRIGAT
  N3_XXXX OU N1_XXXX na nota de entrada com ativo fixo
type: support-article
updated_at: '2022-05-16T22:04:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006565012-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-HELP-SN1MASTER-VLDDATA-OBRIGAT-N3-XXXX-OU-N1-XXXX-na-nota-de-entrada-com-ativo-fixo
---

**Dúvida**

Como resolver o help SN1MASTER VLDDATA\_OBRIGAT N3\_XXXX OU N1\_XXXX no momento de incluir a nota de entrada com ativo fixo?

**Ambiente**

Protheus - Compras - à partir do P12.17

**Solução**

Na integração com o módulo de Ativo Fixo, o módulo de Compras não possui as informações para preenchimento de todos os campos do Ativo. Quando um dos campos que não são preenchidos pelo Compras for obrigatório, será exibida a mensagem de alerta.  
  
Na versão 11, não existia esta validação, causando inconsistência no Ativo Fixo, pois vários campos obrigatórios ficavam em branco. Por este motivo, sugerimos desmarcar a obrigatoriedade do campo N3\_XXXX no dicionário de dados para correta integração.  
  
Obs.: Nos casos que não é possível desativar a obrigatoriedade, poderá ser configurado um Inicializador Padrão nos campos que precisam ser obrigatórios ou então utilizar o ponto de entrada **ATFA006102** - Gravação do Ativo Fixo para que estes campos sejam preenchidos.

***Saiba Mais :***

[Ponto de Entrada ATFA006102 - Gravação do Ativo Fixo](http://tdn.totvs.com/pages/releaseview.action?pageId=6085761%20)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
