---
article_id: 37095622737431
category: SIGAACD - Automação e Coleta de Dados
content_hash: b1aca892571fca0d763b3db693625471e9e403024f50b30d78b950ab3961eee6
fetched_at: '2026-06-28T22:39:13.930605+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento – Backoffice (Linha Protheus) - SIGAACD- Mestre de inventário
  automático - ACDA030
type: support-article
updated_at: '2025-12-18T15:21:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37095622737431-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Mestre-de-invent%C3%A1rio-autom%C3%A1tico-ACDA030
---

No ambiente TOTVS Estoque, para gerar automaticamente um mestre de inventário para vários produtos, deve-se acessar a rotina ACDA030 e selecionar Outras Ações - Automático. Essa função permite excluir mestres, gerar e excluir lançamentos automaticamente, configurando um intervalo de produtos. Produtos bloqueados não terão mestre gerado.

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37095887005079) Tempo aproximado para leitura: **01:00 min**

**Veja um exemplo simulando o processo:**

**Dúvida**  
Como gerar mestre de inventário de forma automática?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque - Todas as versões  
  
**Solução**  
Para gerar automaticamente um mestre de inventário para mais de um produto, na rotina ACDA030 ir em:

Outras Ações - Automático.

Com essa opção é possível Excluir Mestres, Gerar Lançamentos e Excluir Lançamentos de forma automática. É possível informar um range de produtos e configurar conforme desejado.

**OBS:** Por essa opção, caso tenha um produto bloqueado (B1\_MSBLQL = 1) será gerado o help MSBLQL e o mestre para esse produto em específico não será gerado.

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
