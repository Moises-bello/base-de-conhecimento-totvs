---
article_id: 360025381513
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 132c0a501b13cad660d5342ffabc1abf06375df9a49507833062d76976e4633a
fetched_at: '2026-06-28T22:38:55.538906+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Funcionalidade do
  campo D3_EMPOP
type: support-article
updated_at: '2025-03-12T11:43:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025381513-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Funcionalidade-do-campo-D3-EMPOP
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28807095206935)**Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Qual a finalidade do campo D3\_EMPOP?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**O campo “**Empenho para OP (D3\_EMPOP)**”, é utilizado em todas as rotinas que movimentam estoque (internas), com a finalidade de sinalizar no momento da geração dos movimentos internos para produção, se houve a baixa do saldo empenhado nas tabelas **SB2 x SB8 x SBF**, garantindo a integridade dos saldos.

Este campo é utilizado para o controle de **requisições/devoluções para OP que não atualizam empenho**, nesse caso para que o campo esteja como "**N**" deve-se levar em consideração se as ordens de produção com o campo **D3\_EMPOP** como "**N**" tiveram os empenhos gerados e se ocorreu a baixa completa desses empenhos nos movimentos internos. Caso contrário o campo irá permanecer como "**N**"  
  
**Help do campo**  
Empenho para Ordem de Produção  
**S** - Utiliza Empenho para Produção  
**N** - Não Utiliza Empenho para Produção.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
