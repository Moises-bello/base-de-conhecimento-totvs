---
article_id: 360023025352
category: Materiais - Compras (SIGACOM)
content_hash: 33dfc8dfc5ddd4151f66bc55e1ee215acf300d884486084d4d65c1805f1fa5da
fetched_at: '2026-06-28T22:41:07.634930+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como fazer Análise
  de Cotação por Pesos ?
type: support-article
updated_at: '2022-05-16T22:19:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023025352-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-fazer-An%C3%A1lise-de-Cota%C3%A7%C3%A3o-por-Pesos
---

**Dúvida**Como fazer Análise de Cotação por Pesos ?

**Ambiente**Protheus – Compras – A partir da versão 12  
  
**Solução**

Como fazer Análise de Cotação por Pesos ? Há como estabelecer uma regra para o sistema considerar algum fator específico ?

Sim, é possível através dos perguntes do F12 com orientações sobre os campos: Peso Preço, Peso Prazo, Peso Nota.

**Valores:** Os campos aceitam valores de 0 à 9.

**Explicação:** Conforme maior for o valor escolhido, maior será  a relevância sobre os demais campos, pois ele terá um peso maior na análise de cotação.

**Exemplo 1:**Se os campos forem preenchidos da seguinte forma:

* ***Peso Preço**: 3*
* ***Peso Prazo**: 9*
* ***Peso Nota**: 5*

Baseado no exemplo acima, a ordem de prioridade feita pela análise será: 1º Peso Prazo - 2º Peso Nota - 3º Peso Preço.

**Exemplo 2:**Se os campos forem preenchidos da seguinte forma:

* ***Peso Preço**: 2*
* ***Peso Prazo**: 2*
* ***Peso Nota**: 1*

Se existir campos com os valores iguais, nesse caso o sistema entende que o primeiro fornecedor que for encontrado será o campeão, pois como os pesos são iguais, não há fator de diferenciação.
