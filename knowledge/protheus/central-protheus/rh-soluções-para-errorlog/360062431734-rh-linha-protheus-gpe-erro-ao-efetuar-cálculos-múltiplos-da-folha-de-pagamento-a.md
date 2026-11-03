---
article_id: 360062431734
category: RH - Soluções para error.log
content_hash: fa6ee0bf9cd5753d1108559bc32394f24aa8a3090c4bd1cc7b0f829936843ce1
fetched_at: '2026-06-28T22:44:08.844082+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro ao Efetuar Cálculos Múltiplos da folha de
  pagamento: array out of bounds ( 0 of 10 ) on FPROPORC(GPEXMULTV.PRW)'
type: support-article
updated_at: '2025-08-21T18:10:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062431734-RH-Linha-Protheus-GPE-Erro-ao-Efetuar-C%C3%A1lculos-M%C3%BAltiplos-da-folha-de-pagamento-array-out-of-bounds-0-of-10-on-FPROPORC-GPEXMULTV-PRW
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34351353341847)** Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Ao calcular **Folha de Pagamento** através da **rotina Cálculos Múltiplos, em GPEM020A,** gera **error log: *array out of bounds* ( 0 *of* 10 ) *on* FPROPORC(GPEXMULTV.PRW).**  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Causa**Sistema apresenta *error.log* em **cálculos Múltiplos** quando o mnemônico **P\_MULTV** está desativado.  
  
**Solução**Para correção do erro, será necessário atualização do ambiente com o pacote de RH Expedição contínua. Para baixá-lo, [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-MP-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-continua-acumulado-do-modulo-Gest%C3%A3o-de-Pessoal?source=search).  
  
**Saiba mais:**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=585302943>
