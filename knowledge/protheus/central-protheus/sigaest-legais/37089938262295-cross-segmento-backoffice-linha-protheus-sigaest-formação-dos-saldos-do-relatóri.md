---
article_id: 37089938262295
category: SIGAEST - LEGAIS
content_hash: 0f18e653c2fcffd368fb9b86473126f4088a176b3d6559134deb7659447b2e98
fetched_at: '2026-06-28T22:38:51.511751+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Formação dos saldos
  do relatório MATR462.
type: support-article
updated_at: '2025-12-17T16:39:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37089938262295-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Forma%C3%A7%C3%A3o-dos-saldos-do-relat%C3%B3rio-MATR462
---

O documento explica a lógica para calcular os campos Saldo do Trimestre Anterior, Estoque Final e Consumo no relatório Mapa de Produtos Controlados. O Saldo do Trimestre Anterior é a soma das entradas menos as saídas e produtos com TES de saída. Estoque Final segue a mesma regra no período atual. Consumo é a soma das saídas (D3\_QUANT).

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37089916122135) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**

Este documento tem como finalidade descrever a lógica utilizada para o cálculo dos campos Saldo do Trimestre Anterior, Estoque Final e Consumo apresentados no relatório de Mapa de Produtos Controlados.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

**- 1 - Saldo do Trimestre Anterior:**

É obtido através da soma dos valores do campo D1\_QUANT (movimentos de entrada) dos documentos que atualizam estoque (SF4->F4\_ESTOQUE == "S")  
menos a soma dos valores dos campos D2\_QUANT (movimentos de saída que atualizam estoque) e D3\_QUANT dos produtos que possuem TES de saída (SD3->D3\_TM > "500").

**- 2 - Estoque Final:**

Segue a mesma regra de cálculo do Saldo do Trimestre Anterior, considerando os movimentos dentro do período atual.

**- 3 - Consumo:**

É a soma dos valores do campo D3\_QUANT, representando as movimentações de saída do produto.

**ASSUNTOS RELACIONADOS**

[Mapa de Produtos Controlados (MATR462 - SIGAEST)](https://tdn.totvs.com/pages/releaseview.action?pageId=433238645)

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
