---
article_id: 360021663212
category: Financeiro - Contas a Pagar
content_hash: 492636b824edb9f32a0ac7a9a980baaeef9d90425e069419cd9cfbeb82a5d32a
fetched_at: '2026-06-28T22:38:07.139422+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Gerar único título
  para Pis, Cofins e CSLL
type: support-article
updated_at: '2022-08-04T23:47:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021663212-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Gerar-%C3%BAnico-t%C3%ADtulo-para-Pis-Cofins-e-CSLL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min**

**Dúvida**Como gerar retenção de Pis, Cofins e CSLL em um único título?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

É possível gerar a retenção de **Pis**, **Cofins** e **CSLL** em um único título com o valor total dos tributos por meio da configuração do parâmetro **MV\_AG10925**.

Instruções para inclusão do parâmetro, caso não exista no ambiente:

**Tipo:** Caracter

**Descrição:** Permite que sejam aglutinados os impostos **PIS**, **COFINS** e **CSLL** em apenas um titulo (Código de Retenção 5952).

**Conteúdo:**1 - Aglutina, 2 - Não aglutina

A natureza utilizada no título aglutinado será a informada no parâmetro **MV\_PISNAT**.
