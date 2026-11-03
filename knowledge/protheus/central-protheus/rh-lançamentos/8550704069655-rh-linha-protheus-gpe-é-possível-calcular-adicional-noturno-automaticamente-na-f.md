---
article_id: 8550704069655
category: RH - Lançamentos
content_hash: a7c2086bebd6b694a154e35f9cd614161c496f661ba4477f5ddf0e2e3ff3758e
fetched_at: '2026-06-28T22:43:31.259183+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - É possível calcular adicional noturno automaticamente
  na folha de pagamento
type: support-article
updated_at: '2025-07-24T16:59:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8550704069655-RH-Linha-Protheus-GPE-%C3%89-poss%C3%ADvel-calcular-adicional-noturno-automaticamente-na-folha-de-pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26080518756119) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**É possível calcular adicional noturno automaticamente na folha de pagamento?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - Todas as versões.  
  
**Solução**Não é possível calcular automaticamente o adicional noturno para funcionários na folha de pagamento, mesmo que na tabela de horário padrão o horário do funcionário seja noturno.  
É necessário lançar a verba de adicional noturno na rotina de lançamentos por funcionários com as horas a serem pagas, para acessar a rotina, acesse **Atualizações > Lançamentos > Por Funcionários (GPEA580).**

**Exemplo**

**1.** Cadastro da verba de adicional noturno na rotina Verbas em **Atualizações > Definições de cálculo > Verbas (GPEA040)**:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8550524477591)  
 **2.** Lance a verba na rotina Lançamentos por Funcionário em **Atualizações > Lançamento > Por Funcionário (GPEA580)**:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8550547893527)  
  
**3.** Calcule a folha de pagamento em **Miscelânea > Cálculos > Por Roteiro (GPEM020)**:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8550603291543)  
  
**Observação**: Caso tenham muitos funcionários que seja necessário o lançamento, pode ser feito pela rotina de Lançamentos por Verbas ou por Importação de variáveis.

**Saiba mais**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)  
[RH - Linha Protheus - GPE - Como realizar a importação de variáveis](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018541331)   
[RH - Linha Protheus - GPE - Como realizar lançamentos na rotina Lançamentos por Verba](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8551768497815)
