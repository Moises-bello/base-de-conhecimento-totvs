---
article_id: 4773548466199
category: RH – DIRF
content_hash: c86a8758da4f832255897f539028f3fefc0b4d930b02427038188065ca951710
fetched_at: '2026-06-28T22:44:06.952890+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - De onde o sistema busca os dados para a DIRF de
  residente no exterior (expatriado)
type: support-article
updated_at: '2025-08-18T14:59:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4773548466199-RH-Linha-Protheus-GPE-De-onde-o-sistema-busca-os-dados-para-a-DIRF-de-residente-no-exterior-expatriado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34262912806423) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**De onde o sistema busca os dados para a DIRF de residente no exterior (expatriado)?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**O sistema valida o cadastro realizado na rotina **Histórico de Contratos**, sendo que para o período cadastrado o sistema considera o código de retenção informado na aba Residente Exterior.  
A rotina fica no caminho **>Atualizações >Funcionários >Histórico de Contratos**.  
  
Abaixo exemplo de cadastro para expatriado na rotina Histórico de Contratos:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4773142218135)  
  
Aba residente exterior:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4773184462231)  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4773425106327)  
  
Após executar a rotina Gerar Arquivo, em Manutenção de Arquivo será demonstrado os valores referente ao período que consta em Histórico de Contrato. No exemplo abaixo foi executado o cálculo em regime de caixa:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9205147678743)

**Saiba mais**

[RH-DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF?page=2#articles)
