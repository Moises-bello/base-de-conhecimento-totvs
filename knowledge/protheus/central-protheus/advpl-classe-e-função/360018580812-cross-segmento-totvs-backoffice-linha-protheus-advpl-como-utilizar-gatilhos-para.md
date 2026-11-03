---
article_id: 360018580812
category: ADVPL - Classe e Função
content_hash: b535a45f11a749e243bb219812561bfbfcd15d716efd108f649f56047b5f64b3
fetched_at: '2026-06-28T22:40:14.091181+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL -  Como utilizar
  gatilhos para preenchimento dos campos em rotinas MVC
type: support-article
updated_at: '2022-03-11T13:40:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018580812-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-utilizar-gatilhos-para-preenchimento-dos-campos-em-rotinas-MVC
---

**Dúvida**Como utilizar gatilhos para preenchimento dos campos da tabela do cabeçalho para a tabela da grid em rotinas **MVC**?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL– A partir da versão 11.80  
  
**Solução**

O domínio (X7\_CAMPO) e contra-domínio (X7\_CDOMIN) apontando para o mesmo campo que irá disparar a função.

Para utilizar o gatilho para preenchimento do conteúdo dos campos da tabela do cabeçalho para tabela da **grid** é necessário utilizar as funções de preenchimento do **objeto**, ativando o modelo de dados e os **objetos**. Assim como no exemplo a seguir.

No Configurador > Gatilhos.

| Domínio | Sequencia | Contra Domínio | Regra | Posiciona? |
| --- | --- | --- | --- | --- |
| N1\_DESCRIC | 001 | N1\_DESCRIC | u\_GatSN3() | Não |

E a função ficará:

```
//-------------------------------------------------------------------  
  
/*/{Protheus.doc} GatSN3  
Gatilho do objeto SN3  
@since 02/08/2017  
@version 12.17  
/*/  
//-------------------------------------------------------------------  
  
User Function GatSN3()  
  
Local lRet := .T.  
Local oModel    := FWModelActive()  
Local cDesc     := oModel:GetValue('SN1MASTER','N1_DESCRIC')  
  
oModel:SetValue('SN3DETAIL','N3_HISTOR',cDesc)  
  
Return lRet
```

Outro exemplo na CN9

| Domínio | Sequencia | Contra Domínio | Regra | Posiciona? |
| --- | --- | --- | --- | --- |
| CN9\_CLIENT | 001 | CN9\_CLIENT | u\_GatCN9() | Não |

```
#Include "Protheus.ch"  
  
User Function GatCN9()  
Local lRet := .T.  
Local oModel := FWModelActive()  
Local cDesc := oModel:GetValue('CN9MASTER','CN9_CLIENT')  
  
oModel:SetValue('CNCDETAIL','CNC_CLIENT',cDesc)  
  
Return lRet
```

**Saiba Mais:  
[Como utilizar MVC (Model View Controller)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017512652-MP-ADVPL-Como-utilizar-MVC-Model-View-Controller-)**
