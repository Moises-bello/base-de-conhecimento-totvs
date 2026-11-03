---
article_id: 16154478300951
category: SIGAEST - CONSULTAS
content_hash: 714acddcce6f3b9e11a60e13e432d42079be56bf1e76b981feacef8c4ee83436
fetched_at: '2026-06-28T22:38:48.972847+00:00'
product: protheus
section_id: 5367925055639
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATC030 - Funcionalidades
  do Kardex Diario
type: support-article
updated_at: '2025-03-12T12:18:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16154478300951-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATC030-Funcionalidades-do-Kardex-Diario
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16154522897687) Tempo aproximado para leitura: **00:04:00 min****Dúvida**Para que serve o Kardex Diário e quais suas funcionalidades para avaliação dos movimentos?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Ao invés de emitir um relatório para checagem do produto, é possível consultá-lo via Kardex em que são apresentados em tela os movimentos ocorridos dia a dia com cada produto.

Antes de iniciar avaliação do Kardex MATC030, é importante saber que: **Ele não foi preparado para analise com apropriação por "Empresa", ou seja MV\_CUSFIL = E**, caso seja necessario avaliar movimentações aglutinadas por empresa, utilizar do MATR900 - Kardex por periodo:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Como-configurar-corretamente-o-relat%C3%B3rio-Kardex-para-an%C3%A1lise-de-Custos-e-Movimenta%C3%A7%C3%B5es-?source=search>

**IMPORTANTE**: Primordial informação> Só se valida custeio de movimentações, após processamento do recalculo de custo médio.

**Perguntes:**

**Data inicial dos movimentos:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/16154528985879)**

Data inicial da movimentação a ser considerada no cálculo do saldo do produto.

**Data final dos movimentos:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/16154529517079)**

Data final da movimentação a ser considerada no cálculo do saldo do produto.

**Qual armazem:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/16154544951959)**

Digitar o Armazem do qual será feito o cálculo do Kardex (somente armazem ou por filial = \*\*)

**Saldo item a item:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/16154545305111)**

Será totalizado o saldo produto a produto.(sim ou nao)

**Qual moeda:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/16154552523543)**

Moeda a ser considerada no cálculo do kardex. (de 1 a 5)

**Mostra o endereço do produto:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/16154581585303)**

Considerar a visualização do Endereço e Número de Serie na consulta do kardex.

**Sequencia da consulta:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/16154565749655)**

Considera a sequência de impressão dos dados do kardex por Digitação, por Cálculo (sequencial, diario) ou por Calculo por apropriação Mensal.  
--Se Digitacao: não deve ser avaliado custo, somente entendido a ordem do movimentos.  
--Se Calculo: as movimentações são avaliados pela apropriação "diaria,sequencial".  
--Se Calculo mensal: as movimentações são avaliados pela apropriação "mensal".

**Listar as Transf do Produto:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/16154582600855)**

Considera a visualização das transferencias de Enderecos dos Produtos.

**Parte superior**

Apresenta os dados de identificação do produto como código, descrição, tipo, UM, grupo e saldos iniciais (quantidade, custo médio e custo total).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16154436003991)

**Parte central**

São relacionados todos os movimentos ocorridos no período especificado pelo usuário com as informações sobre a data do movimento, código do TES, código fiscal, número do documento, localização física, número de série, identificação, quantidade, custo médio e custo total.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16154483497623)

**Parte inferior**

São apresentados os saldos finais em estoque, totais das entradas e totais das saídas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16154499551895)

Para avaliação detalhada dos movimentos, e periodos, o suporte orienta o MATR900 - Kardex por perido.

**Saiba mais:**

*[MP - SIGAEST - Como fazer uma análise de Custos no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020860771)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
