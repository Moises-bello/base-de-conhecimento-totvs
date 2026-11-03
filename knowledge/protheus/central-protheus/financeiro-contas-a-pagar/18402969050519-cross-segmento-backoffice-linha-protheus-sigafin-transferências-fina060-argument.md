---
article_id: 18402969050519
category: Financeiro - Contas a Pagar
content_hash: 811ec0d3bc56a9b21ab01161c48f4a1da72ee2cbddf3d9399b4418a09bad6b94
fetched_at: '2026-06-28T22:38:08.351444+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Transferências (FINA060)
  - argument #0 error, expected C->U, function substr on FA060BORDE(FINA060.PRX)'
type: support-article
updated_at: '2023-10-19T17:50:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18402969050519-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Transfer%C3%AAncias-FINA060-argument-0-error-expected-C-U-function-substr-on-FA060BORDE-FINA060-PRX
---

**Ocorrência**

Ao tentar executar a rotina Transferências (FINA060) é apresentado o retorno.

THREAD ERROR ([22952], fernando.melo, UP00N060) 18/10/2023 16:29:54  
argument [#0](https://totvssuporte.zendesk.com/agent/tickets/0) error, expected C->U, function substr on FA060BORDE(FINA060.PRX) 02/08/2023 14:01:01 line : 2164

**Causa**O retorno é apresentado com o recebimento de um conteúdo não esperado para o parãmetro MV\_NATDESC

**Solução**Para solucionar do incidente, é necessário que efetue o procedimento abaixo:  
**No configurador**:  
**1.** Em **Base de Dados / Dicionário / Base de Dados**, selecionar a opção **Parâmetros;**  
**2.** Localizar o parâmetro **MV\_NATDESC;**  
**3.** Selecionar a opção **Editar**;

**4.** X6*CONTEUD(C) :  VAZIO - informar "DESCONT"*

**5. Salvar**
