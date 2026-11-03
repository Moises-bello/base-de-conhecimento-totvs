---
article_id: 360018671211
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 41f411e3b1e585fe33aa859aea38df2d8e99644931af2743ce0e890c150214fb
fetched_at: '2026-06-28T22:41:48.301772+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF  - ATFA012 Utilização
  de gatilhos para preenchimento dos campos do objeto da SN3 na rotina
type: support-article
updated_at: '2023-11-30T15:30:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018671211-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-Utiliza%C3%A7%C3%A3o-de-gatilhos-para-preenchimento-dos-campos-do-objeto-da-SN3-na-rotina
---

**Dúvida**Como utilizar gatilhos para preenchimento dos campos do objeto da SN3 na rotina ATFA012?

**Ambiente**Protheus – Ativo Fixo – A partir da versão 11.80  
  
  
**Solução**

Para utilizar o gatilho para preenchimento do conteúdo dos campos da tabela SN3 é necessário utilizar as funções de preenchimento do objeto, ativando o modelo de dados e os objetos. Assim como no exemplo a seguir.

No Configurador > Gatilhos.

| Domínio | Sequencia | Contra Domínio | Regra | Posiciona? |
| --- | --- | --- | --- | --- |
| N3\_HISTOR | 001 | N3\_HISTOR | u\_GatSN3() | Não |

E a função ficará:

 //-------------------------------------------------------------------

/\*/{Protheus.doc} GatSN3

Gatilho do objeto SN3

  

@since 02/08/2017

@version 12.17

/\*/

//-------------------------------------------------------------------

User Function GatSN3()

Local lRet := .T.

Local oModel    := FWModelActive()

Local cDesc     := oModel:GetValue('SN1MASTER','N1\_DESCRIC')

  

oModel:SetValue('SN3DETAIL','N3\_HISTOR',cDesc)

  

Return lRet
