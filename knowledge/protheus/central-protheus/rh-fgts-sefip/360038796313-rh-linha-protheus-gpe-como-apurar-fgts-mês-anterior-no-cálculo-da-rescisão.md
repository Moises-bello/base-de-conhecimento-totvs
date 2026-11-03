---
article_id: 360038796313
category: RH - FGTS / SEFIP
content_hash: 5e028eb9ffdeac1a416b4ead8b95b8136006dbee512a6b36cb2ebb6b8560dada
fetched_at: '2026-06-28T22:43:41.171018+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Como apurar FGTS mês anterior no cálculo da rescisão
type: support-article
updated_at: '2026-06-26T17:16:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038796313-RH-Linha-Protheus-GPE-Como-apurar-FGTS-m%C3%AAs-anterior-no-c%C3%A1lculo-da-rescis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34697462327703) Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Como apurar FGTS mês anterior no cálculo da rescisão  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

1. Em **Atualizações> Definição de cálculo> Manutenção de Tabelas** - **S043 tipos de  rescisão**, preencha o campo fgts mês anterior como S.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050230134)  
  
2. Em **Atualizações> Cadastros> Verbas,** cadastre a verba com **id. de cálculo 0117 - FGTS Mês Anterior**, caso não tenha cadastrada  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050230714)  
  
3. Ex: folha aberta mês 04/2019 cálculo rescisão 05/2019.

A folha do mês 04 deve estar calculada para o funcionário. Após este processo calcule a rescisão, será apresentada a verba com **id 0117** no calculo da rescisão.  
  
**Observações:**Na geração da SEFIP será gerado o registro 32 indicando que houve rescisão não recolhendo o valor de FGTS e sim na GRRF.

**Saiba mais:**

[RH - FGTS/SEFIP](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003115651-RH-FGTS-SEFIP)
