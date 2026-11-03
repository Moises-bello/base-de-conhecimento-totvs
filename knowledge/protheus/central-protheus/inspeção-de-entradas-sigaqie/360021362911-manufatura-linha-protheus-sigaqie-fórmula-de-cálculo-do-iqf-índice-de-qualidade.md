---
article_id: 360021362911
category: Inspeção de Entradas (SIGAQIE)
content_hash: e32c94b7f384211f05fc6e1a7957bb0721732bebba2ae7b43950d6efe3aeeef8
fetched_at: '2026-06-28T22:42:26.977953+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Fórmula de cálculo do IQF - Índice
  de Qualidade do Fornecedor
type: support-article
updated_at: '2023-07-21T19:18:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021362911-Manufatura-Linha-Protheus-SIGAQIE-F%C3%B3rmula-de-c%C3%A1lculo-do-IQF-%C3%8Dndice-de-Qualidade-do-Fornecedor
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16197780516503)**Tempo aproximado para leitura: **00:01:07 min  
  
Dúvida**Como é realizado o cálculo do **IQF - Índice de Qualidade do Fornecedor**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Solução**Para identificar quais são as fórmulas utilizadas no cálculo do **IQF**, acesse o **QIER110 -****Relatório de Fórmulas.**Verifique também de que forma os índices são gerados no Sistema a partir da rotina **QIEA240 - Índices do IQF**. Na terceira coluna, verifique se o índice é do tipo **Informado** ou **Calculado**.  
  
Se o índice for:

* **Informado**: os valores mensais para cada **produto** e **fornecedor** deverão ser cadastrados na rotina **QIEA280 -****Índices Mensais**, antes de gerar o **IQF**;
* **Calculado**: os valores serão gerados de acordo com a fórmula definida no **RdMake** - **QIEA231** que seja anexo.

**Saiba mais**  
A documentação detalhada sobre o cálculo dos índices está disponível no *link*: [Procedimento para Cálculo dos Índices](https://tdn.totvs.com/pages/releaseview.action?pageId=306858407)
