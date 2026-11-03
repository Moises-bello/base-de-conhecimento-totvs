---
article_id: 360025778071
category: Financeiro - Comissão
content_hash: 8fcdf47403594f61d41dcbae6ceef227a95215c7159b4136054ca56c7a93ee98
fetched_at: '2026-06-28T22:37:50.700841+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - É gerado a comissão
  quando é feito a transferência de títulos entre filiais
type: support-article
updated_at: '2026-02-10T17:04:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025778071-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-%C3%89-gerado-a-comiss%C3%A3o-quando-%C3%A9-feito-a-transfer%C3%AAncia-de-t%C3%ADtulos-entre-filiais
---

**Dúvida**  
É gerado a comissão quando é feito a transferência de títulos entre filiais  
  
**Ambiente**  
Microsiga Protheus  – Financeiro – A partir da versão 12  
  
**Solução**

Conforme a **ISSUE DSERFINR-17111**, foi implementada uma validação nos fontes **FINA440**, **FINA040**, **FINA620** e **FINA630**, com o objetivo de **desconsiderar a comissão** nos casos em que o título tenha como origem a rotina **FINA630 (Aprovação/Rejeição da Transferência de Títulos)**.

**Exemplo de comportamento:**

* Um título a receber é gerado por meio da rotina **FINA040**, na **filial 01**, com comissão de **100% na emissão**;
* Após a inclusão do título, a comissão é registrada na **filial 01**;
* É realizada uma **transferência de títulos entre filiais** utilizando a rotina **FINA620**;
* Na **filial 02**, acessa-se a rotina **FINA630** para **aprovar a transferência** do título da filial 01 para a filial 02;
* Neste caso, a **comissão permanece na filial de origem (filial 01)** e **não é transferida** juntamente com o título para a filial 02.
