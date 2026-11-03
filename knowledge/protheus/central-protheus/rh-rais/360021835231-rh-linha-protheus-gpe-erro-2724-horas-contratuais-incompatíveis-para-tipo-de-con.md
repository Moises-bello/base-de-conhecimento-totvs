---
article_id: 360021835231
category: RH - RAIS
content_hash: db6ca9618620dd11982336ef879fc399ee4f0661da1d38075f3c3074370be12e
fetched_at: '2026-06-28T22:44:05.694067+00:00'
product: protheus
section_id: 360000030327
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro 2724: horas contratuais incompatíveis para
  tipo de contrato parcial'
type: support-article
updated_at: '2025-09-04T20:43:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021835231-RH-Linha-Protheus-GPE-Erro-2724-horas-contratuais-incompat%C3%ADveis-para-tipo-de-contrato-parcial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34709202443927) Tempo aproximado para leitura: 00:01:00 min  
  
Ocorrência**Erro 2724: horas contratuais incompatíveis para tipo de contrato parcial  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 11.80  
  
**Causa**A mensagem é gerada quando os funcionários de contrato parcial possuem as horas mensais maior que o permitido.   
De acordo com a Lei 13.467/2017 (que alterou o art. 58-A da CLT), o trabalho em regime de tempo parcial passou a ser válido nas seguintes hipóteses:  
a) **Aquele cuja duração não exceda a 30 (trinta) horas semanais**, sem a possibilidade de horas suplementares semanais, ou  
b)**Aquele cuja duração não exceda a 26 (vinte e seis) horas semanais**, com a possibilidade de acréscimo de até seis horas suplementares semanais.

Para o contrato de trabalho a tempo parcial a jornada normal mensal, considerando as hipóteses acima citadas será:  
a) Se a jornada for de até 30 horas semanais, a jornada mensal será de 150 horas (30 horas x 5 semanas);  
b) Se a jornada for de até 26 horas semanais, a jornada mensal será de 130 horas (26 horas x 5 semanas).

**Solução**Entre no cadastro de funcionários (GPEA010) e ajustar o contrato de trabalho parcial (RA\_HOPARC) ou as horas mensais do funcionário (RA\_HRSMES). Observe a data base do sistema ao realizar a alteração pois ela será gravada na tabela de alterações (SR9) e válida a partir dessa data.  
Se muitos funcionários estiverem com as horas incompatíveis, solicite ao T.I a alteração em lote do campo.

**Saiba mais:**

[RH - RAIS](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030327-RH-RAIS)
