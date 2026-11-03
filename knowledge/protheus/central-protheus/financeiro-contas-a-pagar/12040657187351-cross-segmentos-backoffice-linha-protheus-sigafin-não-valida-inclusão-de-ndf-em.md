---
article_id: 12040657187351
category: Financeiro - Contas a Pagar
content_hash: 5a2b68a498736e890bb8831f0c160dbd584ef3e2f0323e46eb2c0f9325f3131b
fetched_at: '2026-06-28T22:38:09.794643+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Não valida inclusão
  de NDF em borderô
type: support-article
updated_at: '2023-01-30T20:22:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12040657187351-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-N%C3%A3o-valida-inclus%C3%A3o-de-NDF-em-border%C3%B4
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, as rotinas **FINA240/FINA241** não está permitindo realizar a inclusão de um tipo NDF no borderô  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**

A rotina **Manutenção de Borderôs (FINA590), Borderô Pagamentos (FINA240) ou Borderô com Impostos (FINA241),** não permiti a inclusão de títulos de crédito junto ao fornecedor **(NDF)** em um borderô.

**Solução**Caso deseje enviar ao banco a **NDF** deve substitui-la por um tipo válido, exemplo a utilização de **Faturas a** **Pagar** (**FINA290**) gerando um **NF** e incluindo o Borderô.

**Saiba mais**  
[DSERFINP-29320 DT FINA590 - Não valida inclusão de NDF em borderô](https://tdn.totvs.com/pages/releaseview.action?pageId=539528513)  
[Borderô Pagamentos - FINA240 - Financeiro - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=236605212)  
[Borderô de Impostos (FINA241 - SIGAFIN)](https://tdn.totvs.com/pages/viewpage.action?pageId=312165366)
