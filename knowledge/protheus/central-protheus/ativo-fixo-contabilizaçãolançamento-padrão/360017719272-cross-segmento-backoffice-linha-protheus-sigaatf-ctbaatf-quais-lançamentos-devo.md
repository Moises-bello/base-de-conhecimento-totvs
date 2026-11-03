---
article_id: 360017719272
category: Ativo Fixo - Contabilização/Lançamento padrão
content_hash: 4daf179962e86b4300e0773c259fb1c114dec2f28967073d5538527f8efc37a8
fetched_at: '2026-06-28T22:41:42.365125+00:00'
product: protheus
section_id: 1500001536421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - CTBAATF - Quais lançamentos
  devo utilizar na contabilização offline do ativo fixo
type: support-article
updated_at: '2023-11-30T19:32:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017719272-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-CTBAATF-Quais-lan%C3%A7amentos-devo-utilizar-na-contabiliza%C3%A7%C3%A3o-offline-do-ativo-fixo
---

**Dúvida**Quais lançamentos devo utilizar na contabilização offline do ativo fixo

**Ambiente**Protheus – Ativo Fixo – A partir da versão 11.80  
  
  
**Solução**

Devem ser utilizados os lançamentos padrões:

820 - Cálculo da Depreciação

830 - Correção da depreciação

Gerar os lançamentos contábeis *off-line* das correções monetárias, depreciações do ativo imobilizado e as correções das depreciações processadas pela rotina de cálculo. Ao executar a contabilização *off-line*, serão solicitadas as datas inicial e final para definir o período dos movimentos

Os processos das rotinas de transferência ATFA060 / baixa de ativos ATFA030 / inclusão de ativo ATFA010  tem suas contabilizações apenas on line, podendo parametrizar para contabilizar o Sim ou Não
