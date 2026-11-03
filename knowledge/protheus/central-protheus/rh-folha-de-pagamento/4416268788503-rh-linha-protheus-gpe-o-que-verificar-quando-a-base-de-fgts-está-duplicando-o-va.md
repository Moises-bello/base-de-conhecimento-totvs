---
article_id: 4416268788503
category: RH - Folha de Pagamento
content_hash: 1a717ea12312ae781365caaa3f05905ca87d95319a3452f81e4723d7b0e84960
fetched_at: '2026-06-28T22:44:16.050736+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - O que verificar quando a base de FGTS está duplicando
  o valor do salário para funcionário com afastamento 15 dias
type: support-article
updated_at: '2025-05-09T11:40:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416268788503-RH-Linha-Protheus-GPE-O-que-verificar-quando-a-base-de-FGTS-est%C3%A1-duplicando-o-valor-do-sal%C3%A1rio-para-funcion%C3%A1rio-com-afastamento-15-dias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26350894724887) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**O que verificar quando a base de FGTS está duplicando o valor do salário para funcionário com afastamento 15 dias?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**No modulo de Gestão de Pessoal na rotina de cadastro de verbas em **Atualizações > Definições Cálculo > Verbas (GPEA040)**, verificar a verba criada para o calculo de auxilio acidente de trabalho que está amarrada no cadastro do Tipo de Ausência se consta com NÃO para FGTS:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416254665751)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416262257943)

Ajustando a configuração dessa verba gera a base do FGTS de forma correta:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416268614039)

**Obs.:** A verba de auxilio acidente não pode ficar com SIM para FGTS, pois o sistema já considera o salário integral e por ser uma verba que faz parte do salário, por esse motivo valor é duplicado.

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
