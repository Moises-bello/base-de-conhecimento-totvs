---
article_id: 360018057112
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: d92c6887fd91adb84ccdfd744c98180b7ae456613718d6ca9b8ead1475036d8c
fetched_at: '2026-06-28T22:38:30.013152+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Parâmetro MV_REGDPRI
type: support-article
updated_at: '2022-12-09T12:02:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018057112-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Par%C3%A2metro-MV-REGDPRI
---

**Dúvida**

Qual a finalidade do MV\_REGDPRI ?

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT- a partir da versão 11.  
  
**Solução**

O parâmetro **MV\_REGDPRI** tem como definição Indicar a ordem de busca a ser considerada para avaliação da regra de desconto.  
  
Ele define qual o índice de pesquisa utilizado pra identificar se atende alguma regra de desconto, considerando 1 ou 2, que são os índices existentes na tabela ACO.

Cod. Regra  
Tabela Prec. + Cond.Pagto + Form.Pagto + Cliente + Loja + Faixa   
O parâmetro também aceita índices criados pelos usuários.

**Saiba mais**: [Regras de Desconto (FATA080)](https://tdn.totvs.com/x/dQ5dDg)
