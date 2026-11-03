---
article_id: 360025542772
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 86ee0e145479a518d55cf59197c934b00dc84f6cdfb25c0c8a04baef99c9e1e7
fetched_at: '2026-06-28T22:39:50.128638+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Nota Complementar
type: support-article
updated_at: '2026-02-02T11:32:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025542772-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Nota-Complementar
---

**Dúvida**  
Como gerar uma nota complementar de importação?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – SIGAEIC – Todas as versões  
  
**Solução**

A nota complementar contém todas as despesas base de custo que não fizeram parte da Nota (primeira/única/mãe). As despesas devem ter a seguinte configuração :

- Base de custo = SIM

- Base de imposto = NÃO

- Base de ICMS = NÃO

Para preencher os dados acesse:

1. Módulo SIGAEIC em  Atualizações / Financeiro / Cadastro Despesas

2. Realize a alteração ou inclusão da despesa, e preencha o campo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024705911)

Para gerar a nota complementar, realize os seguintes passos:  
1. Acessar a rotina desembaraço / Manutenção (EICDI502)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024706951)

2. Posicione no processo e selecione Outras ações / Despesa

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024707091)

3. Selecione Outras ações / Incluir

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024692832)

4. Preencha os dados referente a despesa.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024693052)

5. Acesse a rotina Desembaraço / Recebimento de importação (EICDI154)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024693232)

6. Posicione no processo e Complementar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024707711)
