---
content_hash: 41f4c2e158cf2d04928e74aaca92c73f863eefd31374f9d33cd6552c57b22d86
fetched_at: '2026-06-28T21:35:30.155742+00:00'
page_id: '808476695'
product: fluig
source: tdn-fluig
title: Atualização para a nova versão do FLUIG.chart
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=808476695
version: 9
---

# Índice

4true.\*ndicenone

## Objetivo

---

Este guia tem por objetivo auxiliar os usuários a seguir o passo a passo necessário para identificação dos pontos onde é necessária a revisão e atualização do código, por conta da atualização de bibliotecas que tivemos. Mais uma medida para reforçar ainda mais a segurança do Fluig.

## Identificação do que precisa ser ajustado

---

Na versão **1.8.2 do Fluig <VALIDAR>**, por conta de uma vulnerabilidade, liberamos no Style Guide uma atualização dos plugins base do componente **FLUIGC.chart**, que são o **Chart.js** e o **Gauge.js**.

Na versão **2.9.4** do **Chart.js**, algumas dessas propriedades foram alteradas ou removidas, enquanto outras ainda são suportadas com pequenas modificações. Abaixo estão as informações para cada propriedade.

**Legenda de alterações**

**Breaking Change:** Alteração significativa que pode impactar o código existente, geralmente modificando a interface da API. Pode causar problemas em casos específicos.

**Feature (Recurso):** Adição à API que normalmente não afeta o código existente. Introduz novas funcionalidades, mas há a possibilidade de interações negativas com o código existente.

**Deprecated (Descontinuado):** Recurso ou API ainda presente, mas seu uso é desencorajado. Pode ser removido em futuras atualizações de versões principais.

## Breaking changes

---

### **Breaking Change: Gráfico LineBar removido. Agora utilize o gráfico Mixed.**

O gráfico `**chart.lineBar(data, options)**` foi removido. Agora o gráfico `**chart.mixed(data, options)**` deve ser usado em seu lugar. Exemplo:

jsRDark1true

### **Breaking Change: Somente um evento para todos os gráficos.**

Agora, quando você clica em alguma sessão do gráfico, todos eles emitem um mesmo evento, chamado `**fluig.chart.click**`. Os eventos abaixo foram removidos:

* line: 'fluig.chart.line.click'
* bar: 'fluig.chart.vertical.click'
* radar: 'fluig.chart.radar.click'
* polarArea: 'fluig.chart.polar.click'
* pie: 'fluig.chart.pie.click'
* doughnut: 'fluig.chart.doughnut.click'
* gauge: 'fluig.chart.gauge.click'
* donut: 'fluig.chart.donut.click'
* lineBar: 'fluig.chart.lineBar.click'
* horizontalBar: 'fluig.chart.horizontal.click'

Exemplo:

jsRDark1true

### **Breaking change: Nova estrutura de datasets para alguns gráficos**

Os gráficos `**polar**`, `**pie**` e `**doughnut**` sofreram uma modificação em sua estrutura de **datasets**. O motivo foi para equalizar a estrutura de todos os gráficos. Exemplo:

jsRDark1true

### **Breaking change: Propriedades removidas na estrutura do dataset.**

A estrutura geral de **datasets** dos gráficos mudaram. As propriedades `**fillColor**`, `**strokeColor**`, `**highlightFill**` e `**highlightStroke**` foram removidas. Agora deve ser usado as propriedades `**backgroundColor**`, `**borderColor**`, `**hoverBackgroundColor**` e `**hoverBorderColor**`. Exemplo:

jsRDark1true

### **Breaking change: Mudança para adicionar, remover ou atualizar dados nos gráficos.**

Agora, para realizar qualquer alteração em um dado no gráfico, é necessário utilizar o código a seguir:

jsRDark1true

### **Alterações por gráfico:**

#### **Gráfico do tipo Line**

| Propriedade | Situação | Orientação |
| --- | --- | --- |
| scaleShowGridLines | Removida | Para controlar as linhas de grade, agora você deve usar as configurações dentro de scales. |
| scaleGridLineColor | Removida | Use as configurações dentro de scales. |
| scaleGridLineWidth | Removida | Use as configurações dentro de scales. |
| pointDot | Removida | Use point dentro de elements em dataset para controlar os pontos. |
| pointDotRadius | Removida | Use radius dentro de point em elements no nível do conjunto de dados. |
| pointDotStrokeWidth | Removida | Use borderWidth dentro de point em elements no nível do conjunto de dados. |
| pointHitDetectionRadius | Removida | Use hitRadius dentro de point em elements no nível do conjunto de dados. |
| datasetStroke | Removida | Use borderColor dentro de datasets. |
| datasetFill | Removida | Use fill dentro de datasets. |
| legendTemplate | Removida | Não existe mais a propriedade legendTemplate. A lógica para personalizar a legenda agora deve ser feita na propriedade legend. Consulte a documentação para mais detalhes. |

#### **Gráfico do tipo Bar ou Horizontal Bar**

| Propriedade | Situação | Orientação |
| --- | --- | --- |
| scaleShowGridLines | Removida | Use as configurações dentro de scales para controlar as linhas de grade. |
| scaleGridLineColor | Removida | Use as configurações dentro de scales para definir a cor das linhas de grade. |
| scaleGridLineWidth | Removida | Use as configurações dentro de scales para definir a largura das linhas de grade. |
| barShowStroke | Removida | Use borderColor dentro de datasets para controlar se as barras têm uma borda. |
| barStrokeWidth | Removida | Use borderWidth dentro de datasets para controlar a largura da borda das barras. |
| barDatasetSpacing | Removida | A versão 2.9.4 usa barPercentage e categoryPercentage dentro de scales para controlar o espaçamento entre barras e conjuntos de dados. |
| legendTemplate | Removida | Não existe mais a propriedade legendTemplate. A lógica para personalizar a legenda agora deve ser feita na propriedade legend. Consulte a documentação para mais detalhes. |

#### **Gráfico do tipo Radar**

| Propriedade | Situação | Orientação |
| --- | --- | --- |
| scaleShowLine | Removida | Use as configurações dentro de scales para controlar a exibição das linhas do eixo. |
| angleShowLineOut | Removida | Não está mais disponível na versão 2.9.4. Considere usar outras propriedades em scales ou gridLines para obter o efeito desejado. |
| scaleShowLabels | Removida | Use as configurações dentro de scales para controlar a exibição de rótulos. |
| angleLineColor | Removida | Use as configurações dentro de gridLines em scales para definir a cor das linhas de grade radiais. |
| pointLabelFontFamily | Removida | Use as configurações dentro de ticks em scales para configurar a família da fonte. |
| pointLabelFontStyle | Removida | Use as configurações dentro de ticks em scales para configurar o estilo da fonte. |
| pointLabelFontSize | Removida | Use as configurações dentro de ticks em scales para configurar o estilo da fonte. |
| pointLabelFontColor | Removida | Use as configurações dentro de ticks em scales para configurar a cor da fonte. |
| pointDot | Removida | Use point dentro de elements em dataset para controlar a exibição de pontos. |
| pointDotRadius | Removida | Use radius dentro de point em elements no nível do conjunto de dados. |
| pointDotStrokeWidth | Removida | Use borderWidth dentro de point em elements no nível do conjunto de dados. |
| pointHitDetectionRadius | Removida | Use hitRadius dentro de point em elements no nível do conjunto de dados. |
| datasetStroke | Removida | Use borderColor dentro de datasets. |
| datasetStrokeWidth | Removida | Use borderWidth dentro de datasets. |
| datasetFill | Removida | Use fill dentro de datasets. |
| legendTemplate | Removida | Não existe mais a propriedade legendTemplate. A lógica para personalizar a legenda agora deve ser feita na propriedade legend. Consulte a documentação para mais detalhes. |

#### **Gráfico do tipo Polar**

| Propriedade | Situação | Orientação |
| --- | --- | --- |
| scaleShowLabelBackdrop | Removida | O recurso de fundo para rótulos de escala foi removido. |
| scaleBackdropColor | Removida | O fundo para rótulos de escala agora é controlado por backgroundColor em ticks dentro de scales. |
| scaleBackdropPaddingY | Removida | O preenchimento vertical para o fundo dos rótulos de escala agora é configurado por padding em ticks dentro de scales. |
| scaleBackdropPaddingX | Removida | O preenchimento horizontal para o fundo dos rótulos de escala agora é configurado por padding em ticks dentro de scales. |
| scaleShowLine | Removida | Use as configurações dentro de scales para controlar a exibição das linhas do eixo. |
| segmentShowStroke | Removida | A propriedade de controle de traçado de segmento foi removida. O controle de borda agora é feito usando borderColor dentro de datasets. |
| segmentborderColor | Removida | Use borderColor dentro de datasets para controlar a cor da borda do segmento. |
| segmentStrokeWidth | Removida | Use borderWidth dentro de datasets para controlar a largura da borda do segmento. |
| animationSteps | Removida | A animação agora é controlada por animation em options. |
| animationEasing | Removida | Use animation em options para controlar a função de easing. |
| animateRotate | Removida | Use animate em options para controlar a animação de rotação. |
| animateScale | Removida | Use animate em options para controlar a animação de escala. |
| legendTemplate | Removida | Não existe mais a propriedade legendTemplate. A lógica para personalizar a legenda agora deve ser feita na propriedade legend. Consulte a documentação para mais detalhes. |

#### **Gráfico do tipo Pie e Doughnut**

| Propriedade | Situação | Orientação |
| --- | --- | --- |
| segmentShowStroke | Removida | A propriedade de controle de traçado de segmento foi removida. O controle de borda agora é feito usando borderColor dentro de datasets. |
| segmentborderColor | Removida | Use borderColor dentro de datasets para controlar a cor da borda do segmento. |
| segmentStrokeWidth | Removida | Use borderWidth dentro de datasets para controlar a largura da borda do segmento. |
| animationSteps | Removida | A animação agora é controlada por animation em options. |
| animationEasing | Removida | Use animation em options para controlar a função de easing. |
| animateRotate | Removida | Use animate em options para controlar a animação de rotação. |
| animateScale | Removida | Use animate em options para controlar a animação de escala. |
| legendTemplate | Removida | Não existe mais a propriedade legendTemplate. A lógica para personalizar a legenda agora deve ser feita na propriedade legend. Consulte a documentação para mais detalhes. |
