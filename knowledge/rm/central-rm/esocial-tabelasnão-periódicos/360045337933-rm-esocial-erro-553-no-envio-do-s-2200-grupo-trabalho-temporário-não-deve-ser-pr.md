---
article_id: 360045337933
category: eSocial - Tabelas/Não Periódicos
content_hash: 1952f31c264f951d615418f080ce38e18825487bdcb035a065fa9c1cbd64db11
fetched_at: '2026-06-28T22:47:10.591734+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RM - eSocial - Erro 553 no envio do S-2200: Grupo Trabalho Temporário não
  deve ser preenchido (v.2.5)'
type: support-article
updated_at: '2021-04-01T19:12:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045337933-RM-eSocial-Erro-553-no-envio-do-S-2200-Grupo-Trabalho-Tempor%C3%A1rio-n%C3%A3o-deve-ser-preenchido-v-2-5
---

**Ocorrência**Ao transmitir o XML do S-2200 de um funcionário cujo registro no RM possui os campos de **Trabalho Temporário** preenchido é apresentado a inconsistência **Código da Ocorrência: 553: Grupo #39;Trabalho Temporário#39; não deve ser preenchido**.  
  
 **Ambiente**RM - eSocial - Todas as Versões  
  
 **Causa**De acordo com o Layout eSocial, informações sobre trabalhadores temporários só devem ser preenchidos quando a Categoria do eSocial for igual a **106 - Trabalhador Temporário - contrato nos termos da Lei 6.019/74**.

![](https://p23.zdusercontent.com/attachment/888110/1no4Y07DhAND74X4jVomrQ2L6?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..ufmQ-mB5GV_pAS6ESH6wmg.ollNsJ1Wk1qpjXmtKIML-AIarceDJvipKLet0eZaWr56ehzefHRaNZgrlQJCK-FInJWHoxj1Sq0ms5v_sCiGEI6jzefcZ_8-TcHOHzr-3Syk2yG2aGGhQKCgzi4tu1FH3WUeCZ8-XupE1viy6Iu3LwrC068du036KmZqDFXdR2qWg1hft5OEeS10WRpQ7u1PMVsjXZtry59JSYnkYc_jUx0LIMSj0A9bed2h4eVM6vgLuVT5QQEtoQ8_DdF86WvurJPEBkqnKBqXi8yBRAYcQ3zs9T_Xl2Yw1F0oqrEtPK4.t6I45PrG4AKhkf_MTcwP8Q)

**Solução**Primeiramente, é necessário validar se no cadastro do funcionário o **Código da Categoria eSocial** está preenchido corretamente. Lembrando que categorias diferentes de **106 - Trabalhador Temporário****não devem** possuir registros de **Trabalho Temporário** preenchidos.

Caso o a categoria do funcionário seja **106 - Trabalhador Temporário**, e o erro ainda sim está sendo apresentado, valide se o XML está sendo gerado com as tags abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061649774/mceclip0.png)
