---
article_id: 9447659049751
category: SIGAEST - PROCESSAMENTOS
content_hash: 25ec267e13dac0b88ac89497eaf5a973161617a6834a11fc438e388c64a1d307
fetched_at: '2026-06-28T22:39:05.006619+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST- TOP ERROR -19 insuficient
  number of parameters
type: support-article
updated_at: '2025-03-12T12:20:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9447659049751-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-TOP-ERROR-19-insuficient-number-of-parameters
---

**Ocorrência**Ao efetuar Processamentos no módulo Estoque/Custos, ocorre o erro: "*TOP ERROR -19 insufficient number of parameters".* Como corrigir?  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - 12.1.27/12.1.33.  
  
**Causa**  
Esse incidente ocorre, pois a parametrização do sistema está incorreta para o Cálculo da Substituição Tributária na entrada de NF.  
  
**Solução**

A rotina Refaz Saldos - MATA300 da data de 13/10/2022, está contemplada com a correção do erro.

**[MATA300  12.1.33 - 13/10/2022](https://suporte.totvs.com/portal/p/10098/download?e=1084717)**

Para clientes que acessarem este artigo a partir de Dezembro de 2022, este fonte já estará contemplado na Expedição Contínua podendo ser baixado clicando abaixo:

[**Expedição Contínua - Estoque/Custos (release 12.1.33)**](https://suporte.totvs.com/portal/p/10098/download#detail/1039086)

OBS: Sempre aplicar pacotes primeiramente em ambiente de homologação com backup prévio do RPO.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Processamentos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033442-SIGAEST-PROCESSAMENTOS)
