---
article_id: 28868089852439
category: Financeiro
content_hash: 5e080fada5a8ac967c815066384663b1ec6a09703da67a1dd564cf02bfa41125
fetched_at: '2026-06-28T22:38:00.838033+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA960 - Como calcular
  valores no campo "RES CTB" - FR4_RESCTB "RES CTB" - FR4_RESCTB
type: support-article
updated_at: '2024-12-30T19:44:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28868089852439-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA960-Como-calcular-valores-no-campo-RES-CTB-FR4-RESCTB-RES-CTB-FR4-RESCTB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28868089824791) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como calcular valores no campo "RES CTB" - FR4\_RESCTB  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução**

Para calcular o valor no campo necessário, é imprescindível configurar a Visão Gerencial no Módulo 34, acessando os seguintes menus: Contabilidade Gerencial > Atualizações > Entidades > Visão Gerencial.

A **Entidade sintética** não possui saldo, sendo assim, para ser preenchido o resultado contábil (**FR4\_RESCTB**) na rotina de apuração **FINA960 irpj/csl lucro real** é necessário que no cadastro da visão gerencial seja configurado o resultado da visão (**CVF\_TOTVIS**) da (s) conta (s) **analítica** igual (SIM) e da entidade superior **sintética** (NÃO)".

Exemplo:   
![Gravar_2024_12_30_14_18_50_489.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/28868089826327)

**Saiba mais**

[Visão gerencial utilizada na rotina de Apuração de IRPJ e CSLL](https://tdn.totvs.com/display/PROT/FIN0103_CPAG_Apuracao_IRPJ_e_CSLL_Linhas_Sinteticas_e_Analiticas)
