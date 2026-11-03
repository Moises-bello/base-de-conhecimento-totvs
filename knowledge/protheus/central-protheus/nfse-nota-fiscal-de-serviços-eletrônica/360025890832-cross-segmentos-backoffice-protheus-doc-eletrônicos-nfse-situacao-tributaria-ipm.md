---
article_id: 360025890832
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: fe272de55dbc66aff19ef83a80a23db601988c4d39233e375fcbebd198db4bf9
fetched_at: '2026-06-28T22:39:58.523303+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Situacao
  Tributaria IPM
type: support-article
updated_at: '2026-03-17T17:37:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025890832-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Situacao-Tributaria-IPM
---

**Dúvida**  
Como gerar a tag <situacao\_tributaria> para prefeituras com provedor IPM?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - Todas as versões  
  
**Solução**

Situação e regra de campos para geração da tag:  
  
**Situação 0 - Tributada Integralmente:** o valor do imposto será lançado para o emissor da nota.  
Campos Protheus: F4\_ISSST=1 ou F4\_ISSST=2 e A1\_RECISS ou C5\_RECISS=2 e A1\_TPESSOA<> 4  
  
**Situação 1 - Tributada Integralmente com ISSRF:** o valor do imposto não será lançado, pois será recolhido pelo tomador, caso seja órgão público municipal.  
Campos Protheus: F4\_ISSST=1 ou F4\_ISSST=2, A1\_RECISS ou C5\_RECISS=1 e A1\_TPESSOA=4  
  
**Situação 2 - Tributada Integralmente e sujeita à Substituição Tributária:** o valor do imposto não será lançado, pois será recolhido pelo tomador (substituto tributário), caso não seja um órgão público municipal.  
Campos Protheus: F4\_ISSST=2, A1\_RECISS ou C5\_RECISS=1 e A1\_TPESSOA <> 4  
  
**Situação 3- Tributada com redução da base de cálculo.**  
Campos Protheus: C6\_ABATISS e/ou C6\_ABATMAT <> de vazio e F4\_ISSST=1  
  
**Situação 4 - Tributada com redução da base de cálculo com ISSRF.**  
Campos Protheus: F4\_ISSST=2, A1\_TPESSOA=4, C6\_ABATISS e/ou C6\_ABATMAT <> de vazio.  
  
**Situação 5 - Tributada com redução da base de cálculo e sujeita à Substituição Tributária.**  
Campos Protheus: F4\_ISSST=2, A1\_TPESSOA <> 4, C6\_ABATISS e/ou C6\_ABATMAT <> de vazio.  
  
**Situação 6- Isenta:** não irá gerar valor de imposto, pois o prestador é isento.  
Campos Protheus: F4\_ISSST=3  
  
**Situação 7 - Imune:** não irá gerar valor do imposto, pois o prestador é imune.  
Campos Protheus: F4\_ISSST=4

Em todas as situações, o campo **A1\_TPESSOA** deve ser diferente de vazio.  
  
  
**Campo A1\_TPESSOA:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27408654803735)

[Manual integração webservice IPM](https://www.nfs-e.net/include/download.php?id=manual_eletron)  
  
**Importante:** Caso esteja usando o configurador de tributos, o campo F4\_NATOPNF deve ser usado no lugar do F4\_ISSST.
