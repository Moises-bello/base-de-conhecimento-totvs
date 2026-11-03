---
article_id: 5368399329687
category: RH - Rescisão
content_hash: cba51b476d3897102626dece3b4eeb7bf9c724e804adb104cc9609abfe45c457
fetched_at: '2026-06-28T22:43:53.710891+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Por que rescisão não calcula saldo de salário (id
  0048), mesmo constando em tabela S043 S para saldo de salário e formulas cálculo
  saldo de salário habilitadas em roteiro RES
type: support-article
updated_at: '2025-05-20T19:24:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5368399329687-RH-Linha-Protheus-GPE-Por-que-rescis%C3%A3o-n%C3%A3o-calcula-saldo-de-sal%C3%A1rio-id-0048-mesmo-constando-em-tabela-S043-S-para-saldo-de-sal%C3%A1rio-e-formulas-c%C3%A1lculo-saldo-de-sal%C3%A1rio-habilitadas-em-roteiro-RES
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18529395201431) Tempo aproximado para leitura: **00:00:30 min** **Dúvida**Por que rescisão não calcula saldo de salário (id 0048), mesmo constando em tabela S043 S para saldo de salário e formulas cálculo saldo de salário habilitadas em roteiro RES?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**A rescisão não calcula saldo de salário (id 0048), mesmo constando em tabela S043 S para saldo de salário e formulas cálculo saldo de salário habilitadas em roteiro RES devido o parâmetro MV\_CALCINF = S. O parâmetro MV\_CALCINF deve estar com N para cálculo de saldo de salário em rescisão.

**Parâmetro MV\_CALCINF**

**Acesso em SIGACFG - Cadastros\Parâmetros**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18529395208215)

**Saiba mais**Para adquirir maior conhecimento acesse o *link* abaixo:  
[MP - GPE - Rescisão não gera desconto INSS mesmo quando o id 0048 (provento saldo de salário) possui incidência Sim INSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052167734-MP-GPE-Rescis%C3%A3o-n%C3%A3o-gera-desconto-INSS-mesmo-quando-o-id-0048-provento-saldo-de-sal%C3%A1rio-possui-incid%C3%AAncia-Sim-INSS?source=search)
