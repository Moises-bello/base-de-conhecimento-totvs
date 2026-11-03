---
article_id: 25280488301335
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 77f58bd6658ddb41220ed2c70b5f730100786567ab76d31766e03fa3ec737877
fetched_at: '2026-06-28T22:39:50.085902+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Help AVG0000258
  Problema: Despesa não pode ser Excluída pois o Processo possui NFs de entrada'
type: support-article
updated_at: '2024-07-31T14:16:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25280488301335-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Help-AVG0000258-Problema-Despesa-n%C3%A3o-pode-ser-Exclu%C3%ADda-pois-o-Processo-possui-NFs-de-entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25280474996503) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao tentar excluir uma despesa de importação, apresenta o Help AVG0000258 " Problema: Despesa não pode ser Excluída, pois o Processo possui NFs de entrada", como corrigir?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Easy Import Control - A partir da versão 12.1.2210

**Solução**

A mensagem "**Help AVG0000258"** é apresentada, pois o processo já possui pré-nota de entrada emitida impossibilitando a exclusão da despesa, para prosseguir com o processo de exclusão da despesa será necessária fazer o estorno da pré-nota de entrada no Recebimento de Importação, rotina "**EICDI154**".

Mensagem:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25280474999191)**

**Passo a passo:**

* Exclusão da Pré-nota de entrada:
  1. Acesse o SIGAEIC - Atualizações - Desembaraço - Recebimento de Importação rotina **"EICDI154"** ;
  2. Selecione o processo, posicionando sobre o registro, selecione a opção com o tipo de nota que deseja excluir, selecione posteriormente a opção"Estorno"e confirme.

* Exclusão da despesa:
  1. Acesse o SIGAEIC - Atualizações - Desembaraço - Manutenção;
  2. Posicione sobre o processo e selecione a opção "Outras Ações" em seguida selecione a opção "Despesas";
  3. Posicione sobre a despesa que deseja excluir, selecione a opção "Outras Ações" em seguida a opção "Excluir" e confirme a exclusão.

**Exemplo do procedimento:**

![Gravar_2024_07_30_14_32_03_3.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/25280475000855)

**Saiba mais:**

[Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Estorno da Pré-Nota.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16703109172503-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Estorno-da-Pr%C3%A9-Nota)
