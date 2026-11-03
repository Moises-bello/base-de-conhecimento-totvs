---
article_id: 360025659813
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 186ecc423cc3313480eb0b40dc05db430d2c989675375992a52d53f47e72c233
fetched_at: '2026-06-28T22:38:38.701494+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - SIGAFAT - Como Configurar a
  Análise de Crédito de todas as Filiais da Empresa
type: support-article
updated_at: '2023-07-12T21:03:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025659813-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Como-Configurar-a-An%C3%A1lise-de-Cr%C3%A9dito-de-todas-as-Filiais-da-Empresa
---

**Dúvida**

Como Configurar a Análise de Crédito de todas as Filiais da Empresa?

**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

Para essa configuração é necessário, no momento da **homologação do sistema**, definir o modo de **compartilhamento** das tabelas **SA1**, **SE1** e **SE5**, de forma igual, como Compartilhadas.

Com isso, quando o sistema analisar os títulos da filial corrente, ele conseguirá enxergar que o cliente possui títulos vencidos em outras filiais e gerará o bloqueio na liberação do pedido.

Caso seu **ambiente** já esteja **em produção**, impossibilitando a alteração do modo de compartilhamento das tabelas, utilize o **Ponto de Entrada**: [DT PE MAAVCRFIN Substituição da Query da Avaliação de Crédito Financeiro do Cliente](https://tdn.totvs.com/x/xAdxEg)

**Saiba Mais:** [Como configurar a Análise de Credito considerando todas as Filiais / Empresas do Sistema](https://tdn.totvs.com/x/1KW7E)
