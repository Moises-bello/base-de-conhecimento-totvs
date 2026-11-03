---
article_id: 360013108932
category: Contabilidade Gerencial - Plano de Contas
content_hash: acbdd1aca5ab1e064224bbd94c873a7440b11f4f1245d26541d7265bbf1c5fdb
fetched_at: '2026-06-28T22:40:33.332136+00:00'
product: protheus
section_id: 1500001549022
source: central-protheus
title: MP - SIGATCB - CTBA020/CTBA025 PLANO DE CONTAS  E PLANO REFERENCIAL  FWNOLIST
type: support-article
updated_at: '2021-04-28T15:26:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013108932-MP-SIGATCB-CTBA020-CTBA025-PLANO-DE-CONTAS-E-PLANO-REFERENCIAL-FWNOLIST
---

**Ocorrência**

Ao associar a conta referencial a conta contabil retorna mensagem:

HELP: FWNOLIST  
Problema: Valor atribuído difere da lista de valores válidos (Nat.Conta)  
   
 **Ambiente**

PORTHEUS – Contabilidade gerencial  – A partir da versão 12  
   
 **Causa**

Campos não preenchidos ou preenchidos incorretamente, como Classe Conta (CVN\_CLASSE) no Cadastro da Conta Referencial  em branco, ou campo da Natureza da Conta Referencial (CVN\_NATCTA) com um digito quando deve haver dois dígitos para o código.

Ex: Natureza Conta Referencial

Errado: '1', '2', '3' e '4'

Correto: '01', '02', '03' e '04'

**Solução**

Para solucionar essa ocorrência, Verifique como estão preenchidos os campos

CT1\_NATCTA  
CT1\_NTSPED  
CVN\_NATCTA  
CVN\_CLASSE  
CVD\_NATCTA
