---
article_id: 360025751111
category: RH - Cálculo PLR
content_hash: 669ef76044d2f46d048616eefda35ea8246d33d69ee41b53ad76b23dab9f20f4
fetched_at: '2026-06-28T22:43:12.844507+00:00'
product: protheus
section_id: 360010855894
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo do PLR data de Referencia
type: support-article
updated_at: '2025-04-15T13:20:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025751111-RH-Linha-Protheus-GPE-C%C3%A1lculo-do-PLR-data-de-Referencia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24993569306903) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao efetuar o Cálculo do PLR no Protheus, grava as datas de referência nas tabelas **(RGB/SRC)** como 01/01/2018 mesmo que o cálculo tenha sido efetuado em um mês posterior ao mês 01/2018, entenda o que verificar em casos semelhantes.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para o eSocial, DIRF, RAIS e outros sistema será considerado o campo **Dt. Pagto.**   
Somente ira  considerar para o campo **Dt. Ref,**  quando houver dois ou mais lançamentos manuais de PLR (Parcelas) para não perder a referência do desconto do IR.

**![2019-03-22_15_20_23-TOTVS_Servi_os__Microsiga__02.9.0007.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360024532911)**

O evento ocorre quando no cadastro do sindicato existe o preenchimento do **Ano Ref Cál**, desta forma o sistema considera o primeiro dia do ano corrente para realização do cálculo.

**Cadastro do sindicato:**

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360024520832)  
  
**Saiba Mais**

[RH - Cálculo PLR](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010855894-RH-C%C3%A1lculo-PLR)

[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
