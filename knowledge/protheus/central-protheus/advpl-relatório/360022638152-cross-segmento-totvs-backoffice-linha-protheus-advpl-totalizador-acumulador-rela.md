---
article_id: 360022638152
category: ADVPL - Relatório
content_hash: a0baabcb74a707194dc21ab7b5474ca431ad592a2cf850e26f1f647115f08dab
fetched_at: '2026-06-28T22:40:22.911638+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Totalizador / Acumulador
  Relatório Totvs
type: support-article
updated_at: '2021-08-25T23:30:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022638152-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Totalizador-Acumulador-Relat%C3%B3rio-Totvs
---

**Dúvida**No Relatório totvs precisamos totalizar alguns campos da célula.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas versões  
  
**Solução**

Na secção Células -> Acumulador -> é possível cria uma regra, determine a célula que estará disponível no lado direito da janela acumulador e em formula faça sua tratativa.

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360082234314/Capturar.PNG)

**Definindo os Acumuladores:**

Os acumuladores permitem criar células com total, média, mínimo e máximo baseado em outras células numéricas e também criar células de contagem de ocorrências baseado em qualquer dado.

1. Clique em Acumulador e, sem seguida, em Adicionar.

A partir de um acumulador também são criados gráficos para apresentação ao final do relatório.

É apresentada a janela Acumulador dividida em 3 áreas:

**Acumulador**

* + Título  
    Define o tipo de acumulador que será criado: se totalizador, valor mínimo, máximo, média ou contador de ocorrências.
  + Agrupar por  
    Os acumuladores são criados baseados em uma célula agrupadora, por exemplo: para criar um acumulador que totalize as comissões faturadas pela venda de cada cliente, é necessário que os valores estejam agrupados por cliente.  
    Nessa caso, basta dar um duplo clique sobre o nome da célula Cliente, na relação de células à direita, para incluí-la no campo Agrupar por. É possível agrupar o acumulador por mais de uma célula.
  + Fórmula  
    É dado que será acumulado. Por exemplo: Comissão.  
    Nesse caso, basta dar um duplo clique sobre o nome da célula Comissão, na relação de células à direita, para incluí-la no campo Fórmula.  
    Pode-se utilizar expressões em AdvPL para composição do acumulador.
  + Imprimir no final do relatório  
    Os acumuladores podem ser impressos separadamente ao final do relatório como uma estatística dos dados apresentados.

**Gráfico**

A partir do acumulador pode-se criar diferentes tipos de gráficos (barra, linha, pizza etc). Os gráficos são gravados em arquivo .BMP, com o mesmo nome do arquivo do relatório.

Se existirem vários acumuladores com gráficos, os arquivos .BMP serão gravados em sequência (matr1501.bmp, matr1502.bmp, etc) no diretório de spool. Se excluído o arquivo .BMP, o gráfico deixará de ser exibido.

* + Nome  
    Define um nome para o gráfico.
  + Nome da série  
    Define o nome para a série do gráfico.
  + Imprimir no final do relatório  
    O gráfico será apresentado ao final do relatório.

**Célula**

* + Título  
    Define um título para a célula.
  + Tamanho  
    Define o tamanho da célula para a séria do gráfico.
  + Máscara  
    Define o formato do dado que será impresso.
  + Imprimir  
    Um acumulador pode ser utilizado apenas para criação de gráfico, assim, se não houver interesse em apresentá-lo no relatório, basta desmarcar esta opção.

**Saiba Mais**

**[Protheus Report](http://tdn.totvs.com/display/public/PROT/Protheus+Report)**
