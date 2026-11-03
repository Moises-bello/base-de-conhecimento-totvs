---
article_id: 360043003054
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: 64b0ae26229e721daf0fc3cbcd487d313314d80cfbba815f4f48624b0dd21e4d
fetched_at: '2026-06-28T22:41:43.192098+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA050 Depreciação
  por horas trabalhadas
type: support-article
updated_at: '2023-11-30T17:18:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043003054-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA050-Deprecia%C3%A7%C3%A3o-por-horas-trabalhadas
---

**Dúvida**Como funciona a depreciação por horas trabalhadas?  
  
**Ambiente**Protheus – Ativo Fixo – A partir da versão 11.80  
  
**Solução**A depreciação por horas trabalhadas funciona através da rotina **ATFA050**(calculo de depreciação), onde este método é visto através do campo **N3\_TPDEPR** do bem que deve estar igual a **5**:  
  
                                            ![](https://totvssuporte.zendesk.com/attachments/token/k3v3BBKgWGjfihI9MtCRJPmxT/?name=inline82012077.png)​   
  
Neste método é obrigatório o preenchimento dos campos **Prod. Período** (N3\_PRODMES) e **Prod. Previst.** (N3\_PRODANO), que determinam, respectivamente, unidade produzida por mês e unidade produzida no período.  
  
**Características do cálculo:**  
  
A alíquota é variável e definida em função das horas trabalhadas no período.  
  
A fórmula para determinar a alíquota é::  
Taxa de depreciação = Horas trabalhadas no período / Horas uteis estimadas em função da vida útil do bem.  
  
A fórmula para determinar o valor da depreciação é:  
Depreciação = Valor Original Atualizado do Bem \* Taxa de depreciação  
  
Onde:  
***Valor original do bem:*** é considerado como valor original o valor de aquisição do bem, que dependendo da forma de atualização deste valor, pode conter as ampliações e as reavaliações sofridas desde sua aquisição.
