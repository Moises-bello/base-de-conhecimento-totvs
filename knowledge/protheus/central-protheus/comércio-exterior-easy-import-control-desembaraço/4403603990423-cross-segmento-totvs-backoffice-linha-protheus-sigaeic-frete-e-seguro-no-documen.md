---
article_id: 4403603990423
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 2b7ba9b958ab89f40de0d67c46281932cac93d351374576f16506eeb492d112f
fetched_at: '2026-06-28T22:39:49.765596+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: ' Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - Frete e Seguro
  no Documento de Entrada do Compras'
type: support-article
updated_at: '2021-07-02T15:01:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403603990423--Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Frete-e-Seguro-no-Documento-de-Entrada-do-Compras
---

**Dúvida**Preenchimento do Valor do Frete e Seguro no Documento de Entrada para nota de Importação.

**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**

Para processos de importação as informações referente o Frete e Seguro, não devem ser apresentados nos campos de Frete e Seguro do documento de entrada, pois os valores de Frete e Seguro internacional já estão no valor da mercadoria (Valor aduaneiro).  
  
Validação para apresentar os campos "If Empty(SC7->C7\_SEQUEN)" sempre que um pedido vier do SIGAEIC este campo sera preenchido.  
  
Os campos de frete e seguro são para notas nacionais não de importação e não podem ser preenchidas, conforme a legislação.  
  
"2.4. Os campos "Valor Total do Frete" e "Valor Total do Seguro" da NF-e de Importação não devem ser preenchidos, pois:  
  
2.4.1. O campo "Valor Total dos Produtos e Serviços" deve ser preenchido com o valor aduaneiro da mercadoria ou bem, constante da Declaração de Importação, que já inclui frete e seguro internacionais.  
  
2.4.1.1. De acordo com o artigo 77 do Decreto Federal 6.759/2009 (Regulamento Aduaneiro), integram o valor aduaneiro: (a) o custo de transporte da mercadoria importada até o porto ou o aeroporto alfandegado de descarga ou o ponto de fronteira alfandegado onde devam ser cumpridas as formalidades de entrada no território aduaneiro; (b) os gastos relativos à carga, à descarga e ao manuseio, associados ao transporte da mercadoria importada, até a chegada aos locais referidos; e (c) o custo do seguro da mercadoria durante as operações referidas.  
  
2.4.2. Os valores de frete e seguros nacionais não devem ser incluídos na NF-e de Importação, pois não compõem o custo de importação da mercadoria."
