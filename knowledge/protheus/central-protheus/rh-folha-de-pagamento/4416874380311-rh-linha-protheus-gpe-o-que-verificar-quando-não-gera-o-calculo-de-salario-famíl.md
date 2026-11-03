---
article_id: 4416874380311
category: RH - Folha de Pagamento
content_hash: 7ed5c89bf8a90d151ef40bf4cf3488395c616163a32a3176ce76ebbd9de004cf
fetched_at: '2026-06-28T22:44:16.065338+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - O que verificar quando não gera o calculo de salario
  família para funcionário afastado mesmo quando o tipo de ausência está configurado
  para pagar
type: support-article
updated_at: '2025-05-05T18:44:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416874380311-RH-Linha-Protheus-GPE-O-que-verificar-quando-n%C3%A3o-gera-o-calculo-de-salario-fam%C3%ADlia-para-funcion%C3%A1rio-afastado-mesmo-quando-o-tipo-de-aus%C3%AAncia-est%C3%A1-configurado-para-pagar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26355954162455) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**O que verificar quando não gera o calculo de salario família para funcionário afastado mesmo quando o tipo de ausência está configurado para pagar?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**No modulo de Gestão de Pessoal na rotina de cadastro de verbas em **Atualizações -> Definições Cálculo -> Verbas**, a verba de afastamento que consta na folha deve ser configurada na aba Incidências com NÃO para salario família. 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416879775127)

Para o pagamento de salario família o sistema valida o salario base do funcionário que consta no cadastro, e caso conste mais alguma verba com "SIM" para salario família será somado junto ao salário. Assim podendo ultrapassar o valor do teto do salário família, e por esse motivo não será considerado o pagamento para o funcionário.

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
