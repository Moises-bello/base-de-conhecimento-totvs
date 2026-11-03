---
article_id: 1500006469141
category: Financeiro - Contas a Receber
content_hash: 17b9728ed0d61841aa06c913d550272788274cc9d3ca98b9215d4373251d48f3
fetched_at: '2026-06-28T22:38:13.864537+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: 'Cross Segmento Protheus - Backoffice Linha Protheus - SIGAFIN - FINR720 -
  Conceito do relatório  '
type: support-article
updated_at: '2021-06-30T00:44:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006469141-Cross-Segmento-Protheus-Backoffice-Linha-Protheus-SIGAFIN-FINR720-Conceito-do-relat%C3%B3rio
---

**Dúvida**Qual é o conceito do relatório FINR720?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINR720 - Todas as versões  
  
**Solução**Toda empresa deveria classificar as **Naturezas** separadamente, isto é, um grupo de **Naturezas** para as entradas (recebimentos) e outra para as saídas (pagamentos). Em toda a implantação recomendamos que os grupos não possuam códigos intercalados entre si. Imagine como se fosse num plano de contas (ativo e passivo). As contas do Ativo não possuem o mesmo código que as contas do Passivo.  
  
**Regime de Competência**  
Reconhece a receita quando ocorre a venda, independente de ter sido paga ou não. O modulo **Financeiro** considera a **data de emissão -> E1\_EMIS1** (pois não há movimentação no **SE5**).  
  
**Regime de Caixa**  
São as datas de recebimento e pagamentos. O modulo **Financeiro** considerará a **data da Baixa ->** **E5\_DATA**.
