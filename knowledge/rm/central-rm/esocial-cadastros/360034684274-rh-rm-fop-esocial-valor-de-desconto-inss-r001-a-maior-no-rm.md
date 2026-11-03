---
article_id: 360034684274
category: eSocial - Cadastros
content_hash: b4029e32ca634a1e26e45852b5057da5f04bc5ae01cb75fca785fb3157366d06
fetched_at: '2026-06-28T22:47:14.564548+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: RH - RM - FOP - eSocial - Valor de desconto INSS R$0,01 a maior no RM
type: support-article
updated_at: '2024-06-26T15:16:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034684274-RH-RM-FOP-eSocial-Valor-de-desconto-INSS-R-0-01-a-maior-no-RM
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24447624708631) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**O que fazer quando no relatório de **Conferência INSS,** o valor de desconto INSS está R$ 0,01 (1 centavo) a maior do que a base do RM?  
  
**Ambiente** TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Geralmente o valor de desconto INSS fica a maior no RM em R$ 0,01 quando o RM está parametrizado para arredondar o valor de desconto INSS. No cálculo de desconto INSS do governo não é realizado este arredondamento.

**Solução**  
1. Para que os valores sejam calculados conforme eSocial acesse **Administração de Pessoal | Cálculos | Tabelas de Cálculo** e desmarque o parâmetro **Arredondar Valores;**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045050394)

2. Após o ajuste do parâmetro deverá realizar o recálculo do envelope;

3. Retifique o evento S-1200 ou S-2299.
