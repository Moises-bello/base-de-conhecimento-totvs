---
article_id: 360021479272
category: Financeiro - Movimentação Bancária
content_hash: 7f439a5f9d7e969741546a6c433825f6f09a0636c74906ef363d7e87a56b316d
fetched_at: '2026-06-28T22:38:19.527814+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: MP - SIGAFIN - FINR470 - Extrato Bancário conversão errada de valores em moeda
  dolar
type: support-article
updated_at: '2021-04-28T15:52:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021479272-MP-SIGAFIN-FINR470-Extrato-Banc%C3%A1rio-convers%C3%A3o-errada-de-valores-em-moeda-dolar
---

**Ocorrência**Ao gerar o extrato bancário financeiro entre moeda dólar e real, na conversão para reais o sistema converte errado.  
   
 **Ambiente**Microsiga Protheus – Financeiro – FINR470 – A partir da versão 11.80

**Causa**Parâmetro errado no relatório “Converte Valores Pela?”

**Solução**A rotina **Extrato Bancário** (FINR470) o parâmetro referente a conversão de **Moedas MV\_PAR09 "Converte Valores Pela?**" Age conforme descrição abaixo:

**Taxa do Movimento:**   
Este parâmetro o sistema busca a taxa do **campo E5\_TXMOEDA** no qual é gravado com a taxa do dia da movimentação ou caso a taxa contratada foi informada esta sobrescreve a taxa do dia.

**Taxa do Dia:**   
Este parâmetro busca a taxa do dia logado no sistema do cadastro de moedas.
