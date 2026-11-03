---
article_id: 360015509851
category: Escrita Fiscal - Impostos - ICMS
content_hash: 9268635b3a50a731cc3d8ce74fce1aa5d7247f159370519bcab4c61ea54771b4
fetched_at: '2026-06-28T22:39:24.383246+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como calcular o DIFAL
  na devolução de venda
type: support-article
updated_at: '2021-07-20T14:20:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015509851-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-o-DIFAL-na-devolu%C3%A7%C3%A3o-de-venda
---

**Dúvida**Como calcular o DIFAL na devolução de venda?  
  
 **Ambiente**  
Microsiga Protheus– Livros Fiscais – A partir da versão 11.80  
  
**Solução**Para calcular o DIFAL na devolução de venda configure conforme abaixo:

Cadastro do Cliente   
Insc. Estadual (A1\_INSCR) = Isento ou em branco  
Contribuinte (A1\_CONTRIB) = Não  
Tipo (A1\_TIPO) = Consumidor Final

Cadastro de TES   
Calcula ICMS (F4\_ICM) = Sim  
Calc. Difal (F4\_DIFAL) = Sim  
Calc.Dif.ICM (F4\_COMPL) = Sim
