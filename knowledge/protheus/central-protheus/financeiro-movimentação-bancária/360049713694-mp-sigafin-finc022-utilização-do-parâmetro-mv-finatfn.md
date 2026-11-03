---
article_id: 360049713694
category: Financeiro - Movimentação Bancária
content_hash: 8c35c8f15338ba40fff97066aabfcea47cf9c6daf7b7b0443b309230ff8c8b05
fetched_at: '2026-06-28T22:38:19.525293+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: MP - SIGAFIN - FINC022 - Utilização do parâmetro MV_FINATFN
type: support-article
updated_at: '2021-04-28T15:52:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049713694-MP-SIGAFIN-FINC022-Utiliza%C3%A7%C3%A3o-do-par%C3%A2metro-MV-FINATFN
---

**Dúvida**  
Qual a finalidade do parâmetro **MV\_FINATFN**?  
  
**Ambiente**Microsiga Protheus – Financeiro – A partir da versão 11.80  
  
**Solução**A finalidade do parâmetro **MV\_FINATFN** é para demonstrar o fluxo de caixa em tempo real, caso esteja preenchido com o conteúdo = 1 (*OnLine*).   
Caso o parâmetro **MV\_FINATFN** esteja preenchido com o conteúdo = 2, o fluxo de caixa não será demonstrado em tempo real, sendo necessário utilizar a rotina **FINA800**.**MV\_FINATFN**("1" = **Fluxo Caixa *On-Line***,"2" = **Fluxo Caixa** ***Off-Line**(sem aspas duplas))*

**Saiba Mais  
Lentidão na preparação do Documento de Saída devido a tabela FJV (Movimento Analitico P/Natureza)  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036448814>FINC022 - Fluxo por Natureza****<https://tdn.totvs.com/display/public/PROT/FINC022+Fluxo+Por+Natureza>**
