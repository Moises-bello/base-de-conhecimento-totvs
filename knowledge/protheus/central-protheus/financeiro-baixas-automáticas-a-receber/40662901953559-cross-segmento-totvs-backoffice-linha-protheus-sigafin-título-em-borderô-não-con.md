---
article_id: 40662901953559
category: 'Financeiro - Baixas Automáticas a Receber '
content_hash: 8aa76ca468d3c7d18e69249ae57d02d8b9237dff79e00d3181d4ab0ef0a5a719
fetched_at: '2026-06-28T22:37:38.780570+00:00'
product: protheus
section_id: 35057325714199
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Título em borderô
  não considera banco informado no momento da baixa
type: support-article
updated_at: '2026-05-22T14:50:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40662901953559-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-T%C3%ADtulo-em-border%C3%B4-n%C3%A3o-considera-banco-informado-no-momento-da-baixa
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40662901948055)** Tempo aproximado para leitura: **00:07:00 min**  
  
**Dúvida**  
Quais são os LPs de contabilização do módulo financeiro online e off-line ?  
  
**Ambiente**  
Por que a rotina de baixa automática não considera o banco informado em tela (E1\_PORTADO) para baixa de títulos vinculados a borderô?

**Solução**   
Quando o número do borderô é preenchido na rotina de baixa automática, o sistema prioriza de forma automática o banco, a agência e a conta definidos no próprio borderô. Evitando assim, divergências.

Dessa forma, os dados bancários informados na tela e o parâmetro "**Filtra Bco Informado**" não influenciam o processamento, sendo desconsiderados para a definição da instituição de efetivação.

O banco informado na rotina somente definirá a conta de destino da baixa quando:

1. O título não estiver vinculado a um borderô;
2. O título estiver vinculado a um borderô, mas o número do borderô não for informado na tela de parâmetros da rotina.

Além disso, caso o parâmetro "**Filtra Bco Informado?"** esteja configurado como Sim, o banco, a agência e a conta informados em tela atuarão exclusivamente como filtros para a seleção e exibição dos títulos, não definindo o banco utilizado na baixa.

Dessa forma, para que a baixa utilize os **dados bancários do próprio borderô**, é necessário:

* informar o número do borderô na rotina;
* manter o parâmetro **“Filtra Bco Informado?”** configurado como **“Não”**.

Saiba Mais:

[FINA110 -Baixa Automática de Títulos a Receber](https://tdn.totvs.com/pages/releaseview.action?pageId=312167132)
