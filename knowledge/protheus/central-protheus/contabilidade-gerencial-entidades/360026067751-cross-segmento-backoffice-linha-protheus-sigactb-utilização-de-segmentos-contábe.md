---
article_id: 360026067751
category: Contabilidade Gerencial - Entidades
content_hash: e82d086979eb2af224934848f9091f1efc4a991ff044fe26d5aa309a2d2dbc0c
fetched_at: '2026-06-28T22:40:49.702784+00:00'
product: protheus
section_id: 1500001537661
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - UTILIZAÇÃO DE SEGMENTOS
  CONTÁBEIS NA EMISSÃO DOS RELATÓRIOS
type: support-article
updated_at: '2022-07-18T20:11:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026067751-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-UTILIZA%C3%87%C3%83O-DE-SEGMENTOS-CONT%C3%81BEIS-NA-EMISS%C3%83O-DOS-RELAT%C3%93RIOS
---

**Dúvida**

Utilização de segmentos contábeis no relatório com base na mascara contábil.  
  
**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus – Contabilidade gerencial  – A partir da versão 11.80 **Solução**

A maioria dos relatórios contábeis é possível utilizar filtro dos segmentos das entidades contábeis.

Para utilização dos segmentos, antes é necessário  configurar a mascara das entidades contábeis através da rotina CTBA130

1 - Primeiro passo é cadastrar a mascara contábil

2 - Depois através da configuração de livros, associar o código da mascara contábil criada.

3 - No plano de contas, no campo Conf.Livros (CT1\_BOOK) informar o código do livro  associado a mascara contábil, nas contas contabeis que serão utilizadas no segmento.

Este procedimento pode ser utilizado para todas as entidades contábeis (conta contábil, centro de custo, item contábil e classe de valor)

Na emissão do relatório, informar o código de configuração do livro, filtrar o segmento e o conteúdo do segmento que será demonstrado no relatório.
