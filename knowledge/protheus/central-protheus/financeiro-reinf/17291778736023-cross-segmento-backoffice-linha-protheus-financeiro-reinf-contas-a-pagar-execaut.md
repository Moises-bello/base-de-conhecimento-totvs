---
article_id: 17291778736023
category: Financeiro - Reinf
content_hash: c57ac8c3b62b10c3abd5998f9e8221308a29d6f7de24ac3410b5b4e8ceb0f4e3
fetched_at: '2026-06-28T22:37:51.652886+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - Financeiro REINF - Contas a Pagar
  Execauto FKF e FKG
type: support-article
updated_at: '2026-03-04T17:20:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17291778736023-Cross-Segmento-Backoffice-Linha-Protheus-Financeiro-REINF-Contas-a-Pagar-Execauto-FKF-e-FKG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17291817434775) Tempo aproximado para leitura: **00:03 min**  
  
**Dúvida**

ExecAuto da rotina Contas a Pagar (FINA050) utilizando as tabelas de complemento do título (FKF) e complemento do imposto do título (FKG).

**Ambiente**  
Cross Segmento - TOTVS Backoffice Protheus - Financeiro REINF - Todas as versões.  
  
**Solução**

ExecAuto da rotina **Contas a Pagar** (**FINA050**) utiliza as tabelas de **complemento do título** (**FKF**) e **complemento do imposto do título** (**FKG**).

Exemplo de como alimentar as tabelas novas de **complemento do título** (campo **FKF\_TPSERV**) através da *MsExecauto* da rotina **FINA050** para: **incluir**, **alterar** e **excluir títulos com complementos**:

[FINA050\_ExecAuto\_Complemento\_do\_titulo](https://tdn.totvs.com/display/PROT/FIN0091_CPAG_FINA050_ExecAuto_Complemento_do_titulo)
