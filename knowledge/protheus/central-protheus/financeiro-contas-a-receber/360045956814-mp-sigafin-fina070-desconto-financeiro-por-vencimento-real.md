---
article_id: 360045956814
category: Financeiro - Contas a Receber
content_hash: 64e137287972915e135f2e82e41a6f061179f9bade889fc5f71b5a45897fc38f
fetched_at: '2026-06-28T22:38:15.031101+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: MP - SIGAFIN - FINA070 - Desconto Financeiro Por Vencimento Real
type: support-article
updated_at: '2021-04-28T15:16:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045956814-MP-SIGAFIN-FINA070-Desconto-Financeiro-Por-Vencimento-Real
---

**Dúvida**Como configurar o sistema para que o desconto financeiro seja pelo vencimento real (próximo dia útil), caso o vencimento seja em algum feriado?  
   
 **Ambiente** Microsiga Protheus – Financeiro - FINA070 – A partir da versão 11.80

**Solução**Para solucionar realize os seguintes passos:  
 1. No configurador (SIGACFG), confira se o feriado esta cadastrado corretamente, como detalhado no material : <https://tdn.totvs.com/display/public/PROT/FIN0041_Cadastrar_Feriado_Tabelas_Genericas_63>  
Exemplo:

![feriado.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360065953213/feriado.PNG)

2. No parâmetro MV\_DTDESCF, altere o conteúdo para "E1\_VENCREA"  ( com as aspas duplas), como mostrado abaixo:

![Desconto_Financeiro_-_Vencicmento_Real.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360065952793/Desconto_Financeiro_-_Vencicmento_Real.PNG)

3. Reinicie o Sistema após a alteração do parâmetro e faça o teste de baixa pela rotina FINA070, com data no próximo dia útil, como mostrado abaixo e veja se o desconto financeiro foi alterado:

![Desconto_Financeiro_-_Vencicmento_Real3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360065972093/Desconto_Financeiro_-_Vencicmento_Real3.PNG)

Segue abaixo link com outros parâmetros da rotina:

<https://tdn.totvs.com/display/public/PROT/Financeiro+-++Protheus+12#Financeiro-Protheus12-Par%C3%A2metros/Configura%C3%A7%C3%B5es>
