---
article_id: 360028620892
category: Financeiro - Contas a Pagar
content_hash: a69d016e9d694c030d9f2689bf293bc682f89e21fb3e252c0e779420e6ab52fb
fetched_at: '2026-06-28T22:38:09.933140+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'MP - SIGAFIN - FISA001 - Tabela de alimentação EFD Contribuições '
type: support-article
updated_at: '2021-04-28T15:18:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028620892-MP-SIGAFIN-FISA001-Tabela-de-alimenta%C3%A7%C3%A3o-EFD-Contribui%C3%A7%C3%B5es
---

**Dúvida**  
Qual a tabela de alimentação EFD Contribuições?  
   
 **Ambiente**  
Microsiga Protheus – Financeiro – A partir da versão 12.1.17  
  
**Solução**A tabela **CL2** somente é gravada quando a apuração da **EFD** Contribuições é processada no **regime de apuração** **competência**, quando **regime de apuração** é **caixa** realmente a tabela **CL2** não será gerada, já que no **regime de apuração caixa** não é gerado registro **F100** e sim o registro **F500** que possui outras regras, validações e por este motivo gravamos em tabelas distintas:   
**Regime de competência** gravamos na tabela **CL2**, **regime de caixa** gravamos a **CL1**.
