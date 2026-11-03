---
article_id: 360022223292
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 1237929bfcc2d0876420ddda7f574a40c7093fe9e8d5a3a87f3907f40312c4fd
fetched_at: '2026-06-28T22:37:19.934565+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como é feito Cálculo
  Rateio do Cronograma Físico ?
type: support-article
updated_at: '2022-05-19T20:44:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022223292-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-%C3%A9-feito-C%C3%A1lculo-Rateio-do-Cronograma-F%C3%ADsico
---

**Dúvida**Como é feito Cálculo Rateio do Cronograma Físico ?  
  
**Ambiente**Microsiga Protheus - Gestão de Contratos – A partir da versão 11.80  
  
**Solução**O cálculo que o sistema efetua no rateio do cronograma físico é feito com base no campo de quantidade. A precisão deste cálculo é determinada pelas casas decimais do campo CNS\_PRVQTD (por padrão do sistema os decimais são 4).  
Quanto maior a precisão das casas decimais deste campo, menor será a diferença lançada nas últimas parcelas.

**Exemplo**:  
No cálculo ( 1(**Quantidade**) **/** 6 (**Parcelas**) =**0.1666** (Fator de multiplicação de cada **item**), aumentando as casas decimais do campo **CNS\_PRVQTD** de 4 para 5, o fator de multiplicação de cada item seria **0,16666** ao invés de **0,1666**, o que aumenta a precisão do cálculo.

Saiba Mais:

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
