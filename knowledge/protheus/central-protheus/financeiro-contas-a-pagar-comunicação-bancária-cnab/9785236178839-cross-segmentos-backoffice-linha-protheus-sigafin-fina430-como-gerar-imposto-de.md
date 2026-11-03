---
article_id: 9785236178839
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: bca5f679a0a6f64648de54d82122845bad556bf0bf4380b580ceb0fb53de2894
fetched_at: '2026-06-28T22:37:56.239680+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA430 - Como gerar
  imposto de PCC na baixa CNAB
type: support-article
updated_at: '2022-10-26T19:59:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9785236178839-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA430-Como-gerar-imposto-de-PCC-na-baixa-CNAB
---

**Dúvida**Como realizar a geração dos impostos de PCC no momento do retorno do banco via CNAB modelo 2?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12.1.27  
  
**Solução**

Nesses casos em que o imposto é provisionado e não gerado, será necessário realizar o cálculo do valor a ser pago do título **(valor do título - impostos)** antes da geração do arquivo de pagamento ao banco, para que ao se obter a resposta do banco o sistema possa realizar a baixa de forma correta.

Os parâmetros responsáveis por esta melhoria são:

**MV\_CNBIMPG - Para CNAB a Pagar**

**MV\_CNABIMP - Para CNAB a Receber**

Ao ser habilitado, não será mais possível gerar o borderô via rotina de **Borderô de impostos**, independente da carteira, tanto **FINA241 (Borderô de impostos)** quanto **Borderô de Recebimentos de** **Impostos** (**FINA061),** onde será necessário o uso da rotina de **Contas a Pagar** ou **Receber** sendo respectivamente **Borderô de Pagamentos (FINA240)** e **Transferências (FINA060)**.

**Saiba mais**

[CNAB - Disponibilidade da geração dos impostos no momento do retorno do banco para baixa do título](https://tdn.totvs.com/display/public/PROT/FIN0042_CNAB_MV_CNBIMPG_FINA430)

[Implementação da geração do PCC no retorno a pagar do CNAB](https://tdn.totvs.com/display/public/PROT/TRRLB6_DT_PCC_no_retorno_a_pagar_CNAB)

[Geração do PCC no retorno do CNAB a pagar](https://tdn.totvs.com/display/public/PROT/TVHAH7_DT_Retorno_CNAB_a_pagar_com_PCC)

[MV\_CNABIMP - Geração de impostos no processamento do CNAB - Contas a Receber](https://tdn.totvs.com/pages/releaseview.action?pageId=152802224)
