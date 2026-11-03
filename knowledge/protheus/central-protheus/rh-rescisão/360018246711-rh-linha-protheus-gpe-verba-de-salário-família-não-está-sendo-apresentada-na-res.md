---
article_id: 360018246711
category: RH - Rescisão
content_hash: 69cd0b82c2e59049afb16fe39cd3a618d8871f8e01a3ad6c92bb601979913494
fetched_at: '2026-06-28T22:43:50.948349+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Verba de salário família não está sendo apresentada
  na rescisão
type: support-article
updated_at: '2025-07-25T13:28:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018246711-RH-Linha-Protheus-GPE-Verba-de-sal%C3%A1rio-fam%C3%ADlia-n%C3%A3o-est%C3%A1-sendo-apresentada-na-rescis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33712484347927) Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Funcionária possui dependente para salário família, porém não está saindo valor para pagamento na rescisão.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) GPE Gestão de Pessoal - A partir da versão 11.80  
  
**Causa**Esse incidente ocorre, pois existem verbas na SRV que estão com **SIM** para Salário Família erroneamente.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Possuir dependente com idade até **14 anos**;  
2. Receber remuneração até o limite estabelecido na **tabela S003**;  
3. Possuir verba para pagamento do salário família com **ID 0034**;  
4. O Protheus sempre irá utilizar o valor do **RA\_SALARIO** para a base de calculo, independente da quantidade de dias de saldo da rescisão.

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
