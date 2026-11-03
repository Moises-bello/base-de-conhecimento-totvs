---
article_id: 360020437911
category: ADVPL - Classe e Função
content_hash: 4cc703b6c6f4ac1b804a07cdf5650682c9e0ff6665582ee314c1a21e2fc0f3ef
fetched_at: '2026-06-28T22:40:18.102364+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Tipos de produtos
  do padrão Protheus(SX5 - tabela 02)
type: support-article
updated_at: '2025-02-07T11:30:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020437911-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Tipos-de-produtos-do-padr%C3%A3o-Protheus-SX5-tabela-02
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29823661394327)*Tempo aproximado para leitura:**00:04:00 min  
  
Dúvida**Preciso saber se existe uma tabela dentro do Protheus onde eu possa ver quais são os tipos de produtos padrões para que eu possa desenvolver o ponto de entrada SPDFIS001 para os tipos de produtos incluídos por nós que vão como 99 para o registro 0200.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Não existe uma função ou qualquer outro recurso que identifique quais tipos foram cadastrados pelo usuário na tabela 02 da SX5.  
A seguir a listagem dos tipos padrões, e ao lado a numeração que o sistema irá usar pra referenciar no registro 0200 do Sped-Fiscal:

```
ME - 00: Mercadoria para Revenda  
MP - 01: Matéria-Prima  
EM - 02: Embalagem  
PP - 03: Produto em Processo  
PA - 04: Produto Acabado  
SP - 05: Subproduto  
PI - 06: Produto Intermediário  
MC - 07: Material de Uso e Consumo  
AI - 08: Ativo Imobilizado  
SV - 09: Serviços  
OI - 10: Outros insumos  
SM - 11: Sementes  
BN - 99: Outras  
GE - 99: Outras  
GG - 99: Outras  
KT - 99: Outras  
PV - 99: Outras  
SL - 99: Outras  
GN - 99: Outras  
IA - 99: Outras  
II - 99: Outras  
IN - 99: Outras  
MM - 99: Outras  
MO - 99: Outras
```

Hoje o Protheus conta com os 23 tipos listados acima por padrão, qualquer outro registro acrescentado será referenciado com 99 Outras.  
  
**Saiba mais**[SPDFIS001 - Trata tipos de produtos](http://tdn.totvs.com/display/public/PROT/SPDFIS001+-+Trata+tipos+de+produtos)
