---
article_id: 13854639857175
category: RH - Provisão
content_hash: fd9c5662372b0a4d6a395316e1fc0a2f6c5c4b9809732e322f539f948a5607bf
fetched_at: '2026-06-28T22:43:55.622556+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: 'RH - Linha Protheus - GPE - Atenção: Tabelas S037 e S038 não estão cadastradas
  para o período de cálculo na Provisão'
type: support-article
updated_at: '2025-06-18T18:22:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13854639857175-RH-Linha-Protheus-GPE-Aten%C3%A7%C3%A3o-Tabelas-S037-e-S038-n%C3%A3o-est%C3%A3o-cadastradas-para-o-per%C3%ADodo-de-c%C3%A1lculo-na-Provis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32903379784087) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao Processar os Cálculos de Provisão de Férias e 13º Salário o sstema exibe o Help "Atenção: Tabelas S037 e S038 não estão cadastradas para o período de Cálculo".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13853575781399)

**Ambiente**TOTVS RH  TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - Todas as Versões.  
  
**Causa**Este incidente ocorre quando não há cadastro dos encargos de empresa nas tabelas S037 e S038 para uma ou mais das filiais indicadas nas perguntas do cálculo de provisão.

É necessário que todas as filiais que estejam dentro do range DE/ATE nas perguntas do cálculo de provisão, possuam cadastro das tabelas S037 e tabela S038, ou que o campo "Filial" destas tabelas esteja em branco.

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse: Atualizações / Definições de Cálculo / Manutenção de Tabelas / Localize a tabela S037 e clique em Outras Ações e em seguida em Alterar;   
  
2. Verifique se Todas as Filiais indicadas nas perguntas "Filial De?" e "Filial Até?" possuem cadastro na tabela.

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13854240562839)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13854287809815)  
Neste caso, Veja que não há cadastro para a filial D SP 02.  
  
3. Inclua o cadastro das Filiais faltantes, ou verifique a possibilidade de deixar o campo "Filial" em branco, para que o cadastro seja utilizado para Todas as Filiais.  
  
4. Realize a mesma validação na tabela S038.

**Saiba Mais:**[RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o) [Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
