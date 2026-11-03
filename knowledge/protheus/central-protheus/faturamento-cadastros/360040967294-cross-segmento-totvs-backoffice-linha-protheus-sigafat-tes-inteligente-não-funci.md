---
article_id: 360040967294
category: Faturamento - Cadastros
content_hash: 6cca90d92419d1d17de31a56d94f552588f7b7f0f3b44eaa583b717c99ef12b9
fetched_at: '2026-06-28T22:38:36.652349+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - TES Inteligente
  não funciona ao utilizar Prospect
type: support-article
updated_at: '2024-04-24T13:20:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040967294-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-TES-Inteligente-n%C3%A3o-funciona-ao-utilizar-Prospect
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Por que o TES Inteligente não funciona ao utilizar um Prospect?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – FAT – A partir da versão 12  
  
**Solução**

Em rotinas como **Televendas (TMKA271)** ou **Orçamento de Vendas (MATA415)** é possível inserir um **Prospect** como comprador, nestas rotinas também está disponível o campo “**Tipo de Operação**” para uso do **TES Inteligente**, porém o TES Inteligente não pode ser executado com Prospects, somente em **Clientes (SA1)** ou **Fornecedores (SA2)**.  
  
A função que executa o TES inteligente é a "**MaTesInt**", ela está declarada no fonte **MATA089**, esta é uma função fiscal que só trata as **tabelas SA1 e SA2**, não tratando o Prospect (**tabela SUS**) independentemente da rotina.
