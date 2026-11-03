---
article_id: 360052972714
category: Financeiro - Movimentação Bancária
content_hash: 9b98b66e3133908092d1f4d42f963b2bd2b489a56e6b1b2adb5578f175f4a9fb
fetched_at: '2026-06-28T22:38:19.522349+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: MP - SIGAFIN - FINC022 - A coluna "realizado"  irá contemplar baixas que movimentarem
  ou não o saldos bancários
type: support-article
updated_at: '2021-04-28T15:52:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052972714-MP-SIGAFIN-FINC022-A-coluna-realizado-ir%C3%A1-contemplar-baixas-que-movimentarem-ou-n%C3%A3o-o-saldos-banc%C3%A1rios
---

**Dúvida**A Coluna "realizado" irá contemplar somente as baixas que movimentaram saldos bancários?  
   
 **Ambiente**Microsiga Protheus – Financeiro – FINC022 – A partir da versão 11.80

**Solução**Referente as linhas das naturezas, não irão contemplar somente na coluna "**realizado**" as baixas que movimentaram saldo bancário. Contemplam também as baixas que não movimentaram saldos bancários.  
  
A rotina **FINC022** trata exatamente os saldos das naturezas, e não saldos bancários.  
  
**Exemplo:**  
1º - Baixar de um título por **DACAO**  
2º - Baixar por compensação e compensação entre carteiras  
  
**Saiba mais:**<https://tdn.totvs.com/display/public/PROT/FIN0007_CREL_diferencas_entre_FINC021_e_FINC022>

<https://tdn.totvs.com/display/public/PROT/FINC022+Fluxo+Por+Natureza#FINC022FluxoPorNatureza-05.OUTRASINFORMA%C3%87%C3%95ES>
