---
article_id: 4403410791063
category: RH - Provisão
content_hash: 3d7eaf0d3885d0b91d42ddf1548dc0568a3bf0b970bb57a4c25088a0c399c279
fetched_at: '2026-06-28T22:43:55.837632+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como ocorre ajuste de saldo na provisão quando
  funcionário tem aumento salarial
type: support-article
updated_at: '2024-08-28T12:12:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403410791063-RH-Linha-Protheus-GPE-Como-ocorre-ajuste-de-saldo-na-provis%C3%A3o-quando-funcion%C3%A1rio-tem-aumento-salarial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25949215316887) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como ocorre ajuste de saldo na provisão quando funcionário tem aumento salarial.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**

1. Geralmente, no cálculo do avo do mês, é apresentado o valor referente à 1/12 avos do salário do funcionário na Linha "No Mês":   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403451254679)

Considerando este exemplo, temos:  Salário R$ 1.200/12 = R$ 100,00.

2.  Na competência seguinte, houve um reajuste e o salário do colaborador aumentou para RS 1.500,00:![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403441928471)

3. Ao Processar o próximo mês de provisão na linha "No Mês" será apresentado o ajuste do valor da provisão com o valor de 1/12 avo mais o ajuste do saldo, considerando o salário atual do funcionário: ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403451399575)

**Cálculo:** R$ 1500,00/12 = R$ 125,00 (avo atual)

R$ 125,00 (avo atual) - R$ 100,00 (avo mês anterior) = R$ 25,00 (diferença do saldo)  
R$ 125,00 + R$ 25,00 = **R$ 150,00** (avo do mês + ajuste de saldo). 

**Dica:** Para facilitar, a conferência também pode ser realizada considerando o Saldo Atual - Anterior:

Cálculo do Valor Atual : Salário / 30 x 5 dias de Férias = 1.500 / 30 x 5 = 250,00  
Cálculo do Valor No Mês: Atual - Anterior = 250,00 - 100 = **150,00**

**Saiba Mais:**[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
