---
article_id: 360048421613
category: Escrita Fiscal - Impostos - ICMS
content_hash: 9789b8f476d03da4049182ef0d382c02074bb86664520b448e0ae8e448d5c88c
fetched_at: '2026-06-28T22:39:23.962768+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Cálculo do Difal
  (EC 87/2015) para cliente Não Contribuinte e geração da guia de recolhimento na
  emissão da nota de saída.
type: support-article
updated_at: '2024-01-18T14:02:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048421613-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%A1lculo-do-Difal-EC-87-2015-para-cliente-N%C3%A3o-Contribuinte-e-gera%C3%A7%C3%A3o-da-guia-de-recolhimento-na-emiss%C3%A3o-da-nota-de-sa%C3%ADda
---

**Dúvida**Como calcular Difal (EC 87/2015) para cliente não contribuinte e gerar a guia de recolhimento na emissão da nota?  
  
**Ambiente**Protheus - Todas as versões  
  
  
**Solução**

Para que seja realizado o cálculo de diferencial de alíquota conforme a EC 87/2015 para cliente consumidor final não contribuinte e gerar a guia de recolhimento no momento da emissão da nota, será  necessário efetuar as configurações conforme detalhado abaixo:

Tes:  
Calc. ICMS (F4\_ICM) = Sim  
L. Fiscal ICMS (F4\_LFICM) = Tributado  
Calc. Dif. ICM (F4\_COMPL) = Sim  
Calc. Difal (F4\_DIFAL) = Sim

Cliente:  
Tipo (A1\_TIPO) = F- Consumidor Final  
Ins. Estadual (A1\_INSCR) = ISENTO  
Contribuinte (A1\_CONTRIB) = Não

MV\_RECST?? (sendo que "??" corresponde a UF do estado de destino, por exemplo MV\_RECSTSP).  
Esse parâmetro deverá ser preenchido com o código e o número da loja do fornecedor.  
Efetue o cadastro de um fornecedor (rotina MATA020) para que seja incluído no parâmetro, por exemplo:

Codigo (A2\_COD) = 12345  
Loja (A2\_LOJA) = 01

O parâmetro MV\_RECST?? deverá ser preenchido com 12345;01

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028698432-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-gerar-o-t%C3%ADtulo-do-DIFAL-ou-ICMS-ST-no-Financeiro-contas-a-pagar-por-opera%C3%A7%C3%A3o->

No parâmetro MV\_SUBTRIB não poderá constar a UF e inscrição estadual do estado de destino.  
Caso esse parâmetro esteja preenchido o recolhimento do Difal será na apuração do ICMS no final do período.

Ao preparar o documento de saída configure as perguntas abaixo:  
Gera Guia ICM Compl. UF Dest.? = Sim  
Gera Guia Fecp UF Destino? Sim (quando houver a necessidade de gerar a guia do Fecp)

Boletim - Difal - Cliente Não Contribuinte:

<https://tdn.totvs.com/pages/releaseview.action?pageId=699815598>
