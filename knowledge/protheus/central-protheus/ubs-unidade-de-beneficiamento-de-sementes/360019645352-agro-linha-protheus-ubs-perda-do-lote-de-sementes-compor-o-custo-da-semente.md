---
article_id: 360019645352
category: UBS - Unidade de Beneficiamento de Sementes
content_hash: 878eedbabfce67dba9bfbec165b8338cc7aba4e018f28764a5a8b083c0248ef5
fetched_at: '2026-06-28T22:45:34.821129+00:00'
product: protheus
section_id: 360005696194
source: central-protheus
title: Agro - Linha Protheus - UBS - Perda do lote de sementes compor o custo da semente
type: support-article
updated_at: '2025-06-20T15:39:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019645352-Agro-Linha-Protheus-UBS-Perda-do-lote-de-sementes-compor-o-custo-da-semente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22312681041303) Tempo aproximado para leitura: **00:00:30 min  
  
Dúvida**Na rotina **AGRA840** **-** **Lote de Sementes**quando é registrada uma quantidade de perda para algum dos produtos da estrutura do lote essa quantidade não é composta no custo da semente, mas é necessário que isso seja feito. Como fazer para que a quantidade de perda faça parte do custo da semente?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - UBS - Unidade de Beneficiamento de Sementes - Versão 12  
  
**Solução**Para que a perda registrada para algum produto componha o custo da semente é necessário:

**1.** Acesse a rotina **MATA685 - Apontar Perda**, acionar os parâmetros por meio da **tecla F12** e informar **Sim** na pergunta **Requisita Produto de Origem**;

**2.** Acione a opção todas as perdas que forem apontadas no **Lote de Sementes** farão parte do custo da semente;

**3.** Registre o lote e aponte a perda, para conferir se o registro referente ao custo foi executado corretamente, é necessário acessar a tabela **SD3** por meio do **APSDU** e analisar os registros.
