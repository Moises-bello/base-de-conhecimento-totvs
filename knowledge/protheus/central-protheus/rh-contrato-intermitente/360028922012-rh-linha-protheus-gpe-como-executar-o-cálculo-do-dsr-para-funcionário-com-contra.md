---
article_id: 360028922012
category: RH - Contrato Intermitente
content_hash: a2e3e0fe2a74c51f0dd9ff74ba174d17f530f94c26402931f4433be4f2040d75
fetched_at: '2026-06-28T22:43:40.047108+00:00'
product: protheus
section_id: 360003139951
source: central-protheus
title: RH - Linha Protheus - GPE - Como executar o cálculo do DSR para funcionário
  com contrato intermitente
type: support-article
updated_at: '2025-04-24T14:14:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028922012-RH-Linha-Protheus-GPE-Como-executar-o-c%C3%A1lculo-do-DSR-para-funcion%C3%A1rio-com-contrato-intermitente
---

#### time.png Tempo aproximado para leitura: **00:02:30 min**

**Dúvida**Como executar o cálculo do DSR para funcionário com contrato intermitente?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Neste artigo será mostrado a forma de cálculo do DSR em 2 situações:   
  
**1.** Quando há **uma convocação** na semana que **possui o DSR**;  
  
Convocação no período de **22/11/2018 à 24/11/2018**:  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030353671)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030385372)  
  
Neste cenário, utilize a seguinte fórmula de cálculo:  
  
**DSR= Quant. de DSR na semana \* Valor da Verba Salário Horista (id 0032) / Quant. Dias de Convocação**  
DSR= 1 \* R$78,12 / 3  
DSR= R$26,04  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030361671)  
  
**2.** Quando há **duas****convocações ou mais** na semana que **possui o DSR**;  
  
Duas Convocações. Primeira convocação no período em **01/11/2018** e outra convocação em **03/11/2018**:  
  
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030363071)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052340013)  
  
Neste cenário, utilize a seguinte regra para o cálculo do DSR:  
  
**DSR= Convocação mais próxima do DSR.**No exemplo, será utilizado para o cálculo do DSR, a convocação mais próxima do DSR, neste caso, a convocação **000002 referente ao dia 03/11.**  
DSR= R$21,70 (valor do salário da convocação)  / 1 (quantidade de dias referentes a esta convocação)  
DSR= R$21,70  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052340633)

Obs.: os fontes **GPFORBRA, GPFO1BRA, GPFO2BRA, GPROTBRA, GPEXCAL1, GPEXINI, GPEXPER, GPEM020, GPEA010 e GPEA018** precisam estar atualizados para que o cálculo seja realizado de forma adequada.   
  
Será utilizado os **itens do calendário de pagamento** (tabela RCG) na aba cadastro de calendário do cadastro de períodos para verificar os dias de pagamento de DSR. 

**Mnemônico P\_CALCINTE**

Surgiu um questionamento de alguns clientes quanto a **forma de cálculo de DSR** e dos avos de férias e 13º, este questionamento foi enviado para nossa consultoria e um documento foi criado baseado nas informações existentes até o momento: [Orientação Consultoria de Segmentos](https://tdn.totvs.com/pages/releaseview.action?pageId=636952260)

Devido a **falta de orientações claras** quanto a forma correta de cálculo, e a divergência entre diversos clientes de qual seria o modelo adequado, foi criado o mnemônico **P\_CALCINTE,** que por padrão estará **desativado,** e, nesta condição, efetuará os cálculos conforme descrito na parte superior deste documento.

Caso o mnemônico seja ativado, o cálculo será efetuado da seguinte forma:

**DSR:**

Total de horas trabalhadas / 6 \* Salário Hora

**Férias e 13o. Salário**

Somatória dos proventos / 12 / 30 / Horas Diárias \* Total de Horas trabalhadas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29446472314391)  
  
**Saiba Mais**

[RH - Contrato Intermitente](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003139951-RH-Contrato-Intermitente)
