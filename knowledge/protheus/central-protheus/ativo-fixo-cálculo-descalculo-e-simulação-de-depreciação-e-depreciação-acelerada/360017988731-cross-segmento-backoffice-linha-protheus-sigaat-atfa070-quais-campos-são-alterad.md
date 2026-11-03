---
article_id: 360017988731
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: eb4d8984c50ed73d0ca16658093cb107aec13d79c70b8e79da5830e1098b3794
fetched_at: '2026-06-28T22:41:43.218679+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAAT- ATFA070 -  Quais campos
  são alterados durante o processo de descalculo da depreciação.
type: support-article
updated_at: '2023-11-30T18:47:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017988731-Cross-Segmento-Backoffice-Linha-Protheus-SIGAAT-ATFA070-Quais-campos-s%C3%A3o-alterados-durante-o-processo-de-descalculo-da-deprecia%C3%A7%C3%A3o
---

**Dúvida**Quais campos são alterados durante o processo de descalculo da depreciação.

**Ambiente**Protheus – Ativo Fixo – A partir da versão 11.80  
  
  
**Solução**

Ao processar o descalculo, somente os movimentos de depreciação serão excluídos, da tabela de movimentos SN4  ocorrência N4\_OCOR=" 06" Depreciação.

Os saldos das tabelas  SN3 - Saldos/ Valores e  SN5 - Arquivo de Saldos, serão atualizados .

**Importante**

A rotina de Descálculo Mensal, pode ser utilizada somente para o último cálculo, para retornar os saldos.

O descalculo não cancela outras movimentações , apenas o calculo de depreciação.
