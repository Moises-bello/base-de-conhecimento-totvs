---
article_id: 1500002044062
category: Ativo Fixo - Solicitação Baixa ou Transferência
content_hash: f00e30dfc984ff4d3c8400b4411942747675780a0da1c7d3b77705148fc1deb8
fetched_at: '2026-06-28T22:41:49.109769+00:00'
product: protheus
section_id: 1500001547622
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA060 - MENSAGEM "AFDTTRANS"
  NA TRANSFERENCIA DE ATIVO PARA OUTRA FILIAL
type: support-article
updated_at: '2023-12-01T15:06:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002044062-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA060-MENSAGEM-AFDTTRANS-NA-TRANSFERENCIA-DE-ATIVO-PARA-OUTRA-FILIAL
---

**Ocorrência**Na execução da transferência de ativos de uma filial para outra retorna mensagem **"A transferência só pode ocorrer no mês imediatamente posterior ao ultimo calculo mensal de correção e depreciação"**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102930073)

**Ambiente**Protheus – Ativo fixo – A partir da versão 12.1.17  
  
**Causa**As causas desta mensagem, ocorre porque na  filial destino esta com a data do ultimo calculo de depreciação diferente da filial de origem.  
  
**Solução**Verifique a data do ultimo calculo de depreciação (ATFA050) da filial destino esta posterior ou anterior a data do calculo da filial de origem.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102930513)

Veja :  [ATFA060 - Como funciona rotina Transferência de ativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015091671-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA060-Como-funciona-rotina-Transfer%C3%AAncia-de-ativo?source=search)
