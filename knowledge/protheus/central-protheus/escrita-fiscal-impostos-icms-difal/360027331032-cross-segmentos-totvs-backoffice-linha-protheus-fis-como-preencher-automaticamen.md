---
article_id: 360027331032
category: Escrita Fiscal - Impostos - ICMS - Difal
content_hash: 01152d168b9875d98755a0dd8497e496006ee6572af6f63815d3343b6763093b
fetched_at: '2026-06-28T22:39:19.292298+00:00'
product: protheus
section_id: 1500001549902
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como preencher automaticamente
  o campo  Código da Obrigação (F6_COBREC)?
type: support-article
updated_at: '2025-07-17T14:05:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027331032-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-preencher-automaticamente-o-campo-C%C3%B3digo-da-Obriga%C3%A7%C3%A3o-F6-COBREC
---

**Dúvida**

Como preencher automaticamente o campo F6\_COBREC?  
  
**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

O preenchimento automaticamente do campo F6\_COBREC é realizado somente via ponto de entrada SPCOBREC.

Realizada inclusão de ponto de entrada para alterar campo F6\_COBREC de forma automática no momento do faturamento de notas com imposto de ICMS ST ou DIFAL.

Para utilização do ponto de entrada é necessário habilitar parâmetro MV\_GNRENF

Exemplo:

#include '[protheus.ch](http://protheus.ch/)'  
#include '[parmtype.ch](http://parmtype.ch/)'

user function SPCOBREC()  
/\*   
Paramixb[1] => Tipo GNRE  
Paramixb[2] => ESTADO da GNRE  
\*/

Local cTipoImp := Paramixb[1] // Tipo de Imposto (3 - ICMS ST ou B - Difal e Fecp de Difal)  
Local cEstado := Paramixb[2] // Estado da GNRE  
Local cCod := "" // Codigo a ser gravado no campo F6\_COBREC

If cTipoImp == "B"  
cCod := "000"  
Else   
cCod := "999"   
EndIf

Documentação completa

<https://tdn.totvs.com/pages/releaseview.action?pageId=655881734>
