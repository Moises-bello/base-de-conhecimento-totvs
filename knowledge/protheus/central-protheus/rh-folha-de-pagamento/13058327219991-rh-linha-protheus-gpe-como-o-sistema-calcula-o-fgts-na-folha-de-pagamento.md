---
article_id: 13058327219991
category: RH - Folha de Pagamento
content_hash: f6382dc2681f6f5223d941afd29165c535af562c6130dec3d23dd0121366c0d1
fetched_at: '2026-06-28T22:44:13.585205+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como o sistema calcula o FGTS na folha de pagamento
type: support-article
updated_at: '2024-09-09T19:20:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13058327219991-RH-Linha-Protheus-GPE-Como-o-sistema-calcula-o-FGTS-na-folha-de-pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26236836092567) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como o sistema calcula o FGTS na folha de pagamento?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Para o cálculo do FGTS, o sistema considera o cadastro da **Tabela S037** em junção com o cadastro do Funcionário.

Na **Tabela S037**, pelo caminho **>Atualizações >Definições cálculos >Manutenção Tabelas**, o sistema valida a coluna %FGTS, onde deve existir cadastro tanto para o tipo de contrato 1-Indeterminado quanto para o 2-Determinado, pois o sistema valida no cadastro do funcionário o tipo de contrato dele para o cálculo do FGTS:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13057946860695)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13058010994327)

Outra validação que o sistema também faz no cadastro do funcionário, é no campo **% Dep. FGTS**, se o campo estiver preenchido com percentual, esse percentual que será considerado no cálculo de FGTS, não o percentual preenchido na Tabela S037:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13058230322327)

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
