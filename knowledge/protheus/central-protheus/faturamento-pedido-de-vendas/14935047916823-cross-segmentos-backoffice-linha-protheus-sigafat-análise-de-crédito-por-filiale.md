---
article_id: 14935047916823
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 6b6c9b093010aaec5b8001c056fc59102ae1bfe23c57d7ab8c285cba794b3847
fetched_at: '2026-06-28T22:38:42.481561+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Análise de crédito
  por filial/empresa
type: support-article
updated_at: '2024-08-23T13:17:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14935047916823-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-An%C3%A1lise-de-cr%C3%A9dito-por-filial-empresa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**

Como configurar a análise de crédito por empresa/filial?

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

Ao realizar a **Análise de Crédito**, o sistema pode considerar todas as **Lojas** (**A1\_LOJA**) do **Cliente** (**A1\_COD**), porém apenas da **Empresa**/**Filial** l**ogada**.

Para que o sistema avalie os **Títulos** de **Outras Empresas** / **Filiais**, é necessário o **Compartilhamento** das **tabelas SA1**, **SE1** e **SE5**. Com isso, quando o sistema Analisar os **Títulos da Empresa**/**Filial logada**, ele conseguirá **visualizar** se o **Cliente** possui **Títulos** em outras **Empresas**/**Filiais**.

Caso seu Ambiente já esteja em **Produção**, e **não** tenha interesse na **alteração** do **Modo de Compartilhamento** das tabelas, utilize o **Ponto de Entrada** abaixo:

* [**DT PE MAAVCRFIN Substituição da Query da Avaliação de Crédito Financeiro do Cliente**](https://tdn.totvs.com/x/xAdxEg)

Ele permite a **Alteração** da Query (busca) de **títulos** no sistema, sendo possível incluir as demais **Empresas** / **Filiais** na **Analise do Crédito do Cliente**.

**Saiba mais:  
[FAT0024 Configurações para Análise / Bloqueio de Crédito](https://tdn.totvs.com/x/Trl3DQ)**
